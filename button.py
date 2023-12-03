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
level_1_img = pygame.image.load(r"images\Levels\01.png")
level_1_img = pygame.transform.scale(level_1_img,(50,50))

level_2_img = pygame.image.load(r"images\Levels\02.png")
level_2_img = pygame.transform.scale(level_2_img,(50,50))

level_3_img = pygame.image.load(r"images\Levels\03.png")
level_3_img = pygame.transform.scale(level_3_img,(50,50))

level_4_img = pygame.image.load(r"images\Levels\04.png")
level_4_img = pygame.transform.scale(level_4_img,(50,50))

level_5_img = pygame.image.load(r"images\Levels\05.png")
level_5_img = pygame.transform.scale(level_5_img,(50,50))

level_6_img = pygame.image.load(r"images\Levels\06.png")
level_6_img = pygame.transform.scale(level_6_img,(50,50))

level_7_img = pygame.image.load(r"images\Levels\07.png")
level_7_img = pygame.transform.scale(level_7_img,(50,50))

level_8_img = pygame.image.load(r"images\Levels\08.png")
level_8_img = pygame.transform.scale(level_8_img,(50,50))

level_9_img = pygame.image.load(r"images\Levels\09.png")
level_9_img = pygame.transform.scale(level_9_img,(50,50))

level_10_img = pygame.image.load(r"images\Levels\10.png")
level_10_img = pygame.transform.scale(level_10_img,(50,50))

level_11_img = pygame.image.load(r"images\Levels\11.png")
level_11img = pygame.transform.scale(level_11_img,(50,50))

level_12_img = pygame.image.load(r"images\Levels\12.png")
level_12_img = pygame.transform.scale(level_12_img,(50,50))

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

#Gold armo
gold_armo_size = 70
armo_location_x = 600
armo_location_y = 400

aries_armo_img = pygame.image.load(r"images\caracters\extras\1_aries_armo.png")
aries_armo_img = pygame.transform.scale(aries_armo_img,(gold_armo_size,gold_armo_size))
aries_rect = aries_armo_img.get_rect()
aries_rect.x = armo_location_x
aries_rect.y = armo_location_x

tauro_armo_img = pygame.image.load(r"images\caracters\extras\2_tauro_armo.png")
tauro_armo_img = pygame.transform.scale(tauro_armo_img,(gold_armo_size,gold_armo_size))

gemini_armo_img = pygame.image.load(r"images\caracters\extras\3_gemini_armo.png")
gemini_armo_img = pygame.transform.scale(gemini_armo_img,(gold_armo_size,gold_armo_size))

cancer_armo_img = pygame.image.load(r"images\caracters\extras\4_cancer_armo.png")
cancer_armo_img = pygame.transform.scale(cancer_armo_img,(gold_armo_size,gold_armo_size))

leo_armo_img = pygame.image.load(r"images\caracters\extras\5_leo_armo.png")
leo_armo_img = pygame.transform.scale(leo_armo_img,(gold_armo_size,gold_armo_size))

virgo_armo_img = pygame.image.load(r"images\caracters\extras\6_virgo_armo.png")
virgo_armo_img = pygame.transform.scale(virgo_armo_img,(gold_armo_size,gold_armo_size))

libra_armo_img = pygame.image.load(r"images\caracters\extras\7_libra_armo.png")
libra_armo_img = pygame.transform.scale(libra_armo_img,(gold_armo_size,gold_armo_size))

cancer_armo_img = pygame.image.load(r"images\caracters\extras\8_cancer_armo.png")
cancer_armo_img = pygame.transform.scale(cancer_armo_img,(gold_armo_size,gold_armo_size))

sagitario_armo_img = pygame.image.load(r"images\caracters\extras\9_sagitario_armo.png")
sagitario_armo_img = pygame.transform.scale(sagitario_armo_img,(gold_armo_size,gold_armo_size))

capricornio_armo_img = pygame.image.load(r"images\caracters\extras\10_capricornio_armo.png")
capricornio_armo_img = pygame.transform.scale(capricornio_armo_img,(gold_armo_size,gold_armo_size))

acuario_armo_img = pygame.image.load(r"images\caracters\extras\11_acuario_armo.png")
acuario_armo_img = pygame.transform.scale(acuario_armo_img,(gold_armo_size,gold_armo_size))

pisis_armo_img = pygame.image.load(r"images\caracters\extras\12_pisis_armo.png")
pisis_armo_img = pygame.transform.scale(pisis_armo_img,(gold_armo_size,gold_armo_size))

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
level_1_button = Button(860,610,level_1_img)
level_2_button = Button(1040,510,level_2_img)
level_3_button = Button(830,465,level_3_img)
level_4_button = Button(565,430,level_4_img)
level_5_button = Button(285,345,level_5_img)
level_6_button = Button(60,282,level_6_img)
level_7_button = Button(270,265,level_7_img)
level_8_button = Button(455,255,level_8_img)
level_9_button = Button(680,240,level_9_img)
level_10_button = Button(890,240,level_10_img)
level_11_button = Button(770,190,level_11_img)
level_12_button = Button(620,155,level_12_img)
    #Setting
up_button_setting_music = Button(750,300,up_img)
music_button_setting = Button(750,400,music_img)
down_button_setting_music = Button(750,500,down_img)

up_button_setting_sound = Button(1020,300,up_img)
sound_button_setting = Button(1020,400,sound_img)
down_button_setting_sound = Button(1020,500,down_img)

info_button_setting = Button(1250,500,info_img)
question_button_setting = Button(1250,300,question_img)

quit_button_setting = Button(300,480,quit_img_settings)

    #Tutorial
next_button = Button(1200,620,next_img)

armo_location_x = 1100
armo_location_y = 600
    #Gold armo
aries_button = Button(armo_location_x,armo_location_y,aries_armo_img)





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
