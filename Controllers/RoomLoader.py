import pygame as pg
import sys
import json

from Classes.Walls import *
from Classes.Platforms import *
from Classes.Nails import *
###   HOW TO USE TILEDMAPS
###   ASEPRITE (es de pago pero se puede pirata)

class RoomLoader:
    def __init__(self,capuchoMan,door,nails,platforms,walls,enemys,coins):
        self.mapInfo = None
        self.countUP = 0
        self.alarm = True
        self.end = False
        self.background = None
        self.capuchoMan = capuchoMan
        self.door = door
        self.nails = nails
        self.platforms = platforms
        self.walls = walls
        self.enemys = enemys
        self.coins = coins


    def update(self):
        if self.alarm:
            if self.countUP == 0:
                self.mapA1()
            elif self.countUP == 1:
                pass
                #self.mapA2()
            elif self.countUP == 2:
                pass
                #self.mapA3()
            elif self.countUP == 3:
                pass
                #self.mapB1()
            elif self.countUP == 4:
                pass
                #self.mapB2()
            elif self.countUP == 5:
                pass
                #self.mapB3()
            else:
                self.end = True

            self.alarm = False
            self.countUP += 1

    def nextLevel(self):
        self.alarm = True

    def mapA1(self):
        ##############################
        #### verificar la forma de mover el mapaA1fondo
        ##############################
        self.background = pg.image.load("./Maps/mapaA1fondo.png")
        #mapInfo = None

        #Lectura de archivo json
        FileName = 'Maps\mapaA1.json'
        with open(FileName) as Information:
            #nonlocal mapInfo
            self.mapInfo = json.load(Information)
        Information.close()

        #Extraccion Objetos Json
        _door = self.mapInfo['layers'][6]['objects']
        _nails = self.mapInfo['layers'][5]['objects']
        _platforms = self.mapInfo['layers'][4]['objects']
        _walls = self.mapInfo['layers'][3]['objects']
        _enemys = self.mapInfo['layers'][2]['objects']
        _coins = self.mapInfo['layers'][1]['objects']

        #Creacion de las paredes
        print(_walls)
        for i in range(len(_walls)):
            temp = Walls((_walls[i]['x']),(_walls[i]['y']),_walls[i]['width'],_walls[i]['height'])
            self.walls.add(temp)
            #temp = Block.Bloque([(walls[i]['x']),(walls[i]['y'])],walls[i]['width'],walls[i]['height'])
            #Blocks.add(temp)

        #Creacion de las plataformas
        for i in range(len(_platforms)):
            temp = Platforms((_platforms[i]['x']),(_platforms[i]['y']),_platforms[i]['width'],_platforms[i]['height'])
            self.walls.add(temp)

        #Creacion de las pinchos
        for i in range(len(_nails)):
            temp = Nails((_nails[i]['x']),(_nails[i]['y']),_nails[i]['width'],_nails[i]['height'])
            self.nails.add(temp)

        #carga en capuchoMan las paredes para verificar por donde caminar
        self.capuchoMan.walls = self.walls
