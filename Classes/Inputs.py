import pygame as pg
import sys


# tener en cuenta la velocidad maxima en x y
# verificar esta maxima y limitarla

class Inputs:
    def __init__(self,capuchoMan):
        self.capuchoMan = capuchoMan
        self.keys = None

    def checkInputs(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self._exit()
            self.keys = pg.key.get_pressed()
            self.controls()

    def _exit(self):
        pg.quit()
        sys.exit()

    def controls(self):
        if not self.keys[pg.K_a] or not self.keys[pg.K_d]:
            self.capuchoMan.direccion = 0
            self.capuchoMan.vel.x = 0
        if self.keys[pg.K_a]:
            self.capuchoMan.direccion = -1
            self.capuchoMan.aux_animacion = 1
            if self.keys[pg.K_LSHIFT]:
                self.capuchoMan.vel.x = -14
            else:
                self.capuchoMan.vel.x = -8
        if self.keys[pg.K_d]:
            self.capuchoMan.direccion = 1
            self.capuchoMan.aux_animacion = 0
            if self.keys[pg.K_LSHIFT]:
                self.capuchoMan.vel.x = 14
            else:
                self.capuchoMan.vel.x = 8
        if self.keys[pg.K_SPACE]:
            if not self.saltando:
                self.capuchoMan.vel.y = -36
                self.capuchoMan.saltando = True
        if self.keys[pg.K_j]:
            #self.disparar()
            pass
