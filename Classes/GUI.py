import pygame as pg
import sys

from Constants import *
from Classes.tools import *


class GUI():
    def __init__(self,CapuchoMAN):
        self.barra = pg.image.load("./Graphics/gui/bar.png").convert_alpha()
        self.numeros = createSprite("./Graphics/gui/numeros.png",[14,19],10)
        self.vida = createSprite("./Graphics/gui/vida.png",[33,28],3)
        self.posVidas = [[644,2],[681,2],[718,2]]
        self.CapuchoMAN = CapuchoMAN
        self.conFPS = 0
        self.seg = 0
        self.min = 1
        self.fuente = pg.font.SysFont('Arial Black',28)
        self.posTime = [1066,-6]
        self.time = None

    def update(self):
        INTERFACE.blit(self.barra,[0,0])
        self.drawPuntos()
        self.drawVida()
        self.drawTime()

    def drawPuntos(self):
        miles = self.CapuchoMAN.puntos/1000
        centena = (self.CapuchoMAN.puntos - ((int(self.CapuchoMAN.puntos/1000))*1000))/100
        decena = (self.CapuchoMAN.puntos % 100)/10
        unidad = decena % 10

        if int(miles) != 0:
            INTERFACE.blit(self.numeros[int(miles)],[183,5])
        if int(centena) != 0 or miles > 0:
            INTERFACE.blit(self.numeros[int(centena)],[200,5])
        if int(decena) != 0 or centena > 0 or miles > 0:
            INTERFACE.blit(self.numeros[int(decena)],[217,5])

        INTERFACE.blit(self.numeros[int(unidad)],[234,5])

    def drawVida(self):
        if self.CapuchoMAN.salud > 500 and self.CapuchoMAN.vidas == 3:
            INTERFACE.blit(self.vida[0],self.posVidas[0])
            INTERFACE.blit(self.vida[0],self.posVidas[1])
            INTERFACE.blit(self.vida[0],self.posVidas[2])
        if self.CapuchoMAN.salud <= 500 and self.CapuchoMAN.vidas == 3:
            INTERFACE.blit(self.vida[0],self.posVidas[0])
            INTERFACE.blit(self.vida[0],self.posVidas[1])
            INTERFACE.blit(self.vida[1],self.posVidas[2])
        if self.CapuchoMAN.salud > 500 and self.CapuchoMAN.vidas == 2:
            INTERFACE.blit(self.vida[0],self.posVidas[0])
            INTERFACE.blit(self.vida[0],self.posVidas[1])
            INTERFACE.blit(self.vida[2],self.posVidas[2])
        if self.CapuchoMAN.salud <= 500 and self.CapuchoMAN.vidas == 2:
            INTERFACE.blit(self.vida[0],self.posVidas[0])
            INTERFACE.blit(self.vida[1],self.posVidas[1])
            INTERFACE.blit(self.vida[2],self.posVidas[2])
        if self.CapuchoMAN.salud > 500 and self.CapuchoMAN.vidas == 1:
            INTERFACE.blit(self.vida[0],self.posVidas[0])
            INTERFACE.blit(self.vida[2],self.posVidas[1])
            INTERFACE.blit(self.vida[2],self.posVidas[2])
        if self.CapuchoMAN.salud <= 500 and self.CapuchoMAN.vidas == 1:
            INTERFACE.blit(self.vida[1],self.posVidas[0])
            INTERFACE.blit(self.vida[2],self.posVidas[1])
            INTERFACE.blit(self.vida[2],self.posVidas[2])
        if self.CapuchoMAN.vidas == 0:
            INTERFACE.blit(self.vida[2],self.posVidas[0])
            INTERFACE.blit(self.vida[2],self.posVidas[1])
            INTERFACE.blit(self.vida[2],self.posVidas[2])

    def drawTime(self):
        self.seg = int(self.conFPS // FPS)
        self.conFPS += 1

        if self.seg == 60:
            self.min -= 1
            self.seg = 0
            self.conFPS = 0

        if (59 - self.seg) > 9:
            self.time = str(self.min) + ':' + str(59 - self.seg)
        else:
            self.time = str(self.min) + ':' + '0' + str(59 - self.seg)

        INTERFACE.blit(self.fuente.render(self.time,True,NEGRO),self.posTime)
        self.CapuchoMAN.setTime(self.time)

    def checkEstado(self,gameOver):
        if gameOver:
            self.conFPS = 0
            self.seg = 0
            self.min = 1
            self.time = None
            self.CapuchoMAN.setTime(self.time)
