import pygame as pg
import sys


def createAnimation(dir_archive, size, columms):
    archive = pg.image.load(dir_archive).convert_alpha()
    animation = []
    for c in range(columms):
        c = archive.subsurface(size[0] * c, 0, size[0], size[1])
        animation.append(c)
    return animation
