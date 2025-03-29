import pygame as pg


class Button:
    def __init__(self, ai_game, msg):
        """Ініціалізує атрибути кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Призначення розмірів та властивостей кнопки
        self.width, self.height = 200, 50
        self.button_color = (128, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)

        # Побудова об'єкта rect кнопки та вирівнюємо по центру екрана
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Текст кнопки створюється тільки один раз
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Перетворює msg в прямокутник і вирівнює текст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Відображає пусту кнопку та виводить текст"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class DifficultyButton(Button):
    """Кнопка для вибору рівня складності"""
    
    def __init__(self, ai_game, msg, difficulty):
        """Ініціалізує кнопку складності"""
        super().__init__(ai_game, msg)
        self.difficulty = difficulty
        self.msg = msg
        self.settings = ai_game.settings
        
        # Розміщуємо кнопки вертикально
        self.rect.y = self.screen_rect.centery + (self.height + 10) * (difficulty - 1)

        # Повний контроль над позицією тексту
        if difficulty == 1:
            self.msg_image_rect.top = self.rect.top + 5
        elif difficulty == 2:
            self.msg_image_rect.centery = self.rect.centery
        else:
            self.msg_image_rect.bottom = self.rect.bottom - 5
        
    def set_difficulty(self):
        """Встановлює рівень складності"""
        if self.difficulty == 1:  # Легкий
            self.settings.ship_speed_factor = 1.5
            self.settings.bullet_speed_factor = 1.5
            self.settings.alien_speed_factor = 0.5
            self.settings.ship_limit = 5
        elif self.difficulty == 2:  # Середній
            self.settings.ship_speed_factor = 2.0
            self.settings.bullet_speed_factor = 2.0
            self.settings.alien_speed_factor = 1.0
            self.settings.ship_limit = 3
        elif self.difficulty == 3:  # Важкий
            self.settings.ship_speed_factor = 2.5
            self.settings.bullet_speed_factor = 2.5
            self.settings.alien_speed_factor = 1.5
            self.settings.ship_limit = 1