import pygame
import sys
from config import Config
from world import World

def main():
    pygame.init()
    try:
        screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        pygame.display.set_caption("Глаза, которые видят слишком много")
    except pygame.error as e:
        print(f"Ошибка инициализации: {e}")
        sys.exit(1)
    
    world = World()
    clock = pygame.time.Clock()
    
    running = True
    while running:
        dt = clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_e:
                    world.handle_interactions()
                elif event.key == pygame.K_SPACE and world.dialog_system.is_active:
                    world.dialog_system.next_line()
        
        world.update()
        screen.fill(Config.BG_COLOR)
        world.render(screen)
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()