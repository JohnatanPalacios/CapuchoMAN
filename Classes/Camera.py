import pygame as pg
import sys

from Classes.Maths import *
from Constants import *

class Camera:
    def __init__(self,capuchoMan):
        self.vel = Vec2D()
        self.capuchoMan = capuchoMan
        self.right = WIDTH
        self.left = 0
        self.size = 7680
        self.stop = False

    def update(self):
        if (self.capuchoMan.rect.left - 64) <= 0 or (self.capuchoMan.rect.right + 64) >= self.size:
            self.stop = True
            self.vel.x = 0
        else:
            self.stop = False

        if not self.stop and ((self.left + 320) >= self.capuchoMan.rect.left) and (self.capuchoMan.rect.right <= (self.right - 960)):
            self.vel.x = 0
            print("en espacio libre...")
        else:
            self.vel.x += (self.capuchoMan.vel.x * -1)
            self.left += (self.vel.x * -1)
            self.right += (self.vel.x * -1)
            print("movimiento de CAMARA")

    def getCameraSpeed(self):
        return [self.vel.x,self.vel.y]
