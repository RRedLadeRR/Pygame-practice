import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Синє небо")

while True:
    screen.fill((135, 206, 250))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
