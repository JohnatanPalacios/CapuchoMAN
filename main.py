import pygame as pg
import sys

from Controllers.GameController import *
from Constants import *
from Classes.Mixer import *
from Classes.Menu import *
from Classes.CapuchoMAN import *
from Classes.GUI import *

def main():
    pg.init()
    soundPlayer = Mixer()

    menu = Menu(soundPlayer)
    while not menu.start:
        menu.update()

    capuchoMan = CapuchoMAN()
    gui = GUI(capuchoMan)
    level = RoomLoader()

    playing = GameController(capuchoMan,gui,level)
    playing.main()
    #main()

if __name__ == "__main__":
    main()
    pg.quit()
    sys.exit()
