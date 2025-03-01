import sys
import pygame as pg

class EmptyScreen:
    """Клас для створення порожнього екрану та обробки подій"""

    def __init__(self):
        """Ініціалізує гру та створює ігрові ресурси"""
        pg.init()

        self.screen = pg.display.set_mode((1280, 720))
        pg.display.set_caption("Empty Screen")

        self.bg_color = ("lightblue")

    def _check_events(self):
        """Обробляє події клавіатури та миші"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                print(f"Натиснута клавіша: {event.key}")

    def _update_screen(self):
        """Заповнює екран фоновим кольором і оновлює відображення"""
        self.screen.fill(self.bg_color)
        pg.display.flip()

    def run_game(self):
        """Запускає основний цикл гри"""
        while True:
            self._check_events()
            self._update_screen()

if __name__ == '__main__':
    game = EmptyScreen()
    game.run_game()
