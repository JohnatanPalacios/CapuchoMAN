import pygame as pg
import sys
import json

from Classes.Wall import *
from Classes.Platform import *
from Classes.Nail import *
from Classes.Coin import *
from Classes.Door import *
###   HOW TO USE TILEDMAPS
###   ASEPRITE para crear sprites

class RoomLoader:
    def __init__(self,capuchoMan,door,nails,walls,enemys,coins,camera):
        self.mapInfo = None
        self.countUP = 0
        self.alarm = True
        self.end = False
        self.background = None
        self.capuchoMan = capuchoMan
        self.camera = camera
        self.door = door
        self.nails = nails
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

    def nextLevel(self,openDoor):
        if openDoor:
            self.alarm = True

    def mapA1(self):
        self.background = pg.image.load("./Maps/mapaA1fondo.png")
        #mapInfo = None

        #Lectura de archivo json
        FileName = 'Maps\mapaA1.json'
        with open(FileName) as Information:
            #nonlocal mapInfo
            self.mapInfo = json.load(Information)
        Information.close()

        #Extraccion Objetos Json
        _coins = self.mapInfo['layers'][1]['objects']
        _enemys = self.mapInfo['layers'][2]['objects']
        _walls = self.mapInfo['layers'][3]['objects']
        _platforms = self.mapInfo['layers'][4]['objects']
        _nails = self.mapInfo['layers'][5]['objects']
        _door = self.mapInfo['layers'][6]['objects']
        _capuchoMAN = self.mapInfo['layers'][7]['objects']

        #Creacion de las monedas
        for i in range(len(_coins)):
            temp = Coin((_coins[i]['x']),(_coins[i]['y']),_coins[i]['width'],_coins[i]['height'],self.camera)
            self.coins.add(temp)
        '''
        #Creacion de los enemigos
        for i in range(len(_enemys)):
            temp = Enemy((_enemys[i]['x']),(_enemys[i]['y']),_enemys[i]['width'],_enemys[i]['height'],self.camera)
            self.enemys.add(temp)
        '''
        #Creacion de las paredes
        for i in range(len(_walls)):
            temp = Wall((_walls[i]['x']),(_walls[i]['y']),_walls[i]['width'],_walls[i]['height'],self.camera)
            self.walls.add(temp)
            #temp = Block.Bloque([(walls[i]['x']),(walls[i]['y'])],walls[i]['width'],walls[i]['height'])
            #Blocks.add(temp)

        #Creacion de las plataformas
        for i in range(len(_platforms)):
            temp = Platform((_platforms[i]['x']),(_platforms[i]['y']),_platforms[i]['width'],_platforms[i]['height'],self.camera)
            self.walls.add(temp)

        #Creacion de las pinchos
        for i in range(len(_nails)):
            temp = Nail((_nails[i]['x']),(_nails[i]['y']),_nails[i]['width'],_nails[i]['height'],self.camera)
            self.nails.add(temp)

        #Creacion de las puertas
        for i in range(len(_door)):
            temp = Door((_door[i]['x']),(_door[i]['y']),_door[i]['width'],_door[i]['height'],self.camera)
            self.door.add(temp)

        #establece los parametros iniciales de posicion y muros del mapa
        self.capuchoMan.setLevelParameters([_capuchoMAN[0]['x'],_capuchoMAN[0]['y']],self.walls)
