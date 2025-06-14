# Aglaia.py (финальная версия)
import pygame
from config import Config
from entities.npc import NPC

class Aglaia(NPC):
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            sprite_path=Config.AGLAIA_SPRITE,
            dialog_id="aglaia_dialog"
        )
        # Подсказка
        self.hint_sprite = pygame.image.load(Config.HINT_SPRITE).convert_alpha()
        self.hint_rect = self.hint_sprite.get_rect()
        self.show_hint = False
        self.hint_alpha = 0

    def update(self, player_rect, world_offset_x):
        # Проверка расстояния до игрока
        npc_world_rect = pygame.Rect(
            self.rect.x - world_offset_x,
            self.rect.y,
            self.rect.width,
            self.rect.height
        )
        
        self.show_hint = player_rect.colliderect(npc_world_rect)
        
        # Плавное появление/исчезание подсказки
        if self.show_hint:
            self.hint_alpha = min(255, self.hint_alpha + 10)
        else:
            self.hint_alpha = max(0, self.hint_alpha - 10)

    def render(self, screen, world_offset_x):
        # Отрисовка NPC
        screen.blit(self.sprite, (self.rect.x - world_offset_x, self.rect.y))
        
        # Отрисовка подсказки
        if self.hint_alpha > 0:
            self.hint_sprite.set_alpha(self.hint_alpha)
            hint_x = self.rect.x - world_offset_x + (self.rect.width // 2) - self.hint_rect.width // 2
            hint_y = self.rect.y - self.hint_rect.height - 5
            screen.blit(self.hint_sprite, (hint_x, hint_y))