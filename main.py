import pygame as pg
import sys

from Controllers.GameController import *
from Constants import *
from Classes.Mixer import *
from Classes.Menu import *

def main():
    pg.init()
    soundPlayer = Mixer()

    menu = Menu(soundPlayer)
    while not menu.start:
        menu.update()

    gui = GUI(self.capuchoMan)
    capuchoMan = CapuchoMAN(soundPlayer)
    #level = RoomLoader()

    playing = GameController(capuchoMan,gui,level)
    playing.main()
    #main()

if __name__ == "__main__":
    main()
    pg.quit()
    sys.exit()
