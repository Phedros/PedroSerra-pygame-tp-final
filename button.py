import pygame
from auxiliar import *

class Button():
    def __init__(self,x,y,image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self,screen,pos_mouse):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos_mouse):
            pass

#images buttons
    # Intro
start_img = pygame.image.load("images\caracters\extras\start.png")
settings_img = pygame.image.load("images\caracters\extras\settings.png")
exit_img = pygame.image.load("images\caracters\extras\exit.png")
    #Pause
resume_img = pygame.image.load(r"images\caracters\extras\resume.png")
settings_pause_img = pygame.image.load("images\caracters\extras\settings_pause.png")
quit_img = pygame.image.load("images\caracters\extras\quit.png")
quit_img_settings = pygame.transform.scale(quit_img,(200,63))
    #Game Over
menu_img = pygame.image.load("images\caracters\extras\menu2.png")
    #Levels
level_one_img = pygame.image.load(r"images\Levels\01.png")
level_one_img = pygame.transform.scale(level_one_img,(50,50))

level_two_img = pygame.image.load(r"images\Levels\02.png")
level_two_img = pygame.transform.scale(level_two_img,(50,50))

setting_button_size = 80
    # Settings
music_img = pygame.image.load("images\caracters\extras\music_img.png")
music_img = pygame.transform.scale(music_img,(setting_button_size,setting_button_size))

up_img = pygame.image.load(r"images\caracters\extras\up_img.png")
up_img = pygame.transform.scale(up_img,(setting_button_size,setting_button_size))

down_img = pygame.image.load("images\caracters\extras\down_img.png")
down_img = pygame.transform.scale(down_img,(setting_button_size,setting_button_size))

sound_img = pygame.image.load("images\caracters\extras\sound_img.png")
sound_img = pygame.transform.scale(sound_img,(setting_button_size,setting_button_size))

info_img = pygame.image.load("images\caracters\extras\info_img.png")
info_img = pygame.transform.scale(info_img,(setting_button_size,setting_button_size))

question_img = pygame.image.load("images\caracters\extras\question_img.png")
question_img = pygame.transform.scale(question_img,(setting_button_size,setting_button_size))

next_img = pygame.image.load(r"images\caracters\extras\next_img.png")
next_img = pygame.transform.scale(next_img,(setting_button_size,setting_button_size))

#--------------------------------------------------------------------------------------------

# Buttons
    #Intro
start_button = Button(300,360,start_img)
settings_button = Button(300,480,settings_img)
exit_button = Button(300,600,exit_img)
    #Pause
resume_button_pause = Button(Auxiliar.center_image(resume_img)-30,400,resume_img)
settings_button_pause = Button(Auxiliar.center_image(settings_pause_img)-30,500,settings_pause_img)
quit_button_pause = Button(Auxiliar.center_image(quit_img)-30,600,quit_img)
    #Game Over
menu_button_game_over = Button(300,480,menu_img)
quit_button_game_over = Button(300,600,quit_img)
    #Levels
level_one_button = Button(860,610,level_one_img)
level_two_button = Button(900,570,level_two_img)
    #Setting
up_button_setting_music = Button(750,300,up_img)
music_button_setting = Button(750,400,music_img)
down_button_setting_music = Button(750,500,down_img)

up_button_setting_sound = Button(1020,300,up_img)
sound_button_setting = Button(1020,400,sound_img)
down_button_setting_sound = Button(1020,500,down_img)

info_button_setting = Button(1250,500,info_img)
question_button_setting = Button(1250,300,question_img)

quit_button_game_over = Button(300,480,quit_img_settings)

    #Tutorial
next_button = Button(1200,620,next_img)





    #                                                   1,1,1,1,1,1,1,1,1,1,1,1,1,1
    #       1,1,2,2,2,3,3,4,4,4,5,5,6,6,6,7,7,8,8,8,9,9,0,0,0,1,1,2,2,2,3,3,4,4,4,5 
    #   4,8,2,6,0,4,8,2,6,0,4,8,2,6,0,4,8,2,6,0,4,8,2,6,0,4,8,2,6,0,4,8,2,6,0,4,8,2
    # 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  40
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  80
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  120
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  160
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  200
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  240
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  280
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  320
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  360
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  400
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  440
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  480
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  520
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  560
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  600
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  640
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  680
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  720
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  760
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]   800
