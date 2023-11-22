from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,animation_speed) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",5,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",5,1,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/idle2.png",2,2)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/idle2.png",2,2,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png",2,1,False)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png",2,1,True)
        self.frame = 0
        self.lives = 3
        self.score = 0
        self.move_x = x
        self.move_y = y
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.is_jump = False
        self.animation_speed = animation_speed
        self.contador = 0
        self.direccion = DIRECCION_R
        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido_move = 0
        self.frame_rate_ms = 12
        self.move_rate_ms = 12

    def walk_control(self,direccion,animation_speed):
        if(self.direccion != direccion or (self.animation != self.walk_l and self.animation != self.walk_r)):
            self.frame = 0
            self.direccion = direccion
            if(direccion == DIRECCION_R):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            elif(direccion == DIRECCION_L):
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
            
            
            self.animation_speed = animation_speed
            self.contador = 0

    def jump_control(self,on_off,animation_speed):
        if(on_off and self.is_jump == False):
            self.move_y = -self.jump_power
            if(self.direccion == DIRECCION_R):
                self.move_x = self.speed_walk
                self.animation = self.jump_r
            elif(self.direccion == DIRECCION_L):
                self.move_x = -self.speed_walk
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
            self.animation_speed = animation_speed
            self.contador = 0
        else:
            self.is_jump = False
            self.stay_control(12)

    def stay_control(self,animation_speed):
        if(self.direccion == DIRECCION_R):
            self.animation = self.stay_r
        elif(self.direccion == DIRECCION_L):
            self.animation = self.stay_l
        self.move_x = 0
        self.move_y = 0
        self.frame = 0
        self.animation_speed = animation_speed
        self.contador = 0

    def do_movement(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido = 0
            self.rect.x += self.move_x
            self.rect.y += self.move_y

    def do_animation(self,delta_ms):

        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation>= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.contador == self.animation_speed - 1):
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

    def update(self,delta_ms):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)

        if(self.rect.y < 550):
            self.rect.y += self.gravity

    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        


