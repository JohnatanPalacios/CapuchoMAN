import pygame as pg
from pygame.locals import *
#from pygame.keys import *
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
        if keys[a]:
            self.capuchoMan.states["direction"] = -1
            self.capuchoMan.vel.x = -7
        elif keys[d]:
            self.capuchoMan.states["direction"] = 1
            self.capuchoMan.vel.x = 7
        else:
            self.capuchoMan.states["direction"] = 0
            self.capuchoMan.vel.x = 0

        if keys[LSHIFT]:
            self.capuchoMan.vel.x *= 2

        if keys[SPACE]:
            self.jumping()

        if keys[j]:
            #self.disparar()
            pass

    def jumping(self):
        if not self.capuchoMan.states["saltando"]:
            self.capuchoMan.states["saltando"] = True
            self.capuchoMan.vel.y = -36

    def _exit(self):
        pg.quit()
        sys.exit()
