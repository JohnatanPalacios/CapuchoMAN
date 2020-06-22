import pygame as pg
import sys

from Classes.Camera import *
from Constants import *


class GameController:
    # aqui va el metodo o variable estatica gameStates
    def __init__(self,capuchoMan,gui,level):
        self.clock = pg.time.Clock()
        self.capuchoMan = capuchoMan
        self.gui = gui
        self.soundPlayer = soundPlayer
        self.level = level
        self.gameOver = False


    def main(self):
        while not self.gameOver:
            self.level.update()
            self.capuchoMan.update()
            self.gui.update()
            self.checkGameOver()
            self.checkSound()

            self.clock.tick(FPS)
            pg.display.flip()

    def checkSound(self):
        if not self.gameOver:
            self.soundPlayer.set_locationGame("playing",True)
        else:
            self.soundPlayer.set_locationGame("playing",False)
