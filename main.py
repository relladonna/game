import pygame
from sys import exit

pygame.init()

# объявляем ширину и высоту экрана
width = 800
height = 400

# создаём экран игры
screen = pygame.display.set_mode((width, height))

# устанавливаем количество кадров в секунду
fps = 60
# создаём объект таймера
clock = pygame.time.Clock()

# загружаем в переменную картинку из папки с нашим файлом
back = pygame.image.load('.jpg')

# даём название окну игры
pygame.display.set_caption("Detective Game")

# объявляем переменную-флаг для цикла игры
game = True

# запускаем бесконечный цикл
while game:
   # получаем список возможных действий игрока
   for event in pygame.event.get():
       # если пользователь нажал на крестик закрытия окна…
       if event.type == pygame.QUIT:
           # …останавливаем цикл
           pygame.quit()
           # добавляем корректное завершение работы
           exit()


   # размещаем новую поверхность на нашем экране — подготовленный jpeg
   screen.blit(back, (0, 0))

   # обновляем экран игры
   pygame.display.update()
   # добавляем к таймеру количество fps для частоты обновления основного цикла
   clock.tick(fps)
