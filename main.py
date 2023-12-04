import pygame as pg
import sys
from constantes import *
from player import Player
from plataforma import Platform
from enemigo import *
from button import *
from auxiliar import *
from box import *
from world_data import *
from gold import *
from score import *

pygame.init()

# Superficie principal
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
clock = pygame.time.Clock()

# Nivel actual
actual_level = 1
max_level = 1

# Imagenes
imagen_fondo_menu = pygame.image.load("images\caracters\extras\Menu.jpg")
imagen_fondo_menu = pygame.transform.scale(imagen_fondo_menu,(ANCHO_VENTANA,ALTO_VENTANA)) # Escalamos la imagen de fondo a la dimension de la ventana

imagen_fondo = pygame.image.load("images/locations/forest/Santuario_Abel.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA)) # Escalamos la imagen de fondo a la dimension de la ventana

imagen_fondo_levels = pygame.image.load("images\caracters\extras\levels_img.jpg")
imagen_fondo_levels = pygame.transform.scale(imagen_fondo_levels,(ANCHO_VENTANA,ALTO_VENTANA))

imagen_fondo_pause = pygame.image.load("images\caracters\extras\pause5.png")
imagen_fondo_pause = pygame.transform.scale(imagen_fondo_pause,(ANCHO_VENTANA,ALTO_VENTANA))

imagen_fondo_game_over = pygame.image.load("images\caracters\extras\game_over.png")
imagen_fondo_game_over = pygame.transform.scale(imagen_fondo_game_over,(ANCHO_VENTANA,ALTO_VENTANA))

imagen_fondo_score = pygame.image.load("images\caracters\extras\score_img.png")
imagen_fondo_score = pygame.transform.scale(imagen_fondo_score,(ANCHO_VENTANA,ALTO_VENTANA))

imagen_setting = pygame.image.load("images\caracters\extras\setting.jpg")
imagen_setting = pygame.transform.scale(imagen_setting,(ANCHO_VENTANA,ALTO_VENTANA))

imagen_tuto_1 = pygame.image.load(r"images\caracters\extras\tutorial_1.png")
imagen_tuto_1 = pygame.transform.scale(imagen_tuto_1,(ANCHO_VENTANA,ALTO_VENTANA))

imagen_tuto_2 = pygame.image.load(r"images\caracters\extras\tutorial_2.png")
imagen_tuto_2 = pygame.transform.scale(imagen_tuto_2,(ANCHO_VENTANA,ALTO_VENTANA))

imagen_tuto_3 = pygame.image.load(r"images\caracters\extras\tutorial_3.png")
imagen_tuto_3 = pygame.transform.scale(imagen_tuto_3,(ANCHO_VENTANA,ALTO_VENTANA))


# Musica
intro_music = pg.mixer.Sound("sound\Saint Seiya - Intro.mp3")
pause_music = pg.mixer.Sound("sound\Saint Seiya - Pause.mp3")
volumen = 0.5

#gameplay_music = pg.mixer.Sound("sound\Saint Seiya - Gameplay.mp3")
level_select_music = pg.mixer.Sound("sound\Saint Seiya - Level selec.mp3")


# define fonts
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

font = pygame.font.SysFont("Bauhaus 93",40)
font_setting = pygame.font.SysFont("Calisto MT",60)
font_menu = pygame.font.SysFont("ITC Machine",50)
font_game_over = pygame.font.SysFont("Viner Hand ITC",100)



def insert_name():
    clicked = False
    player_name = ""

    while True:

        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)
        pygame.display.set_caption('Ingrese el nombre del jugador')

        menu_button_game_over.draw(screen,mouse_pos)
        quit_button_game_over.draw(screen,mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Aquí puedes manejar la lógica cuando se presiona Enter
                    main_selec_levels(new_total_score=0,new_level=1,name=player_name,lives=TOTAL_LIVES)
                elif event.key == pygame.K_BACKSPACE:
                    # Eliminar el último carácter
                    player_name = player_name[:-1]
                else:
                    # Agregar caracteres a la variable del nombre del jugador
                    player_name += event.unicode


            # Limpiar la pantalla
        screen.fill(BLANCO)
        screen.blit(imagen_fondo_menu,imagen_fondo_menu.get_rect())
        # texto
        draw_text("Ingrese su nombre",font_setting,NEGRO,210,400)
        # Dibujar el cuadro de entrada de texto
        pygame.draw.rect(screen, BLANCO, (240, 480, 300, 60))
        pygame.draw.rect(screen, NEGRO, (240, 480, 300, 60), 2)

        # Renderizar el texto del nombre del jugador
        texto = font_menu.render(player_name, True, NEGRO)
        screen.blit(texto, (260, 495))

        pygame.display.flip()

def gameplay(level,score,name,lives):
    player_name = name
    total_score = score
    pg.mixer.music.load("sound\Saint Seiya - Gameplay.mp3")
    pg.mixer.music.play(-1)
    #gameplay_music.play(loops=-1)
    is_pause = False
    ready_to_pass = False
    gold_enter_flag = True

    actual_level = level

    # control tiempo
    tiempo = 0
    tiempo_mil = 0

    # Bullet
    bullet_group = pygame.sprite.Group()

    json_file = Auxiliar.read_json("json.json")

    # Creacion personajes
    dict_player = World.load_level(actual_level,json_file,'player')
    player_1 = Player(
        x=dict_player["x"],
        y=dict_player["y"],
        speed_walk=dict_player["speed_walk"],
        speed_run=dict_player["speed_run"],
        gravity=dict_player["gravity"],
        jump_power=dict_player["jump_power"],
        max_high_jump = dict_player["max_high_jump"],
        animation_speed=dict_player["animation_speed"]
        )
    player_1.score = total_score
    player_1.lives = lives

    dict_super_player = World.load_level(actual_level,json_file,'super_player')
    super_player_1 = Player(
                            x=dict_super_player["x"],
                            y=dict_super_player["y"],
                            speed_walk=dict_super_player["speed_walk"],
                            speed_run=dict_super_player["speed_run"],
                            gravity=dict_super_player["gravity"],
                            jump_power=dict_super_player["jump_power"],
                            max_high_jump = dict_super_player["max_high_jump"],
                            animation_speed=dict_super_player["animation_speed"]
                            )

    load_enemy_list = World.load_level(actual_level,json_file,'enemy_list')
    enemy_list = []
    for enemy in load_enemy_list:
        enemy_list.append(Enemy(
                                x=enemy['x'],
                                y=enemy['y'],
                                speed_walk= enemy['speed_walk'],
                                speed_run=enemy['speed_run'],
                                gravity=enemy['gravity'],
                                jump_power=enemy['jump_power'],
                                max_high_jump = enemy['max_high_jump'],
                                animation_speed=enemy['animation_speed']
                                )
                            )

    box_load = World.load_level(actual_level,json_file,'box')
    box = Box(pos_x=box_load['x'],pos_y=box_load['y'])

    box_list = []
    box_list.append(box)


    gold_list = []



    tiempo = Auxiliar()

    platform_to_load = World.load_level(actual_level,json_file,'platforms')

    world = World(platform_to_load)
    platform_list = world.tile_list

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not player_1.is_hit:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s and player_1.have_box:
                        player_1 = super_player_1.super_pegasus(player_1,delta_ms)
                        player_1.have_box = False
                        for box in box_list:
                            box_list.remove(box)
                    if event.key == pygame.K_SPACE and (player_1.is_on_platform or (player_1.double_jump and not player_1.doing_double_jump)):
                        player_1.jump_control(True,animation_speed=8)
                    if event.key == pygame.K_p:
                        is_pause = True
                        new_time = main_pause(is_pause,time)
                        time = new_time
                        pg.mixer.music.load("sound\Saint Seiya - Gameplay.mp3")
                        pg.mixer.music.play(-1)

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

        # for plataforma in platform_list:
        #     plataforma.draw(screen)

        for block in world.tile_list:
            block.draw(screen)

        delta_ms = clock.tick(FPS)  #limitando que vaya a una velocidad determinada

        for box in box_list:
            box.update(platform_list)
            box.draw(screen)

        for enemy in enemy_list:
            if enemy.destroy:
                enemy_list.remove(enemy)
            enemy.animation_enemy(delta_ms)
            enemy.update(delta_ms,platform_list)
            enemy.draw(screen)


        player_1.update(delta_ms,platform_list)
        player_1.draw(screen)

        if ready_to_pass:
            for gold in gold_list:
                gold.update(platform_list)
                gold.draw(screen)



        for box in box_list:
            if(player_1.rect_limit_colition.colliderect(box.rect) and not player_1.have_box):
                player_1.score += 300
                player_1.have_box = True
                box.show_box_in_screen()

        for gold in gold_list:
            if player_1.rect_limit_colition.colliderect(gold.rect):
                player_1.score += 500
                gold_list.remove(gold)
                actual_level += 1
                if actual_level == 13:
                    main_game_over(player_name,player_1.score,player_1.lives)
                main_selec_levels(player_1.score,actual_level, player_name, player_1.lives)

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

        if len(enemy_list) == 0  and gold_enter_flag:
                gold_enter_flag = False
                gold_list.append(Gold(actual_level))
                ready_to_pass = True
                

        
        time = tiempo.temporizador(int(delta_ms))
        draw_text(f"Health: {player_1.lives}", font, NEGRO, ANCHO_VENTANA/25,12)
        draw_text(f"Time: {time}", font, NEGRO, ANCHO_VENTANA/2.3,12)
        draw_text(f"Score: {player_1.score}", font, NEGRO, ANCHO_VENTANA/1.2,12)

        draw_text(f"Health: {player_1.lives}", font, ROJO, ANCHO_VENTANA/25 +3,15)
        draw_text(f"Time: {time}", font, ROJO, ANCHO_VENTANA/2.3 +3,15)
        draw_text(f"Score: {player_1.score}", font, ROJO, ANCHO_VENTANA/1.2 +3,15)

        if player_1.game_over or time <= 0:
            main_game_over(player_name,total_score,player_1.lives)

        if DEBUG:
            World.draw_grid(screen, tile_size)

        #print(f'$$$$$$$$$$$$$$4 {world.tile_list}')



        pygame.display.flip()

        tiempo_mil += delta_ms
        tiempo_int = int(tiempo_mil/1000)

        #print(f'clock: {tiempo_int}')

def main_selec_levels(new_total_score, new_level, name,lives):
    player_name = name
    total_score = new_total_score
    actual_level = new_level
    total_lives = lives
    pg.mixer.music.load("sound\Saint Seiya - Level selec.mp3")
    pg.mixer.music.play(-1)

    pygame.display.set_caption("Selec Level")


    while True:
        screen.blit(imagen_fondo_levels,imagen_fondo_levels.get_rect())
        mouse_pos = pygame.mouse.get_pos()
        #print(mouse_pos)
        clicked = False

        match actual_level:
            case 1:
                level_1_button.draw(screen,mouse_pos)
            case 2:
                level_1_button.draw(screen,mouse_pos)
                level_2_button.draw(screen,mouse_pos)
            case 3:
                level_1_button.draw(screen,mouse_pos)
                level_2_button.draw(screen,mouse_pos)
                level_3_button.draw(screen,mouse_pos)
            case 4:
                level_1_button.draw(screen,mouse_pos)
                level_2_button.draw(screen,mouse_pos)
                level_3_button.draw(screen,mouse_pos)
                level_4_button.draw(screen,mouse_pos)
            case 5:
                level_1_button.draw(screen,mouse_pos)
                level_2_button.draw(screen,mouse_pos)
                level_3_button.draw(screen,mouse_pos)
                level_4_button.draw(screen,mouse_pos)
                level_5_button.draw(screen,mouse_pos)
            case 6:
                level_1_button.draw(screen,mouse_pos)
                level_2_button.draw(screen,mouse_pos)
                level_3_button.draw(screen,mouse_pos)
                level_4_button.draw(screen,mouse_pos)
                level_5_button.draw(screen,mouse_pos)
                level_6_button.draw(screen,mouse_pos)
            case 7:
                level_1_button.draw(screen,mouse_pos)
                level_2_button.draw(screen,mouse_pos)
                level_3_button.draw(screen,mouse_pos)
                level_4_button.draw(screen,mouse_pos)
                level_5_button.draw(screen,mouse_pos)
                level_6_button.draw(screen,mouse_pos)
                level_7_button.draw(screen,mouse_pos)
            case 8:
                level_1_button.draw(screen,mouse_pos)
                level_2_button.draw(screen,mouse_pos)
                level_3_button.draw(screen,mouse_pos)
                level_4_button.draw(screen,mouse_pos)
                level_5_button.draw(screen,mouse_pos)
                level_6_button.draw(screen,mouse_pos)
                level_7_button.draw(screen,mouse_pos)
                level_8_button.draw(screen,mouse_pos)
            case 9:
                level_1_button.draw(screen,mouse_pos)
                level_2_button.draw(screen,mouse_pos)
                level_3_button.draw(screen,mouse_pos)
                level_4_button.draw(screen,mouse_pos)
                level_5_button.draw(screen,mouse_pos)
                level_6_button.draw(screen,mouse_pos)
                level_7_button.draw(screen,mouse_pos)
                level_8_button.draw(screen,mouse_pos)
                level_9_button.draw(screen,mouse_pos)
            case 10:
                level_1_button.draw(screen,mouse_pos)
                level_2_button.draw(screen,mouse_pos)
                level_3_button.draw(screen,mouse_pos)
                level_4_button.draw(screen,mouse_pos)
                level_5_button.draw(screen,mouse_pos)
                level_6_button.draw(screen,mouse_pos)
                level_7_button.draw(screen,mouse_pos)
                level_8_button.draw(screen,mouse_pos)
                level_9_button.draw(screen,mouse_pos)
                level_10_button.draw(screen,mouse_pos)
            case 11:
                level_1_button.draw(screen,mouse_pos)
                level_2_button.draw(screen,mouse_pos)
                level_3_button.draw(screen,mouse_pos)
                level_4_button.draw(screen,mouse_pos)
                level_5_button.draw(screen,mouse_pos)
                level_6_button.draw(screen,mouse_pos)
                level_7_button.draw(screen,mouse_pos)
                level_8_button.draw(screen,mouse_pos)
                level_9_button.draw(screen,mouse_pos)
                level_10_button.draw(screen,mouse_pos)
                level_11_button.draw(screen,mouse_pos)
            case 12:
                level_1_button.draw(screen,mouse_pos)
                level_2_button.draw(screen,mouse_pos)
                level_3_button.draw(screen,mouse_pos)
                level_4_button.draw(screen,mouse_pos)
                level_5_button.draw(screen,mouse_pos)
                level_6_button.draw(screen,mouse_pos)
                level_7_button.draw(screen,mouse_pos)
                level_8_button.draw(screen,mouse_pos)
                level_9_button.draw(screen,mouse_pos)
                level_10_button.draw(screen,mouse_pos)
                level_11_button.draw(screen,mouse_pos)
                level_12_button.draw(screen,mouse_pos)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and clicked == False:
                if level_1_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)
                elif level_2_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)
                elif level_3_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)
                elif level_4_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)
                elif level_5_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)
                elif level_6_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)
                elif level_7_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)
                elif level_8_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)
                elif level_9_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)
                elif level_10_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)
                elif level_11_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)
                elif level_12_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    gameplay(actual_level,total_score, player_name, total_lives)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False

        #menu_text =
        pygame.display.update()

