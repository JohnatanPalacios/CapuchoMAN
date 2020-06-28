import pygame as pg
import sys

from Constants import *
from .Icon import *


class Menu:
    def __init__(self,soundPlayer):
        self.menuStates = {"initial": True, "credits": False, "options": False}
        self.iconos = pg.sprite.Group()
        self.soundPlayer = soundPlayer
        self.click = (0,0,0)
        self.posMouse = [0,0]
        self.start = False


        self.play = Icon([917,297],"./Graphics/icons/IconoJugar.png")
        self.options = Icon([917,389],"./Graphics/icons/IconoOpciones.png")
        self.credits = Icon([917,482],"./Graphics/icons/IconoCreditos.png")
        self.exit = Icon([917,575],"./Graphics/icons/IconoSalir.png")
        self.accept = Icon([992,602], "./Graphics/icons/IconoAceptar.png")
        self.soundOFF = Icon([506,559], "./Graphics/icons/iconoSonidoOFF.png")
        self.soundON = Icon([506,559], "./Graphics/icons/iconoSonidoON.png")
        self.addIcons()

        self.bgInitial = pg.image.load("./Graphics/bg/inicio.png")
        self.bgControls = pg.image.load("./Graphics/bg/controles.png")
        self.bgCredits = pg.image.load("./Graphics/bg/creditos.png")

    def update(self):
        self.checkInput()
        self.initial()
        self._credits()
        self._options()
        self.checkSound()
        self.soundPlayer.update()
        pg.display.flip()

    def checkSound(self):
        if not self.start:
            self.soundPlayer.set_locationGame("menu",True)
        else:
            self.soundPlayer.set_locationGame("menu",False)

    def initial(self):
        if self.menuStates["initial"]:
            INTERFACE.fill(NEGRO)
            INTERFACE.blit(self.bgInitial,[0,0])
            if self.play.rect.collidepoint(self.posMouse):
                INTERFACE.blit(self.play.image,[917,297])
                if self.click[0] == 1:
                    self.soundPlayer.click()
                    self.start = True
            elif self.options.rect.collidepoint(self.posMouse):
                INTERFACE.blit(self.options.image,[917,389])
                if self.click[0] == 1:
                    self.soundPlayer.click()
                    self.menuStates["initial"] = False
                    self.menuStates["options"] = True
            elif self.credits.rect.collidepoint(self.posMouse):
                INTERFACE.blit(self.credits.image,[917,482])
                if self.click[0] == 1:
                    self.soundPlayer.click()
                    self.menuStates["initial"] = False
                    self.menuStates["credits"] = True
            elif self.exit.rect.collidepoint(self.posMouse):
                INTERFACE.blit(self.exit.image,[917,575])
                if self.click[0] == 1:
                    self.soundPlayer.click()
                    self._exit()

    def _credits(self):
        if self.menuStates["credits"]:
            INTERFACE.fill(NEGRO)
            INTERFACE.blit(self.bgCredits,[0,0])
            if self.accept.rect.collidepoint(self.posMouse):
                INTERFACE.blit(self.accept.image,[992,602])
                if self.click[0] == 1:
                    self.soundPlayer.click()
                    INTERFACE.blit(self.accept.image,[992,602])
                    self.menuStates["credits"] = False
                    self.menuStates["initial"] = True
            self.click = (0,0,0)

    def _options(self):
        if self.menuStates["options"]:
            INTERFACE.fill(NEGRO)
            if self.soundPlayer.getMudo():
                INTERFACE.blit(self.bgControls,[0,0])
                INTERFACE.blit(self.soundOFF.image,[506,559])
            else:
                INTERFACE.blit(self.bgControls,[0,0])
            if self.accept.rect.collidepoint(self.posMouse):
                if self.click[0] == 1:
                    self.soundPlayer.click()
                    INTERFACE.blit(self.accept.image,[992,602])
                    self.menuStates["options"] = False
                    self.menuStates["initial"] = True
                else:
                    INTERFACE.blit(self.accept.image,[992,602])
            elif self.soundON.rect.collidepoint(self.posMouse):
                if self.soundPlayer.getMudo():
                    if self.click[0] == 1:
                        self.soundPlayer.click()
                        self.soundPlayer.mudo()
                    else:
                        INTERFACE.blit(self.soundON.image,[506,559])
                else:
                    if self.click[0] == 1:
                        self.soundPlayer.click()
                        self.soundPlayer.mudo()
                    else:
                        INTERFACE.blit(self.soundOFF.image,[506,559])
            self.click = (0,0,0)


    def checkInput(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self._exit()
            self.posMouse = pg.mouse.get_pos()
            self.click = pg.mouse.get_pressed()


    def addIcons(self):
        self.iconos.add(self.soundOFF)
        self.iconos.add(self.soundON)
        self.iconos.add(self.play)
        self.iconos.add(self.options)
        self.iconos.add(self.credits)
        self.iconos.add(self.exit)
        self.iconos.add(self.accept)


    def _exit(self):
        pg.quit()
        sys.exit()
