class Settings:
    """Клас для збереження налаштувань гри"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (135, 206, 250)  # Світло-блакитний фон

        # Налаштування корабля
        self.ship_speed = 0.5

        # Налаштування снаряда
        self.bullet_speed = 0.25  # Тепер снаряди летять швидше
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 30