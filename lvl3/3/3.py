import sys
import random
import pygame as pg
from time import sleep

pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Бічна стрілянина")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

SHIP_W, SHIP_H = 120, 130
TARGET_W, TARGET_H = 120, 120

player_ship = pg.transform.scale(pg.image.load("images/x-wing.png"), (SHIP_W, SHIP_H))
target_ship = pg.transform.scale(pg.image.load("images/tie-fighter.png"), (TARGET_W, TARGET_H))

player_rect = player_ship.get_rect(midleft=(0, SCREEN_HEIGHT // 2))
target_rect = target_ship.get_rect(midright=(SCREEN_WIDTH, SCREEN_HEIGHT // 2))

player_speed = 1
initial_target_speed = 1
target_speed = initial_target_speed
speed_increment = 0.2

moving_up, moving_down = False, False
bullets = []

misses = 0

font = pg.font.SysFont(None, 48)
play_button = font.render("Play", True, WHITE)
play_button_rect = play_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

game_active = False

# Основний цикл гри
while True:
    screen.fill(BLACK)

    if game_active:
        # Рух корабля
        if moving_up and player_rect.top > 0:
            player_rect.y -= player_speed
        if moving_down and player_rect.bottom < SCREEN_HEIGHT:
            player_rect.y += player_speed

        # Рух ворожого корабля
        target_rect.y += target_speed
        if target_rect.top <= 0 or target_rect.bottom >= SCREEN_HEIGHT:
            target_speed *= -1
            target_speed += speed_increment * (1 if target_speed > 0 else -1)  # Збільшення швидкості

        # Рух куль
        for bullet in bullets[:]:
            bullet.x += 10
            if bullet.left > SCREEN_WIDTH:
                bullets.remove(bullet)
                misses += 1

        # Перевірка зіткнення куль з кораблем-мішенню
        for bullet in bullets[:]:
            if bullet.colliderect(target_rect):
                bullets.remove(bullet)

        # Показ промахів
        score_text = font.render(f"Misses: {misses}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Завершення гри після 3 промахів
        if misses >= 3:
            game_active = False
            misses = 0
            sleep(1)

        # Відображення елементів
        for bullet in bullets:
            pg.draw.rect(screen, RED, bullet)
        screen.blit(player_ship, player_rect)
        screen.blit(target_ship, target_rect)

    else:
        # Показ кнопки Play
        screen.blit(play_button, play_button_rect)

    # Обробка подій
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                moving_up = True
            if event.key == pg.K_DOWN:
                moving_down = True
            if event.key == pg.K_SPACE and game_active:
                bullet_rect = pg.Rect(player_rect.right, player_rect.centery - 3, 10, 6)
                bullets.append(bullet_rect)
            if event.key == pg.K_ESCAPE:
                sys.exit()

        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                moving_up = False
            if event.key == pg.K_DOWN:
                moving_down = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos) and not game_active:
                game_active = True
                misses = 0
                bullets.clear()
                target_speed = initial_target_speed

    pg.display.flip()
