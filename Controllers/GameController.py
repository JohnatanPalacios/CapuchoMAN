import pygame as pg
import sys

from Constants import *


class GameController():
    def __init__(self,gameStates):
        self.clock = pg.time.Clock()
        self.currentTime = 0.0
        self.inGame = True
        self.inputs = Inputs()
        self.gameStates = gameStates

        self.menu = Menu(gameStates)
        self.capuchoMan = CapuchoMAN()
        self.gui = GUI(self.capuchoMan)
        self.sonidos = Mezclador()

        self.gameOver = False


    def update(self):
        self.currentTime = pg.time.get_ticks()
        self.inGame = self.inputs.get_exit()


    def main(self):
        while self.inGame:
            self.inputs.update()
            self.clock.tick(FPS)


jugadores = pg.sprite.Group()
enemigos = pg.sprite.Group()
bloques = pg.sprite.Group()
bonus = pg.sprite.Group()
molotovs = pg.sprite.Group()





grupoSprite = {"bloques":bloques,"bonos":bonus,"enemigos":enemigos}
