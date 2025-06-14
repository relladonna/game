import pygame


class NPC:
    def __init__(self, x, y, sprite_path, dialog_id):
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.sprite.get_rect(topleft=(x, y))
        self.dialog_id = dialog_id
        self.dialog_shown = False
        self.can_interact = False  # Может ли игрок начать диалог
        self.show_hint = False      # Показывать ли подсказку
        self.hint_alpha = 0        # Прозрачность подсказки

    def update(self, player_rect, world_offset_x):
        # Проверяем коллизию в мировых координатах
        npc_world_rect = pygame.Rect(
            self.rect.x - world_offset_x,
            self.rect.y,
            self.rect.width,
            self.rect.height
        )
        self.can_interact = player_rect.colliderect(npc_world_rect)
        
        # Плавное появление/исчезание подсказки
        if self.can_interact and not self.dialog_shown:
            self.hint_alpha = min(255, self.hint_alpha + 10)
        else:
            self.hint_alpha = max(0, self.hint_alpha - 10)

    def render(self, screen, world_offset_x):
        screen.blit(self.sprite, (self.rect.x - world_offset_x, self.rect.y))
        
        # Отрисовка подсказки (например, иконка "E")
        if self.hint_alpha > 0:
            hint_font = pygame.font.SysFont("Arial", 20)
            hint_text = hint_font.render("E", True, (255, 255, 255))
            hint_text.set_alpha(self.hint_alpha)
            hint_x = self.rect.x - world_offset_x + self.rect.width // 2 - hint_text.get_width() // 2
            hint_y = self.rect.y - 30
            screen.blit(hint_text, (hint_x, hint_y))