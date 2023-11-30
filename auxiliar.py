import pygame
from constantes import *


class Auxiliar:
    def __init__(self):
        self.time = TIEMPO_TOTAL

    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        x = 0
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                lista.append(surface_fotograma)
        return lista
    

    def temporizador(self,tiempo):
        self.time -= tiempo
        format_time = self.time
        format_time = int(format_time/1000)

        return format_time
    
    @staticmethod
    def center_image(image):
        ancho_imagen, alto_imagen = image.get_size()
        distance = (ANCHO_VENTANA/2) - (ancho_imagen/2)
        return distance
    
    @staticmethod
    def center_rect(rect,direction):
        if direction == 'W':
            size = rect
            distance = (ANCHO_VENTANA/2) - (size/2)
        elif direction == 'H':
            size = rect
            distance = (ALTO_VENTANA/2) - (size/2)
        return distance
    
