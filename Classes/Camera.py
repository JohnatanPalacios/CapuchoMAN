import pygame as pg
import sys

from Classes.Maths import *
from Constants import *

class Camera:
    def __init__(self,capuchoMan):
        self.vel = Vec2D()
        self.capuchoMan = capuchoMan
        self.seed = int(WIDTH/4)
        self.right = self.seed * 3
        self.left = self.seed
        self.size = 7680
        self.pos = Vec2D()
        self.orientation = None

    def update(self):
        if self.orientation == "horizontal":
            if (self.capuchoMan.rect.left > self.left) and (self.capuchoMan.rect.right < self.right):
                self.vel.x = 0
            elif (self.capuchoMan.rect.left <= self.left) and (self.left - self.seed >= 0) and (self.capuchoMan.vel.x < 0):
                self.vel.x = (self.capuchoMan.vel.x * -1)
                self.capuchoMan.rect.left = self.left
            elif (self.capuchoMan.rect.right >= self.right) and (self.right + self.seed <= self.size) and (self.capuchoMan.vel.x > 0):
                self.vel.x = (self.capuchoMan.vel.x * -1)
                self.capuchoMan.rect.right = self.right
            else:
                self.vel.x = 0
        elif self.orientation == "vertical":
            pass

        self.move()

    def move(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

    def restart(self):
        self.pos.x = 0
        self.pos.y = 0
