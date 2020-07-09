import pygame as pg

from Classes.Maths import *
from Constants import *


class BaseBlock(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, camera):
        super().__init__()
        self.camera = camera
        self.image = pg.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.camera.vel.x
        self.rect.y += self.camera.vel.y
