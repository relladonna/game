import pygame
from config import Config


class Player:
    def __init__(self):
        self.sprite = pygame.image.load(Config.PLAYER_SPRITE).convert_alpha()

        # Позиция у правого края мира (4056 - половина ширины экрана)
        self.world_x = 4056 - Config.SCREEN_WIDTH // 2
        self.world_y = Config.SCREEN_HEIGHT // 1.7

        # Rect для отрисовки (центр экрана)
        self.rect = self.sprite.get_rect(center=(Config.SCREEN_WIDTH // 2, self.world_y))
        self.speed = Config.PLAYER_SPEED
        self.direction = 1  # 1 - вправо, -1 - влево

    def update(self, keys):
        movement = 0

        if keys[pygame.K_RIGHT]:
            movement = -self.speed
            self.direction = -1
        elif keys[pygame.K_LEFT]:
            movement = self.speed
            self.direction = 1

        self.world_x += movement
        return movement

    def render(self, screen):
        flipped = pygame.transform.flip(self.sprite, self.direction < 0, False)
        screen.blit(flipped, self.rect)