import pygame as pg
import sys


class Inputs:
    def __init__(self,clase):
        self.clase = clase
        self.keyAction = None


    def update(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                #self.inGame = False
                self.clase.inGame = False
            self.keyAction = pg.key.get_pressed()
