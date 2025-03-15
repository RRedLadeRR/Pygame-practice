import sys
import pygame as pg

W = 64
H = 64

pg.init()

# Налаштування екрану
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption("Краплі")

# Завантаження краплі
drop = pg.transform.scale(pg.image.load("Pygame-practice/images/Water-Drop.png"), (W, H))

# Створення сітки з краплями
drops = []
for x in range(0, 1280, 100):
    for y in range(0, 720, 100):
        drops.append(pg.Rect(x, y, 20, 20))

# Основний цикл гри
while True:
    screen.fill((255, 255, 255))

    for drop_rect in drops:
        drop_rect.y += 1
        screen.blit(drop, drop_rect)

    drops = [drop_rect for drop_rect in drops if drop_rect.y < 650]

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.flip()
