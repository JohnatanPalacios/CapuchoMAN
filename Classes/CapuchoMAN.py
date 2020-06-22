import pygame as pg
import sys

from Classes.Maths import *
from Classes.Inputs import *
from Classes.tools import *



class Jugador(pg.sprite.Sprite):
    def __init__(self):
        self.posInicial = None
        self.input = Inputs(self)
        self.vidas = 3
        self.salud = 1000
        self.puntos = 0

        self.animacion = self.crear_animacion()
        self.frame = 0
        self.direccion = 0
        self.aux_animacion = 0
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.vel = Vec2D()
        self.states = {"jump": False, "pause": False}
        self.walls = None
        self.molotovs = None
        self.time = None
        self.gravedad = 3.5

    def update(self):
        self.move()
        self.gravity()
        self.animation()
        self.input.checkInputs()

    def move(self):
        self.rect.x += self.vel.x
        self.checkCollisionX()
        self.rect.y += self.vel.y
        self.checkCollisionY()

    def gravity(self):
        self.vel.y += self.gravedad

    def animation(self):
        self.frame = animate(self.frame, 28, self.direccion)
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.mask = pg.mask.from_surface(self.image)

    def checkCollisionX(self):
        collisionList = pg.sprite.spritecollide(self,self.bloques,False,pg.sprite.collide_mask)
        if collisionList:
            for b in collisionList:
                if ((self.rect.right >= b.rect.left) and (self.rect.right <= b.rect.right)):
                    self.rect.right = b.rect.left
                elif ((self.rect.left <= b.rect.right) and (self.rect.left >= b.rect.left)):
                    self.rect.left = b.rect.right

    def checkCollisionY(self):
        collisionList = pg.sprite.spritecollide(self,self.bloques,False,pg.sprite.collide_mask)
        if collisionList:
            for b in collisionList:
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

    def checkGameOver(self):
        if self.vidas == 0:
            self.gameOver = True

    def crear_animacion(self):
        animacion = []
        animacion.append(crear_sprite("./jugador/sprites/derecha.png", [41,60], 6, 5))
        animacion.append(crear_sprite("./jugador/sprites/izquierda.png", [41,60], 6, 5))
        return animacion

        '''
         pygame.transform.flip()
         flip vertically and horizontally
         flip(Surface, xbool, ybool) -> Surface

         This can flip a Surface either vertically, horizontally, or both. Flipping a Surface is non-destructive and returns a new Surface with the same dimensions.
        '''

    def restarVida(self,cantidad):
        jugador.vida -= cantidad

    def setTime(self,time):
        self.time = time

    '''
    def disparar(self):
        molotov = Molotov(self.rect.center,self.direccion)
        self.molotovs.add(molotov)
    '''
