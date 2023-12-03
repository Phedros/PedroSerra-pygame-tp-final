import pygame
from constantes import *
from plataforma import *

tile_size = 40

class World():
    def __init__(self,platform_to_load):
        self.tile_list = []

        list = platform_to_load

        Auxiliar.list_to_json(list,"level_one")

        #load images
        row_count = 0
        for row in list:
            col_count = 0
            for tile in row:
                if tile == 1:
                    block = Platform(col_count * tile_size , row_count * tile_size , tile_size,tile_size)
                    self.tile_list.append(block)
                col_count += 1
            row_count += 1


        #platform_list.append(Platform(1200,450,40,40))



    @staticmethod
    def draw_grid(screen,tile_size):
        for line in range (0, 40):
            pygame.draw.line(screen, (BLANCO), (0, line * tile_size), (ANCHO_VENTANA, line * tile_size))
            pygame.draw.line(screen, (BLANCO), (line * tile_size, 0), (line * tile_size, ALTO_VENTANA))

    @staticmethod
    def load_level(num_level:int, json_file, objet_to_load):
        match num_level:
            case 1:
                json_level = json_file["level_1"]
                object = World.load_objet(objet_to_load, json_level)
            case 2:
                json_level = json_file["level_2"]
                object = World.load_objet(objet_to_load, json_level)
            case 3:
                json_level = json_file["level_3"]
                object = World.load_objet(objet_to_load, json_level)
            case 4:
                json_level = json_file["level_4"]
                object = World.load_objet(objet_to_load, json_level)
            case 5:
                json_level = json_file["level_5"]
                object = World.load_objet(objet_to_load, json_level)
            case 6:
                json_level = json_file["level_6"]
                object = World.load_objet(objet_to_load, json_level)
            case 7:
                json_level = json_file["level_7"]
                object = World.load_objet(objet_to_load, json_level)
            case 8:
                json_level = json_file["level_8"]
                object = World.load_objet(objet_to_load, json_level)
            case 9:
                json_level = json_file["level_9"]
                object = World.load_objet(objet_to_load, json_level)
            case 10:
                json_level = json_file["level_10"]
                object = World.load_objet(objet_to_load, json_level)
            case 11:
                json_level = json_file["level_11"]
                object = World.load_objet(objet_to_load, json_level)
            case 12:
                json_level = json_file["level_12"]
                object = World.load_objet(objet_to_load, json_level)
        return object

    @staticmethod
    def load_objet(objet_to_load,json_level):
        match objet_to_load:
            case 'player':
                objet = json_level["player"]
            case 'super_player':
                objet = json_level["super_player"]
            case 'enemy_list':
                enemy_list = []
                enemies_dict = json_level["enemy_list"]
                for valores in enemies_dict.values():
                    enemy_list.append(valores)
                return enemy_list
            case 'box':
                objet = json_level["box"]
            case 'platforms':
                objet = json_level["platforms"]

        return objet


    #                                                   1,1,1,1,1,1,1,1,1,1,1,1,1,1
    #       1,1,2,2,2,3,3,4,4,4,5,5,6,6,6,7,7,8,8,8,9,9,0,0,0,1,1,2,2,2,3,3,4,4,4,5 
    #   4,8,2,6,0,4,8,2,6,0,4,8,2,6,0,4,8,2,6,0,4,8,2,6,0,4,8,2,6,0,4,8,2,6,0,4,8,2
    # 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  40
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  80
    # [0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],  120
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  160
    # [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  200
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  240
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  280
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  320
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  360
    # [0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  400
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  440
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  480
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0],  520
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  560
    # [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  600
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  640
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  680
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  720
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  760
    # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]   800
