from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,max_high_jump,animation_speed) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk2.png",1,5)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk2.png",1,5,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\stink\stay2.png",1,4)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/stay2.png",1,4,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump2.png",1,2,False)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/jump2.png",1,2,True)
        self.punch_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\stink\punch.png",1,3)
        self.punch_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\stink\punch.png",1,3,True)
        self.jump_punch_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\stink\jump_punch2.png",1,4)
        self.jump_punch_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\stink\jump_punch2.png",1,4,True)
        self.hit_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\stink\hit.png",1,2,False)
        self.hit_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\stink\hit.png",1,2,True)

        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.jump_high = 0
        self.max_high_jump = max_high_jump

        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
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
        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido_move = 0
        self.frame_rate_ms = 12
        self.move_rate_ms = 12

        self.is_running = False

        self.is_hit = False
        self.animation_flag = False
        self.tiempo_transcurrido_hit = 0

        self.is_punching = False
        

        self.rect_down_colition = pygame.Rect(self.rect.x, self.rect.y + self.rect.h - ALTURA_RECT_CONTACTO, self.rect.h, ALTURA_RECT_CONTACTO)
        self.rect_limit_colition = pygame.Rect((self.rect.x+self.rect.w/3), self.rect.y, self.rect.w/3, self.rect.h)        

    def walk_control(self,direccion,animation_speed,is_running):
        if(self.direccion != direccion or (self.animation != self.walk_l and self.animation != self.walk_r) or self.is_running != is_running):
            self.frame = 0
            self.direccion = direccion
            if is_running:
                self.is_running = True
                speed = self.speed_run
            else:
                self.is_running = False
                speed = self.speed_walk
            if(direccion == DIRECCION_R):
                self.move_x = speed
                if (self.is_jump) or not self.is_on_platform:
                    self.animation = self.jump_r
                else:
                    self.animation = self.walk_r
            elif(direccion == DIRECCION_L):
                self.move_x = -speed
                if (self.is_jump) or not self.is_on_platform:
                    self.animation = self.jump_l
                else:
                    self.animation = self.walk_l
            
            
            self.animation_speed = animation_speed
            self.contador = 0

    def jump_control(self,on_off:bool,animation_speed:int):
        if(on_off and self.is_jump == False):
            self.frame = 0
            self.move_y = -self.jump_power
            if(self.direccion == DIRECCION_R):
                self.move_x = self.speed_walk
                self.animation = self.jump_r
            elif(self.direccion == DIRECCION_L):
                self.move_x = -self.speed_walk
                self.animation = self.jump_l
            self.is_jump = True
            self.animation_speed = animation_speed
            self.contador = 0
        else:
            self.is_jump = False
            self.jump_high = 0
            self.stay_control(12)

    def stay_control(self,animation_speed):
        if(self.animation != self.stay_l and self.animation != self.stay_r):
            if(self.direccion == DIRECCION_R):
                self.frame = 0
                if (self.is_jump) or not self.is_on_platform:
                    self.animation = self.jump_r
                else:
                    self.animation = self.stay_r
            elif(self.direccion == DIRECCION_L):
                self.frame = 0
                if (self.is_jump) or not self.is_on_platform:
                    self.animation = self.jump_l
                else:
                    self.animation = self.stay_l
            if not self.is_jump:
                self.move_y = 0

            self.move_x = 0
            self.animation_speed = animation_speed

    def punch(self,animation_speed):
        if self.is_on_platform:
            if self.direccion == DIRECCION_R:
                self.animation = self.punch_r
            if self.direccion == DIRECCION_L:
                self.animation = self.punch_l
        else:
            if self.direccion == DIRECCION_R:
                self.animation = self.jump_punch_r
            if self.direccion == DIRECCION_L:
                self.animation = self.jump_punch_l
        self.move_x = 0
        self.frame = 0
        self.animation_speed = animation_speed


    def do_movement(self,delta_ms):
        # self.tiempo_transcurrido_move += delta_ms
        # if(self.tiempo_transcurrido_move >= self.move_rate_ms):
        #     self.tiempo_transcurrido_move = 0
        if self.rect_limit_colition.x < 0 and self.move_x < 0:
            self.move_x = 0
        if (self.rect_limit_colition.x+self.rect_limit_colition.h/2) > ANCHO_VENTANA and self.move_x > 0:
            self.move_x = 0
        
        self.rect.x += self.move_x
        self.rect.y += self.move_y

        self.jump_high -= self.move_y

        if self.jump_high >= self.max_high_jump:
            self.jump_control(False,animation_speed=8)

        self.rect_down_colition = pygame.Rect(self.rect.x + (self.rect.w/2.5), self.rect.y + self.rect.h - ALTURA_RECT_CONTACTO, self.rect.w/4, ALTURA_RECT_CONTACTO)
        self.rect_limit_colition = pygame.Rect((self.rect.x+self.rect.w/3), self.rect.y, self.rect.w/3, self.rect.h)

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
        


        #self.is_on_platform = True if self.rect.y >= FLOOR_HIGH else False

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
            pygame.draw.rect(screen,YELLOW,self.rect_limit_colition)
            pygame.draw.rect(screen,VERDE,self.rect_down_colition)
        print(f'animacion: {self.animation}')
        print(f'frame: {self.frame}')
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        
    def hit_animation(self,delta_ms,primer_hit):
        self.tiempo_transcurrido_hit += delta_ms
        if (self.animation != self.hit_l and self.animation != self.hit_r):
            if(self.direccion == DIRECCION_R):
                self.animation = self.hit_r
            else:
                self.animation = self.hit_l
            self.frame = 0
            self.animation_speed = 2
            self.is_hit = True
            if primer_hit:
                self.lives -= 1
            
        if self.tiempo_transcurrido_hit > 500:
            self.is_hit = False
            self.tiempo_transcurrido_hit = 0




