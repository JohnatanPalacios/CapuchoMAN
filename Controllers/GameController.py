import pygame as pg
import sys

from Constants import *
from Classes.Camera import *
from Controllers.RoomLoader import *
from Controllers.CollisionController import *
from Classes.CapuchoMAN import *
from Classes.GUI import *

class GameController:
    def __init__(self,soundPlayer):
        self.clock = pg.time.Clock()
        self.capuchoMan = CapuchoMAN()
        self.gui = GUI(self.capuchoMan)
        self.camera = Camera(self.capuchoMan)
        self.soundPlayer = soundPlayer
        self.gameOver = False

        self.lava =  pg.sprite.Group()
        self.door =  pg.sprite.Group()
        self.nails =  pg.sprite.Group()
        self.walls =  pg.sprite.Group()
        self.enemys =  pg.sprite.Group()
        self.coins =  pg.sprite.Group()

        self.molotovs =  pg.sprite.Group()
        self.capuchoMan.molotovs = self.molotovs

        self.level = RoomLoader(self.capuchoMan,self.door,self.nails,self.walls,self.enemys,self.coins,self.lava,self.camera,self.gui)
        self.collisions = CollisionController(self.capuchoMan,self.door,self.nails,self.enemys,self.coins,self.molotovs,self.soundPlayer)

    def main(self):
        while not self.gameOver:
            self.level.nextLevel(self.collisions.openDoor)
            self.level.update()
            self.capuchoMan.update()
            self.collisions.update()
            #self.checkGameOver()
            self.checkSound()
            #self.soundPlayer.update()
            self.updateGroups()
            self.camera.update()
            self.drawGame()
            self.gui.update()
            self.clock.tick(FPS)

    def drawGame(self):
        INTERFACE.fill(NEGRO)
        INTERFACE.blit(self.level.background,self.camera.getPos())
        INTERFACE.blit(self.capuchoMan.image,self.capuchoMan.getPos())
        #self.enemy.draw(INTERFACE)
        self.walls.draw(INTERFACE)
        self.coins.draw(INTERFACE)
        pg.display.flip()

    def checkSound(self):
        if not self.gameOver:
            self.soundPlayer.set_locationGame("playing",True)
        else:
            self.soundPlayer.set_locationGame("playing",False)

    def updateGroups(self):
        for c in self.coins:
            c.update()
        for w in self.walls:
            w.update()
        for n in self.nails:
            n.update()
        for d in self.door:
            d.update()
