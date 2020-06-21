import pygame as pg
import sys


class Inputs():
    def __init__():
        self.posMouse = None
        self.clickMouse = None
        self.keyAction = None
        self.exit = False


    def update(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.exit = False
            self.posMouse = pg.mouse.get_pos()
            self.clickMouse = pg.mouse.get_pressed()
            self.keyAction = pg.key.get_pressed()

    def get_pos(self):
        return self.posMouse

    def get_click(self):
        return self.clickMouse

    def get_keyAction(self):
        return self.keyAction

    def get_exit(self):
        return (not self.exit)
