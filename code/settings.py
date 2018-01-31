class Settings():


    def __init__(self):

        self.screen_width = 800
        self.screen_height = 960
        self.bg_color = (200, 200, 200)
        self.ship_speed_factor = 2
        self.ship_limit = 1

        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 20
        self.fleet_direction = 1

        self.alien_points = 50