import sys
import pygame

W = 64
H = 64

pygame.init()

# Налаштування екрану
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Зірки")

# Завантаження зірки
star = pygame.transform.scale(pygame.image.load("Pygame-practice/images/death-star.png"), (W, H))

# Малювання сітки
for x in range(0, 800, 100):
    for y in range(0, 600, 100):
        screen.blit(star, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
