import pygame as pg
import sys

from Classes.Maths import *
from Classes.Inputs import *
from Classes.Animation import *
from Constants import *



class CapuchoMAN(pg.sprite.Sprite):
    def __init__(self):
        #super().__init__()
        pg.sprite.Sprite.__init__(self)
        self.input = Inputs(self)
        self.vidas = 3
        self.salud = 1000
        self.puntos = 0
        self.states = {"jump": False, "pause": False, "direction": 1}

        self.image = pg.surface.Surface([41,60])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = 180
        self.rect.y = 180

        #self.animation = Animation(self,"./Graphics/saltando (64x47).png",
        #                                "./Graphics/CapMAN.png",[41,60], 6, 5, 28)

        self.vel = Vec2D()
        self.walls = None
        self.molotovs = None
        self.time = None
        self.gravedad = 3.5

    def update(self):
        #self.animation.update()
        self.input.checkInputs()
        self.move()
        self.gravity()
        print("pos capucho: ",self.rect.x," ",self.rect.y)
        print("velx: ",self.vel.x," vely: ",self.vel.y)
        print(self.states["jump"])
        print(" ")

    def move(self):
        self.rect.x = int(self.rect.x + self.vel.x)
        self.checkCollisionX()
        self.rect.y = int(self.rect.y + self.vel.y)
        self.checkCollisionY()

    def gravity(self):
        self.vel.y += self.gravedad

    def checkCollisionX(self):
        collisionList = pg.sprite.spritecollide(self,self.walls,False)#,pg.sprite.collide_mask)
        print("colision en x: ",len(collisionList))
        if collisionList:
            for b in collisionList:
                if ((self.rect.right >= b.rect.left) and (self.rect.right <= b.rect.right)):
                    self.rect.right = b.rect.left
                elif ((self.rect.left <= b.rect.right) and (self.rect.left >= b.rect.left)):
                    self.rect.left = b.rect.right

    def checkCollisionY(self):
        collisionList = pg.sprite.spritecollide(self,self.walls,False)#,pg.sprite.collide_mask)
        print("colision en y: ",len(collisionList))
        if collisionList:
            for b in collisionList:
                if self.rect.bottom >= b.rect.top:#((self.rect.bottom >= b.rect.top) and (self.rect.bottom <= b.rect.bottom)):
                    self.vel.y = 0
                    self.states["jump"] = False
                    self.rect.bottom = b.rect.top
                elif self.rect.top <= b.rect.bottom:#((self.rect.top <= b.rect.bottom) and (self.rect.top >= b.rect.top)):
                    self.vel.y = 0
                    self.rect.top = b.rect.bottom
                    self.vel.y += self.gravedad

    def checkEstado(self):
        if (self.rect.bottom > ALTO + 100) or (self.time == '0:00'):
            self.vidas -= 1
        elif self.salud <= 0:
            self.vidas -= 1
            self.salud = 1000

    def checkGameOver(self):
        if self.vidas == 0:
            self.gameOver = True

    def restarVida(self,cantidad):
        jugador.vida -= cantidad

    def setTime(self,time):
        self.time = time

    '''
    def disparar(self):
        molotov = Molotov(self.rect.center,self.direccion)
        self.molotovs.add(molotov)
    '''
