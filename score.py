import pygame
from constantes import *
#from data_puntajes import lista_puntajes
import json
import sqlite3

def format_name(nombre):
    nombre = nombre.strip().lower().capitalize()
    return nombre

def format_score(puntaje):
    return puntaje.zfill(4)

def create_data_base():
    with sqlite3.connect("bd_score.db") as conexion:
        try:
            sentencia = ''' create  table players
                            (
                                    id integer primary key autoincrement,
                                    name text,
                                    score text
                            )
                        '''
            conexion.execute(sentencia)
            print("Se creo la tabla score")                       
        except sqlite3.OperationalError:
            print("La tabla score ya existe")    

def update_score(name,score):

    create_data_base()
    
    with sqlite3.connect("bd_score.db") as conexion:
        try:
            conexion.execute("insert into players(name,score) values (?,?)", (f"{name}", f"{score}"))
            conexion.commit()
        except:
            print("Error")

def read_score():
    list = []
    print('score1')
    with sqlite3.connect("bd_score.db") as conexion:
        cursor=conexion.execute("SELECT * FROM players ORDER BY score ASC")
        for fila in cursor:
            list.append({"name": fila[1], "score": fila[2]})

        return list


