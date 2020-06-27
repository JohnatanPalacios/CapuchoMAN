import pygame as pg
import sys

from Entities.BaseBlock import *

class Platform(BaseBlock):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.damage = 0
