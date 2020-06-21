import pygame as pg
import sys

from Classes.Inputs import *
from Classes.Menu import *
from Classes.CapuchoMAN import *
from Classes.Camera import *
from Constants import *


class GameController:
    # aqui va el metodo o variable estatica gameStates
    def __init__(self,capuchoMan,gui,soundPlayer,level):
        self.clock = pg.time.Clock()
        self.capuchoMan = capuchoMan
        self.gui = gui
        self.soundPlayer = soundPlayer
        self.level = level
        self.gameOver = False


    def main(self):
        while not self.gameOver:
            self.capuchoMan.update()
            self.gui.update()
            self.clock.tick(FPS)
