import pygame

# Константы
WIDTH, HEIGHT = 800, 400
HERO_WIDTH, HERO_HEIGHT = 40, 40


# Загрузка изображений
Amelia_image = pygame.image.load('Amelia.png')
Amelia_image = pygame.transform.scale(Amelia_image, (HERO_WIDTH, HERO_HEIGHT))
Amelia_walk_gif = pygame.image.load('Amelia_walk.gif')
Amelia_walk_gif = pygame.transform.scale(Amelia_walk_gif, (HERO_WIDTH, HERO_WIDTH))

