import pygame as pg
from pygame.locals import *
#from pygame.key import *
import sys


# tener en cuenta la velocidad maxima en x y
# verificar esta maxima y limitarla

class Inputs:
    def __init__(self,capuchoMan):
        self.capuchoMan = capuchoMan
        #queda pendiente acciones con el mouse

    def checkInputs(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self._exit()
            keys = pg.key.get_pressed()
            self.controls(keys)

    def controls(self,keys):
        if keys[K_a]:
            self.capuchoMan.states["direction"] = -1
            self.capuchoMan.vel.x = -7
        elif keys[K_d]:
            self.capuchoMan.states["direction"] = 1
            self.capuchoMan.vel.x = 7
        else:
            self.capuchoMan.states["direction"] = 0
            self.capuchoMan.vel.x = 0

        if keys[K_LSHIFT]:
            self.capuchoMan.vel.x *= 2

        if keys[K_SPACE]:
            self.jumping()

        if keys[K_j]:
            #self.disparar()
            pass

    def jumping(self):
        if not self.capuchoMan.states["jump"]:
            self.capuchoMan.states["jump"] = True
            self.capuchoMan.vel.y = -40

    def _exit(self):
        pg.quit()
        sys.exit()
