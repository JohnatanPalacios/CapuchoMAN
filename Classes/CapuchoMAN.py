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
        self.G = 3.5
        self.mapOrientation = None

    def update(self):
        self.move()
        self.gravity()
        self.animation.update()
        self.checkHealt()
        self.input.checkInputs()

    def move(self):
        self.rect.y = int(self.rect.y + self.vel.y)
        self.checkCollisionY()
        self.rect.x = int(self.rect.x + self.vel.x)
        self.checkCollisionX()


    def gravity(self):
        self.vel.y += self.G

    def checkCollisionX(self):
        '''
        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                if self.vel.x > 0:
                    self.rect.right = wall.rect.left
                    self.vel.x = 0
                if self.vel.x < 0:
                    self.rect.left = wall.rect.right
                    self.vel.x = 0
        '''
        collisionList = pg.sprite.spritecollide(self, self.walls, False)
        #print("colisiones en x: ", len(collisionList))
        if collisionList:
            for b in collisionList:
                if ((self.rect.right >= b.rect.left) and (self.rect.right <= b.rect.right)):
                    self.rect.right = b.rect.left
                    self.vel.x = 0
                elif ((self.rect.left <= b.rect.right) and (self.rect.left >= b.rect.left)):
                    self.rect.left = b.rect.right
                    self.vel.x = 0


    def checkCollisionY(self):
        inAir = True
        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                if self.vel.y > 0:
                    self.rect.bottom = wall.rect.top
                    self.vel.y = 0
                    self.states["jump"] = False
                    self.states["inAir"] = False
                    inAir = False
                if self.vel.y < 0:
                    self.rect.top = wall.rect.bottom
                    self.vel.y = 0
                    inAir = False
        if inAir:
            self.states["inAir"] = True
        '''
        collisionList = pg.sprite.spritecollide(self, self.walls, False)
        print("colisiones en y: ", len(collisionList))
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
        else:
            self.states["inAir"] = True
        '''

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
        return [self.rect.x, self.rect.y]

    def draw(self):
        INTERFACE.blit(self.image, self.getPos())

    def setup(self, pos, walls, mapOrientation):
        self.rect.x = int(pos[0])
        self.rect.y = int(pos[1])
        self.walls = walls
        self.mapOrientation = mapOrientation
