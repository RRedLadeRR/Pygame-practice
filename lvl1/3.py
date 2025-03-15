import sys
import pygame

W = 60
H = 65.8

pygame.init()

# Налаштування екрану
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Ракета")

# Параметри ракети
rocket = pygame.transform.scale(pygame.image.load("Pygame-practice/images/x-wing.png"), (W, H))
rocket_rect = rocket.get_rect()
rocket_rect.center = screen.get_rect().center

# Швидкість руху
speed = 1

# Основний цикл
while True:
    screen.fill((0, 0, 0))
    screen.blit(rocket, rocket_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Рух ракети
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and rocket_rect.top > 0:
        rocket_rect.y -= speed
    if keys[pygame.K_DOWN] and rocket_rect.bottom < 720:
        rocket_rect.y += speed
    if keys[pygame.K_LEFT] and rocket_rect.left > 0:
        rocket_rect.x -= speed
    if keys[pygame.K_RIGHT] and rocket_rect.right < 1280:
        rocket_rect.x += speed

    pygame.display.flip()
