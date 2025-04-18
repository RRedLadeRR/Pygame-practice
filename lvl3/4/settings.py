class Settings:
    """Клас для зберігання всіх налаштуваннь гри"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        # Параметри екрану
        self.screen_width = 1920
        self.screen_height = 1080
        self.dark_mode = True
        self.bg_color = (0, 0, 0) if self.dark_mode else (128, 0, 0)

        # Параметри корабля
        self.ship_limit = 3

        # Параметри снаряду
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0) if self.dark_mode else (0, 0, 0)
        self.bullets_alowed = 128

        # Параметри прибульців
        self.fleet_drop_speed = 10 # 1

        # Параметри зірок
        self.star_limit = 100
        self.star_speed = 0.09
        self.star_start_color = 200
        self.star_color_limit = 256
        self.star_color_step = 0.15
        self.star_radius = 3 

        # Темп пришвидшення гри
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Ініціалізує налаштування, що змінюються під час гри"""
        # Стандартні значення (середній рівень)
        self.ship_speed_factor = 2.0
        self.bullet_speed_factor = 2.0
        self.alien_speed_factor = 1.0
        self.ship_limit = 3
        
        # Інші налаштування
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Збільшує налаштування швидкості"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
