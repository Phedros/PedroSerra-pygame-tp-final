import pygame
from constantes import *
from auxiliar import Auxiliar

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction, img_path ):
        super().__init__()
        #self.__load_img(img_path)
        self.direction = direction
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (ANCHO_BULLET, ALTO_BULLET))
        self.rect = self.image.get_rect(center=(pos_x, pos_y+(20)))

    def update(self):
        
        match self.direction:
            case 1:
                self.rect.x += 15
                if self.rect.x >= ANCHO_VENTANA:
                    self.kill()
            case 0:
                self.rect.x -= 15
                if self.rect.x <= 0:
                    self.kill()

