import pygame as pg
import sys

from Inputs import *
from tools import *



class Jugador(pg.sprite.Sprite):
    def __init__(self, pos, bloques):
        self.posInicial = pos
        self.inputs = Inputs(self)
        self.vidas = 3
        self.salud = 1000
        self.puntos = 0
        self.states = {}

        self.animacion = self.crear_animacion()
        self.frame = 0
        self.direccion = 0
        self.aux_animacion = 0
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.saltando = False
        self.bloques = bloques
        self.molotovs = None
        self.time = None
        self.gravedad = 3.5

    def update(self):
        self.rect.x += self.velx
        self.colision_x()
        self.rect.y += self.vely
        self.colision_y()
        self.vely += self.gravedad

        self.frame = animar(self.frame, 28, self.direccion)
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.mask = pg.mask.from_surface(self.image)

    def colision_x(self):
        lista_colision = pg.sprite.spritecollide(self,self.bloques,False,pg.sprite.collide_mask)
        if lista_colision:
            for b in lista_colision:
                if ((self.rect.right >= b.rect.left) and (self.rect.right <= b.rect.right)):
                    self.rect.right = b.rect.left
                elif ((self.rect.left <= b.rect.right) and (self.rect.left >= b.rect.left)):
                    self.rect.left = b.rect.right

    def colision_y(self):
        lista_colision = pg.sprite.spritecollide(self,self.bloques,False,pg.sprite.collide_mask)
        if lista_colision:
            for b in lista_colision:
                if ((self.rect.bottom >= b.rect.top) and (self.rect.bottom <= b.rect.bottom)):
                    self.vely = 0
                    self.saltando = False
                    self.rect.bottom = b.rect.top
                elif ((self.rect.top <= b.rect.bottom) and (self.rect.top >= b.rect.top)):
                    self.vely = 0
                    self.rect.top = b.rect.bottom
                    self.vely += self.gravedad

    def checkEstado(self):
        if (self.rect.bottom > ALTO + 100) or (self.time == '0:00'):
            self.vidas -= 1
        elif self.salud <= 0:
            self.vidas -= 1
            self.salud = 1000

    def checkGameOver(self,gameOver,estados):
        if self.vidas == 0:
            gameOver = True
            estados["nivel1"] = False
            estados["inicio"] = True
            self.reiniciar()

    def controles(self,keys):
        if not keys[pg.K_a] or not keys[pg.K_d]:
                self.velx = 0
                self.direccion = 0
        if keys[pg.K_a]:
            self.direccion = -1
            self.aux_animacion = 1
            if keys[pg.K_LSHIFT]:
                    self.velx = -14
            else:
                self.velx = -8
        if keys[pg.K_d]:
            self.direccion = 1
            self.aux_animacion = 0
            if keys[pg.K_LSHIFT]:
                    self.velx = 14
            else:
                self.velx = 8
        if keys[pg.K_SPACE]:
            if not self.saltando:
                self.vely = -36
                self.saltando = True
        if keys[pg.K_j]:
            self.disparar()

    def crear_animacion(self):
        animacion = []
        animacion.append(crear_sprite("./jugador/sprites/derecha.png", [41,60], 6, 5))
        animacion.append(crear_sprite("./jugador/sprites/izquierda.png", [41,60], 6, 5))
        return animacion

    def sumarPuntos(self,puntos):
        self.puntos += puntos

    def restarVida(self,cantidad):
        jugador.vida -= cantidad

    def setTime(self,time):
        self.time = time

    def reiniciar(self):
        self.vidas = 3
        self.salud = 1000
        self.puntos = 0
        self.frame = 0
        self.direccion = 0
        self.aux_animacion = 0
        self.rect.x = self.posInicial[0]
        self.rect.y = self.posInicial[1]
        self.velx = 0
        self.vely = 0
        self.saltando = False

    def checkColisiones(self):
        ls_col = pg.sprite.spritecollide(self,self.bonus,False,pg.sprite.collide_mask)
        if len(ls_col) > 0:
            for bono in ls_col:
                self.sumarPuntos(bono.puntos)
                self.bonus.remove(bono)

    def disparar(self):
        molotov = Molotov(self.rect.center,self.direccion)
        self.molotovs.add(molotov)
