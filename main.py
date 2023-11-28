import pygame
import sys
from constantes import *
from player import Player
from plataforma import Platform
from enemigo import *

# Superficie principal
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()
tiempo = 0
tiempo_mil = 0

imagen_fondo = pygame.image.load("images/locations/forest/Santuario_Abel.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA)) # Escalamos la imagen de fondo a la dimension de la ventana
player_1 = Player(
    x=0,
    y=530,
    speed_walk=5,
    speed_run=10,
    gravity=8,
    jump_power=25,
    max_high_jump = 450,      
    animation_speed=12
    )

enemigo_1 = Enemy(
    x=200,
    y=530,
    speed_walk= 2,
    speed_run=8,
    gravity=8,
    jump_power=25,
    max_high_jump = 450,      
    animation_speed=12
)



lista_plataformas = []
lista_plataformas.append(Platform(300,450,60,60))
lista_plataformas.append(Platform(360,450,60,60))
lista_plataformas.append(Platform(420,450,60,60))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_1.jump_control(True,animation_speed=8)   
            # if event.key == pygame.K_LALT:
            #     player_1.is_running = True 
            #     player_1.walk_control(player_1.direccion,animation_speed=6,is_running=True)   

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player_1.jump_control(False,animation_speed=8)
            # if event.key == pygame.K_LALT:
            #     player_1.is_running = False 


    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LCTRL]):
        player_1.punch(animation_speed=2)
    else:
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

    screen.blit(imagen_fondo,imagen_fondo.get_rect()) #fundimos la imagen de fondo

    for plataforma in lista_plataformas:
        plataforma.draw(screen)

    delta_ms = clock.tick(FPS)  #limitando que vaya a una velocidad determinada
    player_1.update(delta_ms,lista_plataformas)
    player_1.draw(screen)

    enemigo_1.animation_enemy(delta_ms)
    enemigo_1.update(delta_ms,lista_plataformas)
    enemigo_1.draw(screen)
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    tiempo_mil += delta_ms
    tiempo = int(tiempo_mil/1000)

    print(f'clock: {tiempo}')



    






