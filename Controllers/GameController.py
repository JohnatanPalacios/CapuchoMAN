import pygame as pg
import sys

from Classes.Camera import *
from Constants import *
from Controllers.RoomLoader import *

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

        self.player = pg.sprite.Group()
        self.player.add(self.capuchoMan)
        self.molotovs =  pg.sprite.Group()

        self.door =  pg.sprite.Group()
        self.nails =  pg.sprite.Group()
        self.walls =  pg.sprite.Group()
        self.enemys =  pg.sprite.Group()
        self.coins =  pg.sprite.Group()

        self.level = RoomLoader(self.capuchoMan,self.door,self.nails,self.walls,self.enemys,self.coins)
        #self.collisions = CollisionController()

    def main(self):
        while not self.gameOver:
            self.level.update()
            self.capuchoMan.update()
            #self.collisions()
            #self.checkGameOver()
            self.checkSound()

            self.clock.tick(FPS)
            self.drawGame()
            self.gui.update()

    def drawGame(self):
        INTERFACE.fill(NEGRO)
        INTERFACE.blit(self.level.background,[0,0])
        INTERFACE.blit(self.capuchoMan.image,[self.capuchoMan.rect.x,self.capuchoMan.rect.y])
        #self.enemy.draw(INTERFACE)
        #self.coins.draw(INTERFACE)
        pg.display.flip()

    def checkSound(self):
        if not self.gameOver:
            self.soundPlayer.set_locationGame("playing",True)
        else:
            self.soundPlayer.set_locationGame("playing",False)
