import pygame
from config import Config

class NPC:
    def __init__(self, x, y, sprite_path, dialog_id=None):
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.sprite.get_rect(topleft=(x, y))
        self.dialog_id = dialog_id
        self.can_interact = False
        self.hint_alpha = 0
        
        # Загрузка спрайта подсказки
        self.hint_sprite = pygame.image.load(Config.HINT_SPRITE).convert_alpha()
        self.hint_rect = self.hint_sprite.get_rect()

    def update(self, player_rect, world_offset_x, available_dialogs):
        # Экранные координаты NPC
        screen_x = self.rect.x - world_offset_x
        npc_rect = pygame.Rect(screen_x, self.rect.y, self.rect.width, self.rect.height)
        
        # Проверка условий для взаимодействия
        self.can_interact = (
            player_rect.colliderect(npc_rect) and
            self.dialog_id is not None and
            self.dialog_id in available_dialogs
        )
        
        # Анимация подсказки
        if self.can_interact:
            self.hint_alpha = min(255, self.hint_alpha + 15)
        else:
            self.hint_alpha = max(0, self.hint_alpha - 15)

    def render(self, screen, world_offset_x):
        # Отрисовка NPC
        screen.blit(self.sprite, (self.rect.x - world_offset_x, self.rect.y))
        
        # Отрисовка подсказки
        if self.hint_alpha > 0 and self.can_interact:
            self.hint_sprite.set_alpha(self.hint_alpha)
            hint_x = self.rect.x - world_offset_x + (self.rect.width // 2) - self.hint_rect.width // 2
            hint_y = self.rect.y - self.hint_rect.height - 10
            screen.blit(self.hint_sprite, (hint_x, hint_y))