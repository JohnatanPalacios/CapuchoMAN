import pygame as pg
import sys

from Constants import *

pg.init()

def main():
    gameStates = {"Menu": True, "History": False, "Playing": False, "Pause": False}
    started = GameController(gameStates)
    started.main()

if __name__ == "__main__":
    main()
    pg.quit()
    sys.exit()
