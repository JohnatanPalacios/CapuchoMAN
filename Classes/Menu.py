import pygame as pg
import sys

from Constants import *
from .Icon import *
from Inputs import *


class Menu:
    def __init__(self,soundPlayer):
        self.menuStates = {"initial": True, "credits": False, "options": False}
        self.iconos = pg.sprite.Group()
        self.soundPlayer = soundPlayer
        self.gameStates = gameStates
        self.click = None
        self.posMouse = None
        self.start = False


        self.play = Icono([917,297],"./menu/IconoJugar.png")
        self.options = Icono([917,389],"./menu/IconoOpciones.png")
        self.credits = Icono([917,482],"./menu/IconoCreditos.png")
        self.exit = Icono([917,575],"./menu/IconoSalir.png")
        self.accept = Icono([992,602], "./menu/IconoAceptar.png")
        self.sound = Icono([506,559], "./menu/iconoSonidoOFF.png")
        self.addIcons()

        self.bgInitial = pg.image.load("./menu/inicio.png")
        self.bgControls = pg.image.load("./menu/controles.png")
        self.bgCredits = pg.image.load("./menu/credits.png")

    def update():
        self.checkInput()
        self.initial()
        self.credits()
        self.options()
        pg.display.flip()

    def initial(self):
        if self.menuStates["initial"]:
            interface.fill(NEGRO)
            interface.blit(bgInitial,[0,0])
            if self.play.rect.collidepoint(mouse):
                interface.blit(IconoJugar,[917,297])
                if click[0] == 1:
                    self.soundPlayer.click()
                    self.start = True
            elif self.options.rect.collidepoint(mouse):
                interface.blit(IconoOpciones,[917,389])
                if click[0] == 1:
                    self.soundPlayer.click()
                    self.menuStates["initial"] = False
                    self.menuStates["options"] = True
            elif self.credits.rect.collidepoint(mouse):
                interface.blit(IconoCreditos,[917,482])
                if click[0] == 1:
                    self.soundPlayer.click()
                    self.menuStates["initial"] = False
                    self.menuStates["credits"] = True
            elif self.exit.rect.collidepoint(mouse):
                interface.blit(IconoSalir,[917,575])
                if click[0] == 1:
                    self.soundPlayer.click()
                    self.exit()

    def credits(self):
        if self.menuStates["credits"]:
            interface.fill(NEGRO)
            interface.blit(bgCredits,[0,0])
            if self.accept.rect.collidepoint(mouse):
                interface.blit(IconoAceptar,[992,602])
                if click[0] == 1:
                    self.soundPlayer.click()
                    self.menuStates["credits"] = False
                    self.menuStates["initial"] = True

    def options(self):
        if self.menuStates["options"]:
            interface.fill(NEGRO)
            if self.soundPlayer.getMudo():
                interface.blit(bgControls,[0,0])
                interface.blit(IconoSonidoOFF,[506,559])
            else:
                interface.blit(bgControls,[0,0])
            if self.accept.rect.collidepoint(mouse):
                if click[0] == 1:
                    self.soundPlayer.click()
                    interface.blit(IconoAceptar,[992,602])
                    self.menuStates["options"] = False
                    self.menuStates["initial"] = True
                else:
                    interface.blit(IconoAceptar,[992,602])
            elif self.sound.rect.collidepoint(mouse):
                if self.soundPlayer.getMudo():
                    if click[0] == 1:
                        self.soundPlayer.click()
                        self.soundPlayer.mudo()
                    else:
                        interface.blit(IconoSonidoON,[506,559])
                else:
                    if click[0] == 1:
                        self.soundPlayer.click()
                        self.soundPlayer.mudo()
                    else:
                        interface.blit(IconoSonidoOFF,[506,559])


    def checkInput(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.exit()
            self.posMouse = pg.mouse.get_pos()
            self.click = pg.mouse.get_pressed()


    def addIcons(self):
        self.iconos.add(self.sound)
        self.iconos.add(self.play)
        self.iconos.add(self.options)
        self.iconos.add(self.credits)
        self.iconos.add(self.exit)
        self.iconos.add(self.accept)


    def exit(self):
        pg.quit()
        sys.exit()