def tutorial():
    pygame.display.set_caption("Tutorial")
    clicked = False
    counter = 0

    while True:
        mouse_pos = pygame.mouse.get_pos()
        match counter:
            case 0:
                screen.blit(imagen_tuto_1,imagen_tuto_1.get_rect())
            case 1:
                screen.blit(imagen_tuto_2,imagen_tuto_2.get_rect())
            case 2:
                screen.blit(imagen_tuto_3,imagen_tuto_3.get_rect())
            case _:
                pass


        next_button.draw(screen,mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and clicked == False:
                if next_button.rect.collidepoint(mouse_pos):
                    counter += 1
                    if counter >= 3:
                        counter = 0
                        main_setting()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False

        pygame.display.update()

def main_setting():
    #imagen_setting
    pygame.display.set_caption("Setting")

    while True:
        screen.blit(imagen_setting,imagen_setting.get_rect())
        mouse_pos = pygame.mouse.get_pos()
        clicked = False

        draw_text("Music",font_setting,NEGRO,730,230)
        draw_text("Music",font_setting,ROJO_SEIYA,728,228)
        draw_text("Sound",font_setting,NEGRO,990,180)
        draw_text("Sound",font_setting,ROJO_SEIYA,988,178)
        draw_text("Effects",font_setting,NEGRO,980,230)
        draw_text("Effects",font_setting,ROJO_SEIYA,978,228)
        draw_text("Tutorial",font_setting,NEGRO,1210,230)
        draw_text("Tutorial",font_setting,ROJO_SEIYA,1208,228)
        draw_text("Score",font_setting,NEGRO,1230,430)
        draw_text("Score",font_setting,ROJO_SEIYA,1228,428)



        music_button_setting.draw(screen,mouse_pos)
        up_button_setting_music.draw(screen,mouse_pos)
        down_button_setting_music.draw(screen,mouse_pos)
        up_button_setting_sound.draw(screen,mouse_pos)
        down_button_setting_sound.draw(screen,mouse_pos)
        sound_button_setting.draw(screen,mouse_pos)
        info_button_setting.draw(screen,mouse_pos)
        question_button_setting.draw(screen,mouse_pos)
        quit_button_setting.draw(screen,mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and clicked == False:
                if quit_button_setting.rect.collidepoint(mouse_pos):
                    clicked = True
                    main_menu()
                elif up_button_setting_music.rect.collidepoint(mouse_pos):
                    clicked = True
                    volumen = pygame.mixer.music.get_volume()
                    volumen += 0.1
                    if volumen > 1.0:
                        volumen = 1.0
                    pygame.mixer.music.set_volume(volumen)
                elif down_button_setting_music.rect.collidepoint(mouse_pos):
                    clicked = True
                    volumen = pygame.mixer.music.get_volume()
                    print(volumen)
                    volumen -= 0.1
                    print(volumen)
                    if volumen < 0.0:
                        volumen = 0.0
                    pygame.mixer.music.set_volume(volumen)
                elif up_button_setting_sound.rect.collidepoint(mouse_pos):
                    clicked = True
                    main_menu()
                elif down_button_setting_sound.rect.collidepoint(mouse_pos):
                    clicked = True
                    main_menu()
                elif info_button_setting.rect.collidepoint(mouse_pos):
                    clicked = True
                    main_score()
                elif question_button_setting.rect.collidepoint(mouse_pos):
                    clicked = True
                    tutorial()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False

        #menu_text =
        pygame.display.update()

def main_menu():
    total_score = 0
    pygame.display.set_caption("Menu")
    clicked = False
    pg.mixer.music.load("sound\Saint Seiya - Intro.mp3")
    pg.mixer.music.play(-1)

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
                    insert_name()
                    #main_score()
                if settings_button.rect.collidepoint(mouse_pos):
                    clicked = True
                    main_setting()
                if exit_button.rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False

        #menu_text =
        pygame.display.update()

def main_pause(is_pause,time_input):
    actual_time = time_input
    pygame.display.set_caption("pause")
    clicked = False
    pg.mixer.music.load("sound\Saint Seiya - Pause.mp3")
    pg.mixer.music.play(-1)

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
                    return actual_time
                    #gameplay()
                if settings_button_pause.rect.collidepoint(mouse_pos):
                    clicked = True
                    main_setting()
                if quit_button_pause.rect.collidepoint(mouse_pos):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False
        #menu_text =
        pygame.display.flip()
        #pygame.display.update()

def main_score():
    pygame.display.set_caption("Score")
    clicked = False
    pg.mixer.music.load("sound\Saint Seiya - Pause.mp3")
    pg.mixer.music.play(-1)

    y = 280
    score_list_txt = []
    font_tabla = pygame.font.SysFont("Wide Latin",30)
    lista_puntajes = read_score()
    for indice, item in enumerate(lista_puntajes):

    # Si estamos en la primera vuelta, utilizamos la tipografia color blanco
        if len(score_list_txt) == 0:
            color_txt = BLANCO
        else:
            color_txt = ROJO_SEIYA

        nro_txt = font_tabla.render(str(indice + 1), True, (color_txt))
        nombre_txt = font_tabla.render(format_name(str(item["name"])), True, color_txt)
        puntaje_txt = font_tabla.render(format_score(str(item["score"])), True, color_txt)

        score_list_txt.append((nro_txt, (290, y)))
        score_list_txt.append((nombre_txt, (360, y)))
        score_list_txt.append((puntaje_txt, (1020, y)))

        y += 50
    print('score0')
    read_score()

    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        screen.blit(imagen_fondo_score,imagen_fondo_score.get_rect())

        

        # menu_button_game_over.draw(screen,mouse_pos)
        # quit_button_game_over.draw(screen,mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and clicked == False:
                if quit_button_score.rect.collidepoint(mouse_pos):
                    clicked = True
                    main_setting()
            #         main_menu()
            #     if menu_button_game_over.rect.collidepoint(mouse_pos):
            #         pygame.quit()
            #         sys.exit()
            # if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            #     clicked = False
        screen.blit(imagen_fondo_score, (0, 0))
        screen.blits(score_list_txt)
        quit_button_score.draw(screen,mouse_pos)
        #screen.blit(txt_boton, pos_txt_boton)

        pygame.display.flip()

def main_game_over(name,score,lives):
    
    #score_total_lives = lives *1000
    #total_score = score + score_total_lives
    pygame.display.set_caption("Game Over")
    clicked = False
    pg.mixer.music.load("sound\Saint Seiya - Pause.mp3")
    pg.mixer.music.play(-1)

    update_score(name,score)

    while True:

        mouse_pos = pygame.mouse.get_pos()

        screen.blit(imagen_fondo_game_over,imagen_fondo_game_over.get_rect())

        draw_text(f'Score: {score}',font_game_over,ROJO_SEIYA,300,260)

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
                if menu_button_game_over.rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False
        #menu_text =
        pygame.display.flip()
        #pygame.display.update()

main_menu()






