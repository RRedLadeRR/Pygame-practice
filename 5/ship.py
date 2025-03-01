import pygame as pg

W, H = 60, 65.8  # Розмір корабля

class Ship:
    """Клас для управління кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель біля лівого краю екрану"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантаження корабля
        self.image = pg.transform.scale(pg.image.load("images/x-wing.png"), (W, H))
        self.rect = self.image.get_rect()

        # Початкове розташування: лівий край екрана
        self.rect.midleft = self.screen_rect.midleft

        # Збереження позиції у вигляді float
        self.y = float(self.rect.y)

        # Прапори руху
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Оновлює позицію корабля"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Оновлення rect
        self.rect.y = self.y

    def blitme(self):
        """Малює корабель"""
        self.screen.blit(self.image, self.rect)
