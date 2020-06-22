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

# colores
NEGRO = [0, 0, 0]
BLANCO = [255, 255, 255]
ROJO = [255, 0, 0]
VERDE = [0, 255, 0]
AZUL = [0, 0, 255]
