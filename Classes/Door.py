import pygame as pg
import sys

from Entities.BaseBlock import *

class Door(BaseBlock):
    def __init__(self,x,y,width,height,camera):
        super().__init__(x,y,width,height,camera)
        self.damage = 0
