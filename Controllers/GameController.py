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
    def __init__(self,capuchoMan,gui):
        self.clock = pg.time.Clock()
        self.capuchoMan = capuchoMan
        self.gui = gui
        self.soundPlayer = soundPlayer
        self.gameOver = False

        self.groups = {"player": pg.sprite.Group(),
                        "molotovs": pg.sprite.Group(),
                        "door": pg.sprite.Group(),
                        "nails": pg.sprite.Group(),
                        "blocks": pg.sprite.Group(),
                        "enemys": pg.sprite.Group(),
                        "coins": pg.sprite.Group()}

        self.level = RoomLoader(self.groups)



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
            group.draw(INTERFACE)

    def checkSound(self):
        if not self.gameOver:
            self.soundPlayer.set_locationGame("playing",True)
        else:
            self.soundPlayer.set_locationGame("playing",False)
