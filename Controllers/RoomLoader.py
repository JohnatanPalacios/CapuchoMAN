import pygame as pg
import sys

from Classes.Walls import *
###   HOW TO USE TILEDMAPS
###   ASEPRITE (es de pago pero se puede pirata)

class RoomLoader:
    def __init__(self,groups):
        self.roomChangeFlag = False
        self.room = "A"
        self.levelChangeFlag = False
        self.level = 1
        self.door = groups["door"]
        self.nails = groups["nails"]
        self.platforms = groups["platforms"]
        self.walls = groups["walls"]
        self.enemys = groups["enemys"]
        self.coins = groups["coins"]


####### automatizar esto para que cambie de sala y nivel ######



    def update(self):
        if self.levelChangeFlag:

            self.levelChangeFlag = False

    def set_Level(self):
        self.levelChangeFlag = True

    def set_Room(self):
        self.roomChangeFlag = True


    def mapA1(self):
        mapInfo = None

        #Lectura de archivo json
        FileName = 'Maps\mapaA1.json'
        with open(FileName) as Information:
            nonlocal mapInfo
            mapInfo = json.load(Information)
        Information.close()

        #Extraccion Objetos Json
        _door = MapInfo['layers'][6]['objects']
        _nails = MapInfo['layers'][5]['objects']
        _platforms = MapInfo['layers'][4]['objects']
        _walls = MapInfo['layers'][3]['objects']
        _enemys = MapInfo['layers'][2]['objects']
        _coins = MapInfo['layers'][1]['objects']

        #Creacion de las paredes
        for i in range(len(_walls)):
            temp = Walls((_walls[i]['x']),(_walls[i]['y']),_walls[i]['width'],_walls[i]['height'])
            self.walls.add(temp)
            #temp = Block.Bloque([(walls[i]['x']),(walls[i]['y'])],walls[i]['width'],walls[i]['height'])
            #Blocks.add(temp)
