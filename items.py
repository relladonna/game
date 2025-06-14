import pygame
from typing import Tuple, Optional
from config import Config

class Item:
    def __init__(self, x: int, y: int, item_data: dict):
        """
        Args:
            x, y: мировые координаты
            item_data: {
                'id': str, 
                'name': str,
                'description': str,
                'world_sprite': str,
                'inventory_sprite': str,
                'pickup_dialog': str (id диалога)
            }
        """
        self.world_x = x
        self.world_y = y
        self.data = item_data
        self.is_collected = False
        self.hint_visible = False
        self.hint_alpha = 0

        # Загрузка спрайтов
        self.world_sprite = self._load_sprite(item_data['world_sprite'])
        self.inventory_sprite = self._load_sprite(item_data['inventory_sprite'])
        self.rect = self.world_sprite.get_rect(center=(x, y))

    def _load_sprite(self, path: str) -> pygame.Surface:
        try:
            return pygame.image.load(path).convert_alpha()
        except:
            print(f"Ошибка загрузки спрайта: {path}")
            surf = pygame.Surface((40, 40), pygame.SRCALPHA)
            color = (255, 215, 0) if "world" in path else (200, 160, 60)
            pygame.draw.rect(surf, color, (0, 0, 40, 40), 3)
            return surf

    def update(self, player_rect: pygame.Rect, world_offset: Tuple[int, int]) -> Optional[str]:
        """Обновляет состояние предмета. Возвращает dialog_id если предмет подобран"""
        if self.is_collected:
            return None

        # Экранные координаты
        screen_x = self.world_x - world_offset[0]
        screen_y = self.world_y - world_offset[1]
        item_rect = pygame.Rect(
            screen_x - self.rect.w//2,
            screen_y - self.rect.h//2,
            self.rect.w,
            self.rect.h
        )

        # Проверка расстояния до игрока
        distance = max(
            abs(player_rect.centerx - screen_x),
            abs(player_rect.centery - screen_y)
        )

        # Логика подсказки
        self.hint_visible = distance < 120
        self.hint_alpha = min(255, self.hint_alpha + 15 if self.hint_visible else self.hint_alpha - 15)

        # Логика подбора
        if distance < 50:
            self.is_collected = True
            return self.data.get('pickup_dialog')
        return None

    def render(self, screen: pygame.Surface, world_offset: Tuple[int, int]):
        if self.is_collected:
            return

        screen_x = self.world_x - world_offset[0]
        screen_y = self.world_y - world_offset[1]

        # Отрисовка предмета
        screen.blit(self.world_sprite, (screen_x - self.rect.w//2, screen_y - self.rect.h//2))

        # Отрисовка подсказки
        if self.hint_alpha > 0:
            hint_img = pygame.image.load(Config.HINT_SPRITE).convert_alpha()
            hint_img.set_alpha(self.hint_alpha)
            hint_rect = hint_img.get_rect(center=(screen_x, screen_y - 40))
            screen.blit(hint_img, hint_rect)