import pygame as pg
from auxiliar import *
from constantes import *

class Box(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.frame = 0
        self.box_img = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\extras\pegasus_box.png",1,1)
        self.mini_box = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\extras\mini_pegasus_box.png",1,1)
        #self.box_img = pygame.transform.scale(self.box_img, (ANCHO_BOX, ALTO_BOX))
        self.animation = self.box_img
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.gravity = GRAVITY
        self.move_y = 0

    def update(self,lista_plataformas):
        if (self.frame < len(self.animation) - 1):
            self.frame += 1
        else:
            self.frame = 0
        
        if not self.is_on_floor(lista_plataformas):
            self.rect.y += self.gravity
            self.is_on_platform = False
        else:
            self.is_on_platform = True
    
    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen,ROJO,self.rect)

        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def is_on_floor(self,lista_plataformas):
        retorno = False
        
        for plataforma in lista_plataformas:
            if(self.rect.colliderect(plataforma.rect_up_colition)):
                retorno = True
                break
        return retorno
    
    def show_box_in_screen(self):
        self.animation = self.mini_box
        self.rect.x = 1100
        self.rect.y = 20
        self.gravity = 0
        