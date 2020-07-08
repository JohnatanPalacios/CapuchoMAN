import pygame as pg
import sys

from Constants import *
from Classes.tools import *


class GUI():
    def __init__(self,CapuchoMAN):
        self.textBar = pg.image.load("./Graphics/gui/bar.png").convert_alpha()
        self.numeros = createAnimation("./Graphics/gui/numeros.png",[14,19],10)
        self.live = createAnimation("./Graphics/gui/vida.png",[33,28],3)
        self.posLives = [[644,2],[681,2],[718,2]]
        self.CapuchoMAN = CapuchoMAN
        self.conFPS = 0
        self.seg = 0
        self.min = 0
        self.fuente = pg.font.SysFont('Arial Black',28)
        self.posTime = [1066,-6]
        self.time = None

    def update(self):
        INTERFACE.blit(self.textBar,[0,0])
        self.drawPoints()
        self.drawHealthLive()
        self.drawTime()
        pg.display.flip()

    def set_time(self,time):
        self.min = int(time)
        self.seg = int((time-self.min)*10)
        self.conFPS = 0

    def drawPoints(self):
        miles = self.CapuchoMAN.points/1000
        centena = (self.CapuchoMAN.points - ((int(self.CapuchoMAN.points/1000))*1000))/100
        decena = (self.CapuchoMAN.points % 100)/10
        unidad = decena % 10

        if int(miles) != 0:
            INTERFACE.blit(self.numeros[int(miles)],[193,5])
        if int(centena) != 0 or miles > 0:
            INTERFACE.blit(self.numeros[int(centena)],[210,5])
        if int(decena) != 0 or centena > 0 or miles > 0:
            INTERFACE.blit(self.numeros[int(decena)],[227,5])

        INTERFACE.blit(self.numeros[int(unidad)],[244,5])

    def drawHealthLive(self):
        if self.CapuchoMAN.health > 500 and self.CapuchoMAN.lives == 3:
            INTERFACE.blit(self.live[0],self.posLives[0])
            INTERFACE.blit(self.live[0],self.posLives[1])
            INTERFACE.blit(self.live[0],self.posLives[2])
        if self.CapuchoMAN.health <= 500 and self.CapuchoMAN.lives == 3:
            INTERFACE.blit(self.live[0],self.posLives[0])
            INTERFACE.blit(self.live[0],self.posLives[1])
            INTERFACE.blit(self.live[1],self.posLives[2])
        if self.CapuchoMAN.health > 500 and self.CapuchoMAN.lives == 2:
            INTERFACE.blit(self.live[0],self.posLives[0])
            INTERFACE.blit(self.live[0],self.posLives[1])
            INTERFACE.blit(self.live[2],self.posLives[2])
        if self.CapuchoMAN.health <= 500 and self.CapuchoMAN.lives == 2:
            INTERFACE.blit(self.live[0],self.posLives[0])
            INTERFACE.blit(self.live[1],self.posLives[1])
            INTERFACE.blit(self.live[2],self.posLives[2])
        if self.CapuchoMAN.health > 500 and self.CapuchoMAN.lives == 1:
            INTERFACE.blit(self.live[0],self.posLives[0])
            INTERFACE.blit(self.live[2],self.posLives[1])
            INTERFACE.blit(self.live[2],self.posLives[2])
        if self.CapuchoMAN.health <= 500 and self.CapuchoMAN.lives == 1:
            INTERFACE.blit(self.live[1],self.posLives[0])
            INTERFACE.blit(self.live[2],self.posLives[1])
            INTERFACE.blit(self.live[2],self.posLives[2])
        if self.CapuchoMAN.lives == 0:
            INTERFACE.blit(self.live[2],self.posLives[0])
            INTERFACE.blit(self.live[2],self.posLives[1])
            INTERFACE.blit(self.live[2],self.posLives[2])

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
        self.CapuchoMAN.time = self.time
