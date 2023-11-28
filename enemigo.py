import pygame
from auxiliar import Auxiliar
from constantes import *

class Enemy:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,max_high_jump,animation_speed) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\enemy\enemy_walk2.png",1,6)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\enemy\enemy_walk2.png",1,6,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\enemy\enemy_stay.png",1,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\enemy\enemy_stay.png",1,1,True)

        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.max_high_jump = max_high_jump
        self.animation_speed = animation_speed

        self.frame = 0
        self.lives = 3
        self.score = 0
        self.move_x = 2
        self.move_y = 0

        self.animation = self.walk_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_jump = False
        self.animation_speed = animation_speed
        self.direccion = DIRECCION_R
        self.is_on_platform = False
        self.contador = 0
        self.time_lapse = 0
        self.direction_flag = False

        self.rect_down_colition = pygame.Rect(self.rect.x/4, self.rect.y + self.rect.h - ALTURA_RECT_CONTACTO, self.rect.h, ALTURA_RECT_CONTACTO)

    def walk(self,animation_speed):
        self.frame = 0
        if (self.direccion == DIRECCION_R):
            self.move_x = self.speed_walk
            self.animation = self.walk_r
        if (self.direccion == DIRECCION_L):
            self.move_x = -self.speed_walk
            self.animation = self.walk_l
        
        self.animation_speed = animation_speed
        self.contador = 0
        

    def stay_control(self,animation_speed):
        if(self.direccion == DIRECCION_R):
            self.animation = self.stay_r
        elif(self.direccion == DIRECCION_L):
            self.animation = self.stay_l
        self.move_x = 0
        #self.frame = 0
        self.animation_speed = animation_speed
        #self.contador = 0

    def do_movement(self,delta_ms):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        # print(f'rect x: {self.rect.x}')
        # print(f'move x: {self.move_x}')

        self.rect_down_colition = pygame.Rect(self.rect.x, self.rect.y + self.rect.h - ALTURA_RECT_CONTACTO, self.rect.h, ALTURA_RECT_CONTACTO)

    def do_animation(self,delta_ms):

        if(self.contador >= self.animation_speed):
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
                if(self.is_jump == True):
                    self.is_jump = False
                    self.move_y = 0
            self.contador = 0
        else:
            self.contador += 1

    def update(self,delta_ms,lista_plataformas):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)

        if not self.is_on_floor(lista_plataformas):
            self.rect.y += self.gravity
            self.is_on_platform = False
        else:
            self.is_on_platform = True

    def is_on_floor(self,lista_plataformas):
        retorno = False
        if self.rect.y >= FLOOR_HIGH :
            self.is_on_platform = True
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_down_colition.colliderect(plataforma.rect_up_colition)):
                    retorno = True
                    break
        return retorno
    
    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,ROJO,self.rect)
            pygame.draw.rect(screen,VERDE,self.rect_down_colition)
        # print(f'frame: {self.frame}')
        # print(f'animation: {self.animation}')
        # print(f'speedWalk: {self.speed_walk}')
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def animation_enemy(self,delta_ms):
        self.time_lapse += delta_ms
        if self.time_lapse > 1000:
            if self.direction_flag:
                # print(f'direccion L')
                self.direccion = DIRECCION_L
                self.direction_flag = False
            else:
                # print(f'direccion R')
                self.direccion = DIRECCION_R
                self.direction_flag = True
            self.walk(animation_speed=6)
            self.time_lapse = 0
