import pygame
from config import Config
from entities.npc import NPC

class Ghost(NPC):
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            sprite_path=Config.GHOST_SPRITE,
            dialog_id="ghost_dialog"
        )
        self.flicker_timer = 0
        self.visible = True
        
    def update(self, player_rect, world_offset_x):
        super().update(player_rect, world_offset_x)
        
        # Эффект мерцания для призрака
        self.flicker_timer += 1
        if self.flicker_timer % 10 == 0:
            self.visible = not self.visible
            
        # Призрак появляется только при определенных условиях
        distance = abs((self.rect.x - world_offset_x) - player_rect.x)
        self.show_hint = distance < 200 and not self.dialog_shown
        
    def render(self, screen, world_offset_x):
        if self.visible:
            screen.blit(self.sprite, (self.rect.x - world_offset_x, self.rect.y))
            
        if self.hint_alpha > 0 and self.show_hint:
            hint_font = pygame.font.SysFont("Arial", 20)
            hint_text = hint_font.render("E", True, (200, 200, 255))
            hint_text.set_alpha(self.hint_alpha)
            hint_x = self.rect.x - world_offset_x + self.rect.width // 2 - hint_text.get_width() // 2
            hint_y = self.rect.y - 30
            screen.blit(hint_text, (hint_x, hint_y))