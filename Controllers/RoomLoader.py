import pygame as pg
import sys
import json

from Classes.Platform import *
from Classes.Lava import *
from Classes.Wall import *
from Classes.Nail import *
from Classes.Coin import *
from Classes.Door import *
###   HOW TO USE TILEDMAPS
###   ASEPRITE para crear sprites

class RoomLoader:
    def __init__(self,capuchoMan,door,nails,walls,enemys,coins,lava,camera,gui):
        self.mapInfo = None
        self.countUP = 0
        self.alarm = True
        self.end = False
        self.background = None
        self.gui = gui
        self.lava = lava
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
                #self.mapA1()
                self.mapA2()
            elif self.countUP == 1:
                self.clearLevel()
                self.mapA2()
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

    def clearLevel(self):
        for w in self.walls:
            self.walls.remove(w)
        for c in self.coins:
            self.coins.remove(c)
        for n in self.nails:
            self.nails.remove(n)
        for d in self.door:
            self.door.remove(d)
        for l in self.lava:
            self.lava.remove(l)

    def mapA1(self):
        self.background = pg.image.load("./Maps/mapaA1fondo.png")
        self.camera.setup("horizontal",self.background.get_width())

        #Lectura de archivo json
        FileName = 'Maps\mapaA1.json'
        with open(FileName) as Information:
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
        self.capuchoMan.setup([_capuchoMAN[0]['x'],_capuchoMAN[0]['y']],self.walls,"horizontal")

        #establece el tiempo para jugar el mapa
        self.gui.set_time(1)

    def mapA2(self):
        self.background = pg.image.load("./Maps/mapaA2fondo.png")
        self.camera.setup("vertical",self.background.get_height())

        #Lectura de archivo json
        FileName = 'Maps\mapaA2.json'
        with open(FileName) as Information:
            self.mapInfo = json.load(Information)
        Information.close()

        #Extraccion Objetos Json
        _coins = self.mapInfo['layers'][3]['objects']
        _enemys = self.mapInfo['layers'][4]['objects']
        _walls = self.mapInfo['layers'][5]['objects']
        _platforms = self.mapInfo['layers'][6]['objects']
        _nails = self.mapInfo['layers'][7]['objects']
        _door = self.mapInfo['layers'][8]['objects']
        _lava = self.mapInfo['layers'][9]['objects']
        _capuchoMAN = self.mapInfo['layers'][10]['objects']

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

        #Creacion de la lava
        for i in range(len(_lava)):
            temp = Lava((_lava[i]['x']),(_lava[i]['y']),_lava[i]['width'],_lava[i]['height'],self.camera)
            self.lava.add(temp)
            self.walls.add(temp)

        #establece los parametros iniciales de posicion y muros del mapa
        self.capuchoMan.setup([_capuchoMAN[0]['x'],_capuchoMAN[0]['y']],self.walls,"vertical")

        #establece el tiempo para jugar el mapa
        self.gui.set_time(1.5)
