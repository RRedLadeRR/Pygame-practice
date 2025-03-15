import sys
import pygame

W = 60
H = 65.8

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Ігровий персонаж")

player = pygame.transform.scale(pygame.image.load("Pygame-practice/images/x-wing.png"), (W, H))
player_rect = player.get_rect()
player_rect.center = screen.get_rect().center

while True:
    screen.fill((255, 255, 255))
    screen.blit(player, player_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
