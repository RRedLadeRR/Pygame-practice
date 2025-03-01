import sys
import pygame as pg
from bullet import Bullet
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Клас для управління грою"""

    def __init__(self):
        """Ініціалізує гру та створює ресурси"""
        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Космічний бій")

        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()

    def _check_events(self):
        """Обробляє події клавіатури"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Обробка натискань клавіш"""
        if event.key == pg.K_UP:
            self.ship.moving_up = True
        elif event.key == pg.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pg.K_SPACE:
            self._fire_bullet()
        elif event.key == pg.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Обробка відпускання клавіш"""
        if event.key == pg.K_UP:
            self.ship.moving_up = False
        elif event.key == pg.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Створює новий снаряд і додає його до групи"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Оновлює позицію снарядів і видаляє старі"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Оновлює екран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pg.display.flip()

    def run_game(self):
        """Запускає основний цикл гри"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
