import pygame as pg
import sys

pg.mixer.init()

class Mixer:
    def __init__(self):
        self.locationGame = {"menu": False, "history": False, "playing": False}
        self.playList = [pg.mixer.music.load("./Sounds/rock1.ogg"),
                        pg.mixer.music.load("./Sounds/rock2.ogg"),
                        pg.mixer.music.load("./Sounds/rock3.ogg")]
        self.musicMenu = pg.mixer.Sound("./Sounds/menu.ogg")
        self.musicHistoria = pg.mixer.Sound("./Sounds/historia.ogg")
        self.sonidoClick = pg.mixer.Sound('./Sounds/Click.ogg')
        self.grunt = pg.mixer.Sound('./Sounds/grunt.ogg')
        self.flagMenu = True
        self.flagMudo = False
        self.flagHistoria = True
        self.conPlayList = 0

    def update(self):
        self.menu()
        self.history()
        self.playing()

    def set_locationGame(self,state,value):
        if state in self.locationGame:
            self.locationGame[state] = value


    def menu(self):
        if self.flagMudo:
            self.musicMenu.stop()
            self.flagMenu = True
        elif self.locationGame["menu"] and not self.flagMudo and self.flagMenu:
            self.musicMenu.play(-1)
            self.flagMenu = False
        elif not self.locationGame["menu"]:# and not self.flagMenu:
            self.musicMenu.stop()
            self.flagMenu = True

    def history(self):
        if self.flagMudo:
            self.musicHistoria.stop()
            self.flagHistoria = True
        elif self.locationGame["history"] and not self.flagMudo and self.flagHistoria:
            self.musicHistoria.play(-1)
            self.flagHistoria = False
        elif not self.locationGame["history"]:# and not self.flagMenu:
            self.musicHistoria.stop()
            self.flagHistoria = True


    def playing(self):
        if self.locationGame["playing"]:
            if not self.flagMudo:
                if pg.mixer.music.get_busy() == 0: #1 es sonando y 0 es sin sonido
                    self.playList[self.nextSong()]
                    pg.mixer.music.play()
        else:
            pg.mixer.music.stop()


    def click(self):
        self.sonidoClick.play()

    def grunt(self):
        self.grunt.play()

    def nextSong(self):
        if self.conPlayList < len(self.playList):
            self.conPlayList += 1
        else:
            self.conPlayList = 0
        return (self.conPlayList - 1)

    def mudo(self):
        if not self.flagMudo:
            self.flagMudo = True
            print("apagado")
        else:
            self.flagMudo = False
            print("encendido")

    def getMudo(self):
        return self.flagMudo
