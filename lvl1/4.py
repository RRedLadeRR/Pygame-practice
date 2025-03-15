import sys
import pygame

pygame.init()

# Налаштування екрану
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Клавіші")

# Основний цикл
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(f"Натиснута клавіша: {event.key}")

    pygame.display.flip()
