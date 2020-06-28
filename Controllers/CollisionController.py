import pygame as pg
import sys

class CollisionController:
    def __init__(self,capuchoMan,door,nails,enemys,coins,molotovs):
        self.capuchoMan = capuchoMan
        self.door = door
        self.nails = nails
        self.enemys = enemys
        self.coins = coins
        self.molotovs = molotovs

    def update(self):
        self.checkCoins()
        self.checkNails()

    def checkCoins(self):
        collisionList = pg.sprite.spritecollide(self.capuchoMan,self.coins,False)#,pg.sprite.collide_mask)
        if collisionList:
            for coin in collisionList:
                self.capuchoMan.points += coin.points
                self.coins.remove(coin)

    def checkNails(self):
        collisionList = pg.sprite.spritecollide(self.capuchoMan,self.nails,False)#,pg.sprite.collide_mask)
        #print("DAÑO! REDUCCION DE SALUD ", len(collisionList))
        if collisionList:
            for nail in collisionList:
                self.capuchoMan.health -= nail.damage
