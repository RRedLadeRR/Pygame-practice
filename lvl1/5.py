import sys
import pygame

W = 60
H = 65.8

pygame.init()

# Налаштування екрану
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Бічна стрілянина")

# Параметри корабля
ship = pygame.transform.scale(pygame.image.load("images/x-wing.png"), (W, H))
ship_rect = ship.get_rect()
ship_rect.midleft = screen.get_rect().midleft

# Список куль
bullets = []

# Прапори руху
moving_up = False
moving_down = False

# Основний цикл гри
while True:
    screen.fill((0, 0, 0))
    screen.blit(ship, ship_rect)

    # Рух куль
    for bullet in bullets[:]:
        bullet.x += 1
        if bullet.left > 1280:
            bullets.remove(bullet)

    # Малювання куль
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 0, 0), bullet)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
            if event.key == pygame.K_SPACE:
                bullet_rect = pygame.Rect(ship_rect.right, ship_rect.centery - 3, 10, 6)
                bullets.append(bullet_rect)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False

    # Рух корабля
    if moving_up and ship_rect.top > 0:
        ship_rect.y -= 1
    if moving_down and ship_rect.bottom < 720:
        ship_rect.y += 1

    pygame.display.flip()
