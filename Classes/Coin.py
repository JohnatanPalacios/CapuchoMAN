import pygame as pg
import sys

from Entities.BaseBlock import *
from Classes.tools import *

class Coin(BaseBlock):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.points = 90
        self.frame = 0
        self.animation = createAnimation("./Graphics/coins/GoldenCoins.png",[32,32],7)
        self.numberFrames = len(self.animation)
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.animate()
        self.image = self.animation[self.frame]
        super().update()

    def animate(self):
        if self.frame > 0:
            self.frame -= 1
        else:
            self.frame = (self.numberFrames - 1)
