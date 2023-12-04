from doctest import FAIL_FAST
import pygame
from constantes import *
from auxiliar import Auxiliar
from bullet import *

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,max_high_jump,animation_speed) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/walk.png",1,5)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/walk.png",1,5,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\stay.png",1,4)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/stay.png",1,4,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/jump.png",1,2,False)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/jump.png",1,2,True)
        self.punch_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\punch.png",1,3)
        self.punch_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\punch.png",1,3,True)
        self.jump_punch_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\jump_punch.png",1,4)
        self.jump_punch_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\jump_punch.png",1,4,True)
        self.hit_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\hit.png",1,2,False)
        self.hit_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\hit.png",1,2,True)
        self.dead_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\dead.png",1,5,False)
        self.dead_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\dead.png",1,5,True)
        self.animation_pegasus = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\seiya\animation_pegasus2.png",1,19)
        

        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.jump_high = 0
        self.max_high_jump = max_high_jump

        self.frame = 0
        self.lives = 1
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
        self.is_dead = False
        self.tiempo_transcurrido_dead = 0
        self.game_over = False

        self.animation_mode = False
        self.location_x = 0
        self.location_y = 0

        self.is_super_pegasus = False
        self.double_jump = False
        self.doing_double_jump = False
        self.countdown_pegasus_mode = False
        self.tiempo_transcurrido_pegasus_mode = 0

        self.have_box = False

        # Atributos para disparar y recargar
        self.ready = True
        self.bullet_time = 0
        self.bullet_cooldown = 50
        self.bullet_group = pygame.sprite.Group()

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
            
            if self.doing_double_jump:
                self.doing_double_jump = False
            if not self.is_on_platform:
                self.doing_double_jump = True
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

        self.check_pegasus_animation_mode(delta_ms)

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
        # if self.rect.y >= FLOOR_HIGH :
        #     self.is_on_platform = True
        #     retorno = True
        # else:
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
        self.recharge()
        self.bullet_group.draw(screen)
        self.bullet_group.update()

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
                if self.lives == 0:
                    self.is_dead = True
                    self.dead_animation
            
        if self.tiempo_transcurrido_hit > 500:
            self.is_hit = False
            self.tiempo_transcurrido_hit = 0

    def dead_animation(self,delta_ms):
        self.move_x = 0
        self.tiempo_transcurrido_dead += delta_ms
        if (self.animation != self.dead_l and self.animation != self.dead_r):
            if(self.direccion == DIRECCION_R):
                self.animation = self.dead_r
            else:
                self.animation = self.dead_l
            self.frame = 0
            self.animation_speed = 30

        if self.tiempo_transcurrido_dead > 500:
            self.frame = 1
        if self.tiempo_transcurrido_dead > 2500:
            self.game_over = True

    def super_pegasus(self,player,delta_ms):

        self.gravity = player.gravity
        self.jump_power = player.jump_power
        self.jump_high = player.jump_high
        self.frame = player.frame
        
        self.score = player.score
        self.move_x = player.move_x
        self.move_y = player.move_y
        self.animation = player.animation
        self.image = player.image
        self.rect = player.rect
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.is_jump = player.is_jump
        self.animation_speed = player.animation_speed
        self.direccion = player.direccion
        self.is_on_platform = player.is_on_platform
        self.contador = player.contador
        self.tiempo_transcurrido_animation = player.tiempo_transcurrido_animation
        self.tiempo_transcurrido_move = player.tiempo_transcurrido_move
        self.frame_rate_ms = player.frame_rate_ms
        self.move_rate_ms = player.move_rate_ms
        self.is_running = player.is_running
        self.is_hit = player.is_hit
        self.animation_flag = player.animation_flag
        self.tiempo_transcurrido_hit = player.tiempo_transcurrido_hit
        self.is_punching = player.is_punching
        self.is_dead = player.is_dead
        self.tiempo_transcurrido_dead = player.tiempo_transcurrido_dead
        self.game_over = player.game_over
        self.rect_down_colition = player.rect_down_colition
        self.rect_limit_colition = player.rect_limit_colition
        self.animation_mode = player.animation_mode
        self.doing_double_jump = player.doing_double_jump
        self.countdown_pegasus_mode = player.countdown_pegasus_mode
        self.tiempo_transcurrido_pegasus_mode = player.tiempo_transcurrido_pegasus_mode
        
        self.location_x = player.location_x
        self.location_y = player.location_y
        
        if not self.is_super_pegasus:
            self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/pegasus_walk.png",1,5)
            self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/pegasus_walk.png",1,5,True)
            self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\pegasus_stay.png",1,4)
            self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/pegasus_stay.png",1,4,True)
            self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/pegasus_jump.png",1,2,False)
            self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/pegasus_jump.png",1,2,True)
            self.punch_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\pegasus_punch.png",1,3)
            self.punch_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\pegasus_punch.png",1,3,True)
            self.jump_punch_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\pegasus_jump_punch.png",1,4)
            self.jump_punch_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\pegasus_jump_punch.png",1,4,True)
            self.hit_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\hit.png",1,2,False)
            self.hit_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\hit.png",1,2,True)
            self.dead_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\pegasus_dead.png",1,5,False)
            self.dead_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\pegasus_dead.png",1,5,True)
            self.animation_pegasus = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\seiya\animation_pegasus2.png",1,19)

            self.lives = player.lives + 1
            self.is_super_pegasus = True
            self.double_jump = True
            self.do_pegasus_animation(delta_ms)
            
            
        else:
            self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/walk.png",1,5)
            self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/walk.png",1,5,True)
            self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\stay.png",1,4)
            self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/stay.png",1,4,True)
            self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/jump.png",1,2,False)
            self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/seiya/jump.png",1,2,True)
            self.punch_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\punch.png",1,3)
            self.punch_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\punch.png",1,3,True)
            self.jump_punch_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\jump_punch.png",1,4)
            self.jump_punch_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\jump_punch.png",1,4,True)
            self.hit_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\hit.png",1,2,False)
            self.hit_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\hit.png",1,2,True)
            self.dead_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\dead.png",1,5,False)
            self.dead_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\seiya\dead.png",1,5,True)
            self.animation_pegasus = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\seiya\animation_pegasus2.png",1,19)

            self.double_jump = False
            self.lives = player.lives
            self.is_super_pegasus = False

        return self

    def do_pegasus_animation(self,delta_ms):

        self.move_x = 0
        self.tiempo_transcurrido_animation += delta_ms
        if (self.animation != self.animation_pegasus):
            
            self.location_x = self.rect.x
            self.location_y = self.rect.y
            self.rect.x = ANCHO_VENTANA/2 - self.rect.w
            self.rect.y = ALTO_VENTANA/3 - self.rect.h
            self.animation = self.animation_pegasus
            self.frame = 0
            self.animation_speed = 6
            self.animation_mode = True
            self.gravity = 0


        # if self.tiempo_transcurrido_animation > 500:
        #     self.animation_mode = False
        #     self.rect.x = self.location_x
        #     self.rect.y = self.location_y
        #     self.gravity = GRAVITY

    def check_pegasus_animation_mode(self,delta_ms):
        if (self.animation_mode and self.frame == 18):
            self.animation_mode = False
            self.animation = self.stay_r
            self.frame = 0
            self.rect.x = self.location_x
            self.rect.y = self.location_y - 50
            self.gravity = GRAVITY

        



    def recharge(self):
        if not self.ready:
            curent_time = pygame.time.get_ticks()
            if curent_time - self.bullet_time >= self.bullet_cooldown:
                self.ready = True

    def create_bullet(self):
        if self.direccion == DIRECCION_L:
            pos_x=self.rect.x
        else:
            pos_x=self.rect.x + self.rect.w
        pos_y=self.rect.y
        return Bullet(pos_x , pos_y , direction=self.direccion , img_path='images\caracters\seiya\pegasus_shoot.png')

    def shoot_bullet(self):
        if self.ready:
            self.bullet_group.add(self.create_bullet())
            self.ready = False
            self.bullet_time = pygame.time.get_ticks()