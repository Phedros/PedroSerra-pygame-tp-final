import pygame
from constantes import *
from auxiliar import Auxiliar

def import_platform():
    pass

class Platform:
    def __init__(self,x,y,w,h,type=0) -> None:
        self.image = Auxiliar.getSurfaceFromSpriteSheet('images\caracters\extras\plataformaUnica.png',1,1)[type]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rect_up_colition = pygame.Rect(self.rect.x, self.rect.y , self.rect.h, ALTURA_RECT_CONTACTO)

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if DEBUG:
            pygame.draw.rect(screen,ROJO,self.rect)
            pygame.draw.rect(screen,VERDE,self.rect_up_colition)