import pygame as pg
import sys

from Classes.Maths import *
from Constants import *


class Camera:
    def __init__(self, capuchoMan):
        self.vel = Vec2D()
        self.cMan = capuchoMan
        self.right = int(WIDTH/4) * 3
        self.left = int(WIDTH/4)
        self.top = int(HEIGTH/4)#int(HEIGTH/8) * 3
        self.bottom = int(HEIGTH/4) * 3#int(HEIGTH/8) * 5
        self.size = None
        self.pos = Vec2D()
        self.orientation = None

    def update(self):
        if self.orientation == "horizontal":
            if (self.cMan.rect.left > self.left) and (self.cMan.rect.right < self.right):
                self.vel.x = 0
            elif (self.cMan.rect.left <= self.left) and (self.pos.x * -1 > 0):
                self.vel.x = (self.cMan.vel.x * -1)
                self.cMan.rect.left = self.left
            elif (self.cMan.rect.right >= self.right) and ((self.pos.x * -1) + WIDTH +10 < self.size):
                self.vel.x = (self.cMan.vel.x * -1)
                self.cMan.rect.right = self.right
            else:
                self.vel.x = 0
        elif self.orientation == "vertical":
            if (self.cMan.rect.top <= self.top) and (abs(self.pos.y) > 0):
                self.vel.y = int(self.cMan.vel.y * -1)
                self.cMan.rect.top = self.top
            elif (self.cMan.rect.bottom >= self.bottom) and (abs(self.pos.y) + HEIGTH +12 < self.size):
                self.vel.y = int(self.cMan.vel.y * -1)
                self.cMan.rect.bottom = self.bottom
            else:
                self.vel.y = 0

        self.move()

    def move(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

    def setup(self,orientation,size):
        self.pos.x = 0
        self.pos.y = 0
        self.orientation = orientation
        self.size = size

    def getPos(self):
        return [self.pos.x,self.pos.y]
