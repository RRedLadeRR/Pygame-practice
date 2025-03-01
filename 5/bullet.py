import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Клас для управління снарядами корабля"""

    def __init__(self, ai_game):
        """Створює снаряд у позиції корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Створюємо снаряд і розміщуємо біля корабля
        self.rect = pg.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright  # Зміщуємо його праворуч від корабля

        # Зберігаємо позицію як float
        self.x = float(self.rect.x)

    def update(self):
        """Переміщує снаряд вправо"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Малює снаряд на екрані"""
        pg.draw.rect(self.screen, self.color, self.rect)
