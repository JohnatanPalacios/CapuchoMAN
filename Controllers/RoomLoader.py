import pygame as pg
import sys


jugadores = pg.sprite.Group()
enemigos = pg.sprite.Group()
bloques = pg.sprite.Group()
bonus = pg.sprite.Group()
molotovs = pg.sprite.Group()


#Lectura de archivo json
FileName= 'Maps\mapaA1.json'
with open(FileName) as Information:
    MapInfo=json.load(Information)
Information.close()

#Extraccion Objetos Json
CollisionsA = MapInfo['layers'][13]['objects']
PlatformsA = MapInfo['layers'][14]['objects']
DiamondsPosA = MapInfo['layers'][10]['objects']
ApplesPosA = MapInfo['layers'][11]['objects']
CoinsPosA = MapInfo['layers'][12]['objects']
DoorA = MapInfo['layers'][15]['objects']
Enemys1A = MapInfo['layers'][16]['objects']

#Creacion de las paredes
    for i in range(len(Constants.CollisionsA)):
        Temporal = Block.Bloque([(Constants.CollisionsA[i]['x']),(Constants.CollisionsA[i]['y'])],Constants.CollisionsA[i]['width'],Constants.CollisionsA[i]['height'])
        Blocks.add(Temporal)

###   HOW TO USE TILEDMAPS
###   ASEPRITE
