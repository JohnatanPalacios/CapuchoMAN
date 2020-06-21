import pygame as pg
import sys

class Icono(pg.sprite.Sprite):
    def __init__(self,pos,address):
        pg.sprite.Sprite.__init__(self)
        self.icon =  pg.image.load(address)
        self.image = icon
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
