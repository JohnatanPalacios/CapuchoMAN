import pygame as pg
import sys

from Classes.Maths import *
from Classes.Inputs import *
from Classes.Animation import *
from Constants import *

class CapuchoMAN(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.input = Inputs(self)
        self.lives = 3
        self.health = 1000
        self.points = 0
        self.states = {"jump": False, "inAir": False, "pause": False, "direction": 1, "openDoor": False}
        self.animation = Animation(self,"./Graphics/saltando (64x47).png",
                                        "./Graphics/CapMAN.png",[41,60], 6, 5, 28)
        self.vel = Vec2D()
        self.walls = None
        self.time = None
        self.molotovs = None
        self.gravedad = 3.5
        self.mapOrientation = None

    def update(self):
        self.input.checkInputs()
        self.gravity()
        self.move()
        self.animation.update()
        self.checkHealt()

    def move(self):
        if self.mapOrientation == "horizontal":
            self.rect.x = int(self.rect.x + self.vel.x)
            self.checkCollisionX()
            self.rect.y = int(self.rect.y + self.vel.y)
            self.checkCollisionY()
        elif self.mapOrientation == "vertical":
            self.rect.y = int(self.rect.y + self.vel.y)
            self.checkCollisionY()
            self.rect.x = int(self.rect.x + self.vel.x)
            self.checkCollisionX()


    def gravity(self):
        self.vel.y += self.gravedad

    def checkCollisionX(self):
        collisionList = pg.sprite.spritecollide(self,self.walls,False)#,pg.sprite.collide_mask)
        print("colisiones en x: ",len(collisionList))
        if collisionList:
            for b in collisionList:
                if ((self.rect.right >= b.rect.left) and (self.rect.right <= b.rect.right)):
                    self.rect.right = b.rect.left
                elif ((self.rect.left <= b.rect.right) and (self.rect.left >= b.rect.left)):
                    self.rect.left = b.rect.right

    def checkCollisionY(self):
        collisionList = pg.sprite.spritecollide(self,self.walls,False)#,pg.sprite.collide_mask)
        print("colisiones en y: ",len(collisionList))
        if collisionList:
            for b in collisionList:
                if ((self.rect.bottom >= b.rect.top) and (self.rect.bottom <= b.rect.bottom)):
                    self.vel.y = 0
                    self.states["jump"] = False
                    self.states["inAir"] = False
                    self.rect.bottom = b.rect.top
                elif ((self.rect.top <= b.rect.bottom) and (self.rect.top >= b.rect.top)):
                    self.vel.y = 0
                    self.rect.top = b.rect.bottom
                    self.vel.y += self.gravedad
        else:
            self.states["inAir"] = True

    def checkHealt(self):
        if (self.rect.bottom > HEIGTH + 100) or (self.time == '0:00'):
            self.lives -= 1
        elif self.health <= 0:
            self.lives -= 1
            self.health = 1000

    '''
    def disparar(self):
        molotov = Molotov(self.rect.center,self.direccion)
        self.molotovs.add(molotov)
    '''

    def getPos(self):
        return [self.rect.x,self.rect.y]

    def setup(self,pos,walls,mapOrientation): #cambiar por setup o setups igual en camara
        self.rect.x = int(pos[0])
        self.rect.y = int(pos[1])
        self.walls = walls
        self.mapOrientation = "horizontal"
