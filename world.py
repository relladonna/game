# world.py
import pygame
from config import Config
from entities.player import Player
from entities.aglaia import Aglaia
from entities.doctor import Doctor
from dialog_system import DialogSystem

class World:
    def __init__(self):
        try:
            self.font = pygame.font.Font(Config.FONT_PATH, 24)
        except:
            self.font = pygame.font.SysFont("Arial", 24)

        self.player = Player()
        self.npcs = [
            Doctor(1450, 315),
            Aglaia(1650, 315)
        ]

        try:
            self.background = pygame.image.load(Config.BACKGROUND).convert()
        except:
            self.background = pygame.Surface((4056, Config.SCREEN_HEIGHT))
            self.background.fill(Config.BG_COLOR)

        self.dialog_system = DialogSystem(self.font)
        self.world_offset_x = 0

    def update(self):
        keys = pygame.key.get_pressed()
        movement = self.player.update(keys)
        
        # Move world in opposite direction
        self.world_offset_x -= movement
        
        # World boundaries
        self.world_offset_x = max(0, min(self.world_offset_x, 4056 - Config.SCREEN_WIDTH))

        # Update NPCs
        for npc in self.npcs:
            npc.update(self.player.rect, self.world_offset_x)

    def render(self, screen):
        # Draw background with offset
        screen.blit(self.background, (-self.world_offset_x, 0))
        
        # Draw NPCs
        for npc in self.npcs:
            npc.render(screen, self.world_offset_x)
        
        # Draw player (fixed position)
        self.player.render(screen)
        
        # Draw dialogs
        self.dialog_system.render(screen)