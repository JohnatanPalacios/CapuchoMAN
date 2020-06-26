import pygame as pg
import sys

from Classes.Camera import *
from Constants import *
from Controllers.RoomLoader import *

#######################################
# OJO SI NO SE HACEN LAS COLISIONES CON ESTO NO FUNCIONA LA MASCARA
# collide_mask (sprite1, sprite2) -> (int, int)
#########################################################
'''
self.groups = {"player": player,
                "molotovs": molotovs,
                "door": door,
                "nails": nails,
                "platforms": platforms,
                "walls": walls,
                "enemys": enemys,
                "coins": coins}
'''


class GameController:
    # aqui va el metodo o variable estatica gameStates

    def __init__(self,capuchoMan,gui,soundPlayer):
        self.clock = pg.time.Clock()
        self.capuchoMan = capuchoMan
        self.gui = gui
        self.soundPlayer = soundPlayer
        self.gameOver = False

        self.player =  pg.sprite.Group()
        self.molotovs =  pg.sprite.Group()
        self.door =  pg.sprite.Group()
        self.nails =  pg.sprite.Group()
        self.platforms =  pg.sprite.Group()
        self.walls =  pg.sprite.Group()
        self.enemys =  pg.sprite.Group()
        self.coins =  pg.sprite.Group()

        self.level = RoomLoader(capuchoMan,self.door,self.nails,self.platforms,self.walls,self.enemys,self.coins)
        #self.collisions = CollisionController()


    def main(self):
        while not self.gameOver:
            self.level.update()
            self.capuchoMan.update()
            self.gui.update()
            #self.collisions()
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
