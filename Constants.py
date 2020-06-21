import pygame as pg
import sys

FPS = 20
WIDTH = 1280 #ANCHO
HEIGTH = 704#ALTO
windowSize = [WIDTH,HEIGTH]

interface = pg.display.set_mode(windowSize)
icon = pg.image.load('./Graphics/CapuchoMAN.png')
pg.display.set_icon(icon)
pg.display.set_caption("CapuchoMAN")
