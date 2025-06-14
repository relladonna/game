import pygame
from config import Config

class Inventory:
    def __init__(self, capacity: int = 6):
        self.slots = [None] * capacity
        self.slot_size = 50
        self.padding = 5
        self.start_x = (Config.SCREEN_WIDTH - (capacity * (self.slot_size + self.padding))) // 2
        self.start_y = 30
        self.selected_slot = None

    def add_item(self, item) -> bool:
        """Пытается добавить предмет в первый свободный слот"""
        for i in range(len(self.slots)):
            if self.slots[i] is None:
                self.slots[i] = item
                return True
        return False

    def handle_click(self, pos):
        """Обрабатывает клик по инвентарю, возвращает выбранный предмет"""
        for i, item in enumerate(self.slots):
            slot_rect = pygame.Rect(
                self.start_x + i * (self.slot_size + self.padding),
                self.start_y,
                self.slot_size,
                self.slot_size
            )
            if slot_rect.collidepoint(pos):
                self.selected_slot = i
                return item
        return None

    def render(self, screen: pygame.Surface, font: pygame.font.Font):
        # Фон инвентаря
        bg_width = len(self.slots) * (self.slot_size + self.padding)
        bg = pygame.Surface((bg_width, self.slot_size + 10), pygame.SRCALPHA)
        bg.fill((50, 50, 50, 180))
        screen.blit(bg, (self.start_x - 5, self.start_y - 5))

        # Отрисовка слотов и предметов
        for i, item in enumerate(self.slots):
            slot_rect = pygame.Rect(
                self.start_x + i * (self.slot_size + self.padding),
                self.start_y,
                self.slot_size,
                self.slot_size
            )
            
            # Рамка слота
            color = (220, 220, 0) if i == self.selected_slot else (150, 150, 150)
            pygame.draw.rect(screen, color, slot_rect, 2)

            # Предмет в слоте
            if item:
                scaled_sprite = pygame.transform.scale(
                    item.inventory_sprite,
                    (self.slot_size - 8, self.slot_size - 8)
                )
                screen.blit(scaled_sprite, (slot_rect.x + 4, slot_rect.y + 4))

        # Описание выбранного предмета
        if self.selected_slot is not None and self.slots[self.selected_slot]:
            item = self.slots[self.selected_slot]
            desc = f"{item.data['name']}: {item.data['description']}"
            text = font.render(desc, True, (255, 255, 255))
            screen.blit(text, (20, Config.SCREEN_HEIGHT - 30))