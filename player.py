from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump,animation_speed,contador) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",5,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",5,1,True)
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/idle.png",1,1)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png",18,2,False)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump.png",18,2,True)
        self.frame = 0
        self.lives = 3
        self.score = 0
        self.move_x = x
        self.move_y = y
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump = jump
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.is_jump = False
        self.animation_speed = animation_speed
        self.contador = contador


    def control(self,action,animation_speed):

        if(action == "WALK_R"):
            self.move_x = self.speed_walk
            self.animation = self.walk_r
            self.frame = 0
            self.animation_speed = animation_speed
            self.contador = 0
        elif(action == "WALK_L"):
            self.move_x = -self.speed_walk
            self.animation = self.walk_l
            self.frame = 0
            self.animation_speed = animation_speed
            self.contador = 0
        elif(action == "JUMP_R"):
            self.move_y = -self.jump
            self.move_x = self.speed_walk
            self.animation = self.jump_r
            self.frame = 0
            self.is_jump = True
            self.animation_speed = animation_speed
            self.contador = 0

        elif(action == "JUMP_L"):
            self.move_y = -self.jump
            self.move_x = -self.speed_walk
            self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
            self.animation_speed = animation_speed
            self.contador = 0

        elif(action == "STAY"):
            self.animation = self.stay
            self.move_x = 0
            self.move_y = 0
            self.frame = 0
            self.animation_speed = animation_speed
            self.contador = 0
            
    

    def update(self):
            
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


        self.rect.x += self.move_x
        self.rect.y += self.move_y
        
        if(self.rect.y < 550):
            self.rect.y += self.gravity
    
    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        


