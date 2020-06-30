import pygame as pg
import sys

class CollisionController:
    def __init__(self,capuchoMan,door,nails,enemys,coins,molotovs,soundPlayer):
        self.capuchoMan = capuchoMan
        self.door = door
        self.nails = nails
        self.enemys = enemys
        self.coins = coins
        self.molotovs = molotovs
        self.soundPlayer = soundPlayer
        self.openDoor = False

    def update(self):
        self.checkCoins()
        self.checkNails()
        self.checkDoor()

    def checkCoins(self):
        collisionList = pg.sprite.spritecollide(self.capuchoMan,self.coins,False)
        if collisionList:
            for coin in collisionList:
                self.capuchoMan.points += coin.points
                self.coins.remove(coin)

    def checkNails(self):
        collisionList = pg.sprite.spritecollide(self.capuchoMan,self.nails,False)
        if collisionList:
            for nail in collisionList:
                self.soundPlayer.grunt()
                self.capuchoMan.health -= nail.damage

    def checkDoor(self):
        collisionList = pg.sprite.spritecollide(self.capuchoMan,self.door,False)
        if collisionList and self.capuchoMan.states["openDoor"]:
            self.openDoor = True
        else:
            self.capuchoMan.states["openDoor"] = False
            self.openDoor = False
