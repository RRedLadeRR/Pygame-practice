import pygame as pg


W = 60
H = 65.8

class Ship:
    """Клас для управління кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та встановлює цого початкову позицію"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантаження корабля і отримання поверхні
        # self.image = pg.image.load("images/x-wing.png")
        self.image = pg.transform.scale(pg.image.load("images/x-wing.png"), (W, H))
        self.rect = self.image.get_rect()
        # Кожен новий корабель з'являеться у нижній частині екрану
        self.rect.midbottom = self.screen_rect.midbottom

        # Зберігання дробової координати центра корабля
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Флаг переміщення
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Малює корабель в поточній позиції"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """Оновлює позицію корабля з урахуванням флагу"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Оновлюємо rect.x та rect.y на основі змінених значень
        # Оновлення атрибуту rect значення self.x
        self.rect.x = self.x
        self.rect.y = self.y
