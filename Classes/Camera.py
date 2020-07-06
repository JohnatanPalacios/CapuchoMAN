import pygame as pg
import sys

from Classes.Maths import *
from Constants import *

class Camera:
    def __init__(self,capuchoMan):
        self.vel = Vec2D()
        self.capuchoMan = capuchoMan
        self.right = int(WIDTH/4) * 3
        self.left = int(WIDTH/4)
        self.top = int(HEIGTH/8) * 3
        self.bottom = int(HEIGTH/8) * 5
        self.size = None ### get_size() returns a tuple, but not necessary now
        self.pos = Vec2D()
        self.orientation = None

    def update(self):
        if self.orientation == "horizontal":
            if (self.capuchoMan.rect.left > self.left) and (self.capuchoMan.rect.right < self.right):
                self.vel.x = 0
            elif (self.capuchoMan.rect.left <= self.left) and (self.pos.x * -1 > 0):
                self.vel.x = (self.capuchoMan.vel.x * -1)
                self.capuchoMan.rect.left = self.left
            elif (self.capuchoMan.rect.right >= self.right) and ((self.pos.x * -1) + WIDTH +10 < self.size):
                self.vel.x = (self.capuchoMan.vel.x * -1)
                self.capuchoMan.rect.right = self.right
            else:
                self.vel.x = 0
        elif self.orientation == "vertical":
            #if (self.capuchoMan.rect.top > self.top) and (self.capuchoMan.rect.bottom < self.bottom):
            #    self.vel.y = 0
            if (self.capuchoMan.rect.top <= self.top) and (self.pos.y * -1 > 0):
                self.vel.y = int(self.capuchoMan.vel.y * -1)
                self.capuchoMan.rect.top = self.top
            elif (self.capuchoMan.rect.bottom >= self.bottom) and ((self.pos.y * -1) + HEIGTH +12 < self.size):
                self.vel.y = int(self.capuchoMan.vel.y * -1)
                self.capuchoMan.rect.bottom = self.bottom
            else:
                self.vel.y = 0
            #print(self.pos)
            print(self.capuchoMan.vel)

        self.move()

    def move(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

    def restart(self):
        self.pos.x = 0
        self.pos.y = 0
