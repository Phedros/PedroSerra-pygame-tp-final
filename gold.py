import pygame as pg
from auxiliar import *
from constantes import *

class Gold(pg.sprite.Sprite):
    def __init__(self,level):
        super().__init__()
        self.frame = 0
        match level:
            case 1 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\1_aries_armo.png",1,1)
            case 2 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\2_tauro_armo.png",1,1)
            case 3 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\3_gemini_armo.png",1,1)
            case 4 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\4_cancer_armo.png",1,1)
            case 5 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\5_leo_armo.png",1,1)
            case 6 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\6_virgo_armo.png",1,1)
            case 7 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\7_libra_armo.png",1,1)
            case 8 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\8_cancer_armo.png",1,1)
            case 9 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\9_sagitario_armo.png",1,1)
            case 10 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\10_capricornio_armo.png",1,1)
            case 11 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\11_acuario_armo.png",1,1)
            case 12 :
                self.gold_img = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\extras\12_pisis_armo.png",1,1)
        self.animation = self.gold_img
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 10
        self.gravity = GRAVITY
        self.move_y = 0
        self.level = level


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
        
    
        # 