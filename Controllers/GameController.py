import pygame as pg
import sys

from Classes.Camera import *
from Constants import *

#######################################
# OJO SI NO SE HACEN LAS COLISIONES CON ESTO NO FUNCIONA LA MASCARA
# collide_mask (sprite1, sprite2) -> (int, int)
#########################################################

class GameController:
    # aqui va el metodo o variable estatica gameStates
    def __init__(self,capuchoMan,gui,level):
        self.clock = pg.time.Clock()
        self.capuchoMan = capuchoMan
        self.gui = gui
        self.soundPlayer = soundPlayer
        self.level = level
        self.gameOver = False

        self.player = pg.sprite.Group()
        self.enemigos = pg.sprite.Group()
        self.bloques = pg.sprite.Group()
        self.bonus = pg.sprite.Group()
        self.molotovs = pg.sprite.Group()


    def main(self):
        while not self.gameOver:
            self.level.update()
            self.capuchoMan.update()
            self.gui.update()
            self.checkGameOver()
            self.checkSound()

            self.clock.tick(FPS)
            pg.display.flip()

    def drawGroups(self):
        for group in groups:
            group.draw(interface)

    def checkSound(self):
        if not self.gameOver:
            self.soundPlayer.set_locationGame("playing",True)
        else:
            self.soundPlayer.set_locationGame("playing",False)
