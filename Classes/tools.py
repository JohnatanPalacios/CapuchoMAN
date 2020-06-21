import pygame as pg
import sys


def crear_sprite(dir_sabana, dimensiones, columnas, filas=1):
    sabana = pygame.image.load(dir_sabana)
    ancho_cuadros = dimensiones[0]
    alto_cuadros = dimensiones[1]
    animacion = []
    # Recorta como fila
    if filas == 1:
        for cuadro in range(columnas):
            cuadro = sabana.subsurface(ancho_cuadros * cuadro, 0, ancho_cuadros, alto_cuadros)
            animacion.append(cuadro)
    # recorta una sabana matriz como una fila
    else:
        for fila in range(filas):
            for cuadro in range(columnas):
                cuadro = sabana.subsurface(ancho_cuadros * cuadro,alto_cuadros * fila,ancho_cuadros,alto_cuadros)
                animacion.append(cuadro)
    return animacion

def animate(currentFrame, numberFrames, address):
    if address == 0:
        return currentFrame
    elif address == 1:
        if currentFrame < (numberFrames - 1):
            currentFrame += 1
        else:
            currentFrame = 0
        return currentFrame
    elif address == -1:
        if currentFrame > 0:
            currentFrame -= 1
        else:
            currentFrame = (numberFrames - 1)
        return currentFrame
