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
    '''
    def update(self):
        self.vel.y = globales.vely_entorno
        self.vel.x = globales.velx_entorno
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.mask = pg.mask.from_surface(self.image)
    '''
