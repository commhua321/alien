import pygame
from pygame.sprite import Sprite
#精靈，會動的精靈
#繼承精靈類
class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        #初始化精靈
        super().__init__()

        #初始化ship位置
        self.screen = screen

        #載入ship的圖案並且獲得rect
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        #初始化ship到指定位置，設定rect屬性有center，centerx，centery以及screen屬性top
        #，bottom，left，right
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.centery = float(self.screen_rect.bottom - self.rect.width // 2)


        #按鍵關閉
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #按下按鍵後的更新以及框邊檢測
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor







    def blitme(self):
        #在指定位置繪製ship
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #重置時，欲將ship放置在中間下方
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = float(self.screen_rect.bottom - self.rect.width / 2)