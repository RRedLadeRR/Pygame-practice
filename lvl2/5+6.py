import sys
import random
import pygame as pg
from time import sleep

W = 64
H = 64

W2 = 110
H2 = 57.8

pg.init()

# Налаштування екрану
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption("Кінець гри")

# Завантаження м'яча та персонажа
ball = pg.transform.scale(pg.image.load("Pygame-practice/images/ball.png"), (W, H))
player = pg.transform.scale(pg.image.load("Pygame-practice/images/Cristiano-Ronaldo.png"), (W2, H2))

# Позиції
ball_rect = ball.get_rect(topleft=(random.randint(0, 750), 0))
player_rect = player.get_rect(midbottom=(400, 590))

# Швидкість руху
ball_speed = 0.5
player_speed = 2

# Лічильник пропусків
misses = 0

# Основний цикл гри
while True:
    screen.fill((0, 128, 0))

    # Рух м'яча
    ball_rect.y += ball_speed
    if ball_rect.y > 720:
        ball_rect.y = 0
        ball_rect.x = random.randint(0, 750)
        misses += 1  # Підрахунок пропусків

    # Рух гравця
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pg.K_RIGHT] and player_rect.right < 1280:
        player_rect.x += player_speed

    # Перевірка на зіткнення
    if player_rect.colliderect(ball_rect):
        ball_rect.y = 0
        ball_rect.x = random.randint(0, 750)

    # Показ пропусків
    font = pg.font.SysFont(None, 48)
    score_text = font.render(f"Пропуски: {misses}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Завершення гри після 3 пропусків
    if misses >= 3:
        print("You Lose!")
        sleep(3)
        sys.exit()

    screen.blit(ball, ball_rect)
    screen.blit(player, player_rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.flip()
