import pygame as pg
import sys
from constantes import *
from player import Player
from plataforma import Platform
from enemigo import *
from button import *
from auxiliar import *
from box import *

pygame.init()

# Superficie principal
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
clock = pygame.time.Clock()

# Imagenes
imagen_fondo_menu = pygame.image.load("images\caracters\extras\Menu.jpg")
imagen_fondo_menu = pygame.transform.scale(imagen_fondo_menu,(ANCHO_VENTANA,ALTO_VENTANA)) # Escalamos la imagen de fondo a la dimension de la ventana

imagen_fondo = pygame.image.load("images/locations/forest/Santuario_Abel.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA)) # Escalamos la imagen de fondo a la dimension de la ventana

imagen_fondo_pause = pygame.image.load("images\caracters\extras\pause5.png")
imagen_fondo_pause = pygame.transform.scale(imagen_fondo_pause,(ANCHO_VENTANA,ALTO_VENTANA))

imagen_fondo_game_over = pygame.image.load("images\caracters\extras\game_over.png")
imagen_fondo_game_over = pygame.transform.scale(imagen_fondo_game_over,(ANCHO_VENTANA,ALTO_VENTANA))

# Musica
intro_music = pg.mixer.Sound("sound\Saint Seiya - Intro.mp3")
pause_music = pg.mixer.Sound("sound\Saint Seiya - Pause.mp3")
gameplay_music = pg.mixer.Sound("sound\Saint Seiya - Gameplay.mp3")


# define fonts
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

font = pygame.font.SysFont("Bauhaus 93",40)
font_menu = pygame.font.SysFont("ITC Machine",50)

# Buttons
    #Intro
start_button = Button(300,360,start_img)
settings_button = Button(300,480,settings_img)
exit_button = Button(300,600,exit_img)
    #Pause
resume_button_pause = Button(Auxiliar.center_image(resume_img)-30,300,resume_img)
settings_button_pause = Button(Auxiliar.center_image(settings_pause_img)-30,450,settings_pause_img)
quit_button_pause = Button(Auxiliar.center_image(quit_img)-30,600,quit_img)
    #Game Over
menu_button_game_over = Button(300,480,menu_img)
quit_button_game_over = Button(300,600,quit_img)


def gameplay():
    gameplay_music.play(-1)
    is_pause = False

    # control tiempo
    tiempo = 0
    tiempo_mil = 0

    # Bullet
    bullet_group = pygame.sprite.Group()

    # Creacion personajes

    player_1 = Player(
        x=0,
        y=530,
        speed_walk=5,
        speed_run=10,
        gravity=GRAVITY,
        jump_power=25,
        max_high_jump = 450,      
        animation_speed=12
        )
    
    super_player_1 = Player(
        x=0,
        y=530,
        speed_walk=5,
        speed_run=10,
        gravity=GRAVITY,
        jump_power=25,
        max_high_jump = 450,      
        animation_speed=12
        )
    
    enemy_list = []
    enemy_list.append(Enemy(
                            x=720,
                            y=110,
                            speed_walk= 2,
                            speed_run=8,
                            gravity=GRAVITY,
                            jump_power=25,
                            max_high_jump = 450,      
                            animation_speed=12
                            ))
    enemy_list.append(Enemy(
                            x=220,
                            y=110,
                            speed_walk= 2,
                            speed_run=8,
                            gravity=GRAVITY,
                            jump_power=25,
                            max_high_jump = 450,      
                            animation_speed=12
                            ))
    
    enemy_list.append(Enemy(
                            x=1220,
                            y=110,
                            speed_walk= 2,
                            speed_run=8,
                            gravity=GRAVITY,
                            jump_power=25,
                            max_high_jump = 450,      
                            animation_speed=12
                            ))
    box_list = []
    box_list.append(Box(130,300))

    box = Box(130,300)
    

    tiempo = Auxiliar()

    platform_list = []
    platform_list.append(Platform(00,450,60,60))
    platform_list.append(Platform(60,450,60,60))
    platform_list.append(Platform(120,450,60,60))
    platform_list.append(Platform(180,450,60,60))
    platform_list.append(Platform(240,450,60,60))

    platform_list.append(Platform(1200,450,60,60))
    platform_list.append(Platform(1260,450,60,60))
    platform_list.append(Platform(1320,450,60,60))
    platform_list.append(Platform(1380,450,60,60))
    platform_list.append(Platform(1440,450,60,60))
    #Platform()

    platform_list.append(Platform(600,250,60,60))
    platform_list.append(Platform(660,250,60,60))
    platform_list.append(Platform(720,250,60,60))
    platform_list.append(Platform(780,250,60,60))
    platform_list.append(Platform(840,250,60,60))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not player_1.is_hit:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and (player_1.is_on_platform or (player_1.double_jump and not player_1.doing_double_jump)):
                        player_1.jump_control(True,animation_speed=8) 
                    if event.key == pygame.K_p:
                        is_pause = True
                        main_pause(is_pause)
                        gameplay_music.play(-1)
                    if event.key == pygame.K_s and player_1.have_box:
                        player_1 = super_player_1.super_pegasus(player_1,delta_ms) 
                        player_1.have_box = False
                        for box in box_list:
                            box_list.remove(box)

                        #if not player_1.is_super_pegasus:
                        

                    # if event.key == pygame.K_LALT:
                    #     player_1.is_running = True 
                    #     player_1.walk_control(player_1.direccion,animation_speed=6,is_running=True)   

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        player_1.jump_control(False,animation_speed=8)
                    # if event.key == pygame.K_LALT:
                    #     player_1.is_running = False 


        keys = pygame.key.get_pressed()
        if not player_1.is_hit and not player_1.is_dead and not player_1.animation_mode:
            if(keys[pygame.K_LCTRL]):
                player_1.punch(animation_speed=2)
                if player_1.is_super_pegasus:
                    player_1.shoot_bullet()
                player_1.is_punching = True
            else:
                player_1.is_punching = False
                if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LALT]):
                    player_1.walk_control(DIRECCION_L,animation_speed=6,is_running=False)
                
                elif(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and keys[pygame.K_LALT]):
                    player_1.walk_control(DIRECCION_L,animation_speed=6,is_running=True)

                elif(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_LALT]):
                    player_1.walk_control(DIRECCION_R,animation_speed=6,is_running=False)

                elif(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and keys[pygame.K_LALT]):
                    player_1.walk_control(DIRECCION_R,animation_speed=6,is_running=True)

                elif(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
                    player_1.stay_control(animation_speed=12)

                elif(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
                    player_1.stay_control(animation_speed=12)
        else:
            if player_1.is_dead:
                player_1.dead_animation(delta_ms)
            elif player_1.is_hit:
                player_1.hit_animation(delta_ms,False)

        screen.blit(imagen_fondo,imagen_fondo.get_rect()) #fundimos la imagen de fondo

        for plataforma in platform_list:
            plataforma.draw(screen)

        delta_ms = clock.tick(FPS)  #limitando que vaya a una velocidad determinada

        for box in box_list:
            box.update(platform_list)
            box.draw(screen)

        for enemy in enemy_list:
            enemy.animation_enemy(delta_ms)
            enemy.update(delta_ms,platform_list)
            enemy.draw(screen)

        player_1.update(delta_ms,platform_list)
        player_1.draw(screen)

        for box in box_list:
            if(player_1.rect_limit_colition.colliderect(box.rect) and not player_1.have_box):
                player_1.have_box = True
                box.show_box_in_screen()

        for enemy in enemy_list:
            if not player_1.animation_mode and not enemy.is_dead:
                for bullet in enemy.bullet_group.sprites():
                    if(bullet.rect.colliderect(player_1.rect_limit_colition)) or \
                        enemy.rect.colliderect(player_1.rect_limit_colition):

                        player_1.animation = player_1.hit_animation(delta_ms,True)
                        bullet.kill()

            for bullet in player_1.bullet_group.sprites():
                if(bullet.rect.colliderect(enemy.rect)):
                    score = enemy.hit_animation(delta_ms,bullet.direction)
                    enemy.move_x = 0
                    enemy.ready = False
                    bullet.kill()
                    if score:
                        player_1.score += 100

            if (player_1.is_punching):
                if(player_1.rect.colliderect(enemy.rect)) or enemy.is_hit:
                    score = enemy.hit_animation(delta_ms,player_1.direccion)
                    enemy.move_x = 0
                    enemy.ready = False
                    if score:
                        player_1.score += 100

            if (player_1.is_super_pegasus and not player_1.countdown_pegasus_mode):
                player_1.tiempo_transcurrido_pegasus_mode += delta_ms
                if player_1.tiempo_transcurrido_pegasus_mode > TIEMPO_PEGASUS_MODE:
                    player_1.countdown_pegasus_mode = True
                    player_1 = super_player_1.super_pegasus(player_1,delta_ms)
        
        
        # enemigos update
        # player dibujarlo
        # dibujar todo el nivel
        if player_1.game_over:
            main_game_over()
        
        time = tiempo.temporizador(int(delta_ms))
        draw_text(f"Health: {player_1.lives}", font, NEGRO, ANCHO_VENTANA/25,12)
        draw_text(f"Time: {time}", font, NEGRO, ANCHO_VENTANA/2.3,12)
        draw_text(f"Score: {player_1.score}", font, NEGRO, ANCHO_VENTANA/1.2,12)

        draw_text(f"Health: {player_1.lives}", font, ROJO, ANCHO_VENTANA/25 +3,15)
        draw_text(f"Time: {time}", font, ROJO, ANCHO_VENTANA/2.3 +3,15)
        draw_text(f"Score: {player_1.score}", font, ROJO, ANCHO_VENTANA/1.2 +3,15)

        pygame.display.flip()
        
        tiempo_mil += delta_ms
        tiempo_int = int(tiempo_mil/1000)

        #print(f'clock: {tiempo_int}')

def main_menu():
    pygame.display.set_caption("Menu")
    clicked = False
    intro_music.play(-1)

    while True:
        screen.blit(imagen_fondo_menu,imagen_fondo_menu.get_rect())
        mouse_pos = pygame.mouse.get_pos()

        start_button.draw(screen,mouse_pos)
        settings_button.draw(screen,mouse_pos)
        exit_button.draw(screen,mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and clicked == False:
                if start_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    intro_music.stop()
                    gameplay()
                if settings_button.rect.collidepoint(mouse_pos):
                    print('click')
                    clicked = True
                if exit_button.rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False

        #menu_text = 
        pygame.display.update()

def main_pause(is_pause):
    pygame.display.set_caption("pause")
    clicked = False
    gameplay_music.stop()
    pause_music.play(-1)

    while is_pause:
        
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(imagen_fondo_pause,imagen_fondo_pause.get_rect())
        resume_button_pause.draw(screen,mouse_pos)
        settings_button_pause.draw(screen,mouse_pos)
        quit_button_pause.draw(screen,mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and clicked == False:
                if resume_button_pause.rect.collidepoint(mouse_pos):
                    clicked = True
                    pause_music.stop()
                    is_pause = False
                    #gameplay()
                if settings_button_pause.rect.collidepoint(mouse_pos):
                    print('click')
                    clicked = True
                if quit_button_pause.rect.collidepoint(mouse_pos):
                    pause_music.stop()
                    intro_music.play(-1)
                    main_menu()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False
        #menu_text = 
        pygame.display.flip()
        #pygame.display.update()

        
def main_game_over():
    pygame.display.set_caption("Game Over")
    clicked = False
    gameplay_music.stop()
    pause_music.play(-1)

    while True:
        
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(imagen_fondo_game_over,imagen_fondo_game_over.get_rect())

        menu_button_game_over.draw(screen,mouse_pos)
        quit_button_game_over.draw(screen,mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and clicked == False:
                if menu_button_game_over.rect.collidepoint(mouse_pos):
                    clicked = True
                    pause_music.stop()
                    main_menu()
                if quit_button_pause.rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False
        #menu_text = 
        pygame.display.flip()
        #pygame.display.update()

main_menu()






