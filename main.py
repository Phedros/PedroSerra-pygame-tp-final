import pygame
import sys
from constantes import *
from player import Player

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
    y=0,
    speed_walk=4,
    speed_run=8,
    gravity=8,
    jump=16,
    animation_speed=1,
    contador=0
    )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.control("WALK_L",8)
            if event.key == pygame.K_RIGHT:
                player_1.control("WALK_R",8)
            if event.key == pygame.K_SPACE:
                player_1.control("JUMP_R",1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                player_1.control("STAY",1)

    screen.blit(imagen_fondo,imagen_fondo.get_rect()) #fundimos la imagen de fondo
   
    player_1.update()
    player_1.draw(screen)
    
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
    
    delta_ms = clock.tick(FPS)  #limitando que vaya a una velocidad determinada
    tiempo_mil += delta_ms
    tiempo = int(tiempo_mil/1000)

    print(f'clock: {tiempo}')



    






