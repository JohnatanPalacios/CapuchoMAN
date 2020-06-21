import pygame as pg
import sys

from Controllers.GameController import *
from Constants import *

def main():
    pg.init()
    soundPlayer = Mezclador()

    menu = Menu(self.soundPlayer)
    while not self.menu.start:
        self.menu.update()

    gui = GUI(self.capuchoMan)
    capuchoMan = CapuchoMAN(soundPlayer)
    level = RoomLoader()

    playing = GameController(capuchoMan,gui,level)
    playing.main()
    #main()

if __name__ == "__main__":
    main()
    pg.quit()
    sys.exit()
