# player.py
import pygame
from config import Config

class Player:
    def __init__(self):
        self.sprite = pygame.image.load(Config.PLAYER_SPRITE).convert_alpha()
        self.rect = self.sprite.get_rect(center=(Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT // 1.8))
        self.speed = Config.PLAYER_SPEED
        self.direction = 1  # 1 - right, -1 - left

    def update(self, keys):
        movement = 0
        if keys[pygame.K_LEFT]:
            movement += self.speed
            self.direction = 1
        if keys[pygame.K_RIGHT]:
            movement -= self.speed
            self.direction = -1
        return movement

    def render(self, screen):
        flipped = pygame.transform.flip(self.sprite, self.direction < 0, False)
        screen.blit(flipped, self.rect)