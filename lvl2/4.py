import sys
import pygame as pg
import random

W = 64
H = 64

pg.init()

# Налаштування екрану
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Дощ")

# Завантаження краплі
drop = pg.transform.scale(pg.image.load("Pygame-practice/images/Water-Drop.png"), (W, H))

# Створення крапель
drops = []
for _ in range(50): 
    x = random.randint(0, SCREEN_WIDTH - 20)
    y = random.randint(-720, 0)
    drops.append(pg.Rect(x, y, 20, 20))

# Швидкість крапель
DROP_SPEED = 3

# Основний цикл гри
while True:
    screen.fill((255, 255, 255))

    # Рух крапель вниз
    for drop_rect in drops:
        drop_rect.y += DROP_SPEED
        screen.blit(drop, drop_rect)

        # Якщо крапля доходить донизу — повертається на верхню межу екрану
        if drop_rect.y > SCREEN_HEIGHT:
            drop_rect.y = random.randint(-100, -20)  # Знову зверху
            drop_rect.x = random.randint(0, SCREEN_WIDTH - 20)

    # Обробка подій
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.flip()

