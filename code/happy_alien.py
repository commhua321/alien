import pygame
from pygame.sprite import Group
from settings import Settings
from alien import Alien
from ship import Ship
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard

import game_functions as gf



def run_game():

    #初始化Pygame
    pygame.init()
    #載入bgm
    pygame.mixer.music.load("sounds/bgm_maoudamashii_8bit24.ogg")
    pygame.mixer.music.set_volume(0.2)
    shoot_sound = pygame.mixer.Sound("sounds/tama1.wav")
    shoot_sound.set_volume(0.2)

    #載入遊戲設定值
    ai_settings = Settings()
    #設置窗口大小
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #設置窗口標題
    pygame.display.set_caption("Happy Alien")

    #設置開始按鈕
    play_button = Button(ai_settings, screen, "Press s to start")



    #創建遊戲需要的元素設定
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)


    #主要遊戲迴圈
    while True:
        #確認按鍵反應
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets,shoot_sound)

        #active game
        #
        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()



