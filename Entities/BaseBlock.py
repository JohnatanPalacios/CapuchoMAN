import pygame as pg

from Classes.Maths import *
from Constants import *

class BaseBlock(pg.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pg.Surface([width,height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = Vec2D()

    def update(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y

    def setVel(self,vel):
        self.vel.x = vel[0]
        self.vel.y = vel[1]
