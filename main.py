import pygame
import sys
from config import Config
from world import World


def initialize_game():
    """Инициализация игровых компонентов"""
    pygame.init()
    pygame.mixer.init()  # Для звуковых эффектов
    try:
        screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        pygame.display.set_caption("Глаза, которые видят слишком много")
        return screen
    except pygame.error as e:
        print(f"Ошибка инициализации экрана: {e}")
        sys.exit(1)


def main():
    # Инициализация игры
    screen = initialize_game()
    clock = pygame.time.Clock()

    try:
        # Создание игрового мира (без передачи game_state)
        world = World()  # Убрали аргумент game_state

        # Главный игровой цикл
        running = True
        while running:
            dt = clock.tick(60) / 1000  # Дельта времени в секундах

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and world.dialog_system.is_active:
                        world.dialog_system.next_line()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_e:  # Добавили обработку клавиши E
                        world.try_interact()  # Вызов метода взаимодействия

            world.update()
            screen.fill((0, 0, 0))
            world.render(screen)
            pygame.display.flip()

    except Exception as e:
        print(f"Критическая ошибка: {e}")
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()