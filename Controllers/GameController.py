import pygame as pg
import sys

from Classes.Camera import *
from Constants import *
from Controllers.RoomLoader import *
from Controllers.CollisionController import *

from Classes.CapuchoMAN import *
from Classes.GUI import *

#######################################
# OJO SI NO SE HACEN LAS COLISIONES CON ESTO NO FUNCIONA LA MASCARA
# collide_mask (sprite1, sprite2) -> (int, int)
#########################################################

class GameController:
    def __init__(self,soundPlayer):
        self.clock = pg.time.Clock()
        self.capuchoMan = CapuchoMAN()
        self.gui = GUI(self.capuchoMan)
        self.soundPlayer = soundPlayer
        self.gameOver = False

        self.door =  pg.sprite.Group()
        self.nails =  pg.sprite.Group()
        self.walls =  pg.sprite.Group()
        self.enemys =  pg.sprite.Group()
        self.coins =  pg.sprite.Group()

        self.molotovs =  pg.sprite.Group()
        self.capuchoMan.molotovs = self.molotovs

        self.level = RoomLoader(self.capuchoMan,self.door,self.nails,self.walls,self.enemys,self.coins)
        self.collisions = CollisionController(self.capuchoMan,self.door,self.nails,self.enemys,self.coins,self.molotovs)

    def main(self):
        while not self.gameOver:
            self.level.update()
            self.capuchoMan.update()
            self.collisions.update()
            #self.checkGameOver()
            self.checkSound()
            self.drawGame()
            self.gui.update()
            self.clock.tick(FPS)

    def drawGame(self):
        INTERFACE.fill(NEGRO)
        INTERFACE.blit(self.level.background,[0,0])
        INTERFACE.blit(self.capuchoMan.image,self.capuchoMan.getPos())
        #self.enemy.draw(INTERFACE)
        #self.coins.draw(INTERFACE)
        pg.display.flip()

    def checkSound(self):
        if not self.gameOver:
            self.soundPlayer.set_locationGame("playing",True)
        else:
            self.soundPlayer.set_locationGame("playing",False)
