import pygame as pg
import sys

##########################################################
#  CUIDADO, SE DEBE CREAR LA IMAGEN CUANDO ESTA PARADO  #
#########################################################

class Animation:
    def __init__(self,object,jump,address,size,columns,rows=1,num=0):
        self.object = object
        self.jump = pg.image.load(jump).convert_alpha()
        self.animations = self.build(address,size,columns,rows,num)
        self.frame = 0
        self.numberFrames = len(self.animations[0])

        self.object.image = self.animations[0][0]
        self.object.rect = self.object.image.get_rect()

    def update(self):
        if self.object.states["jump"] or self.object.states["inAir"]:
            self.object.image = self.jump
        else:
            self.animate()
            self.object.image = self.animations[self.aux()][self.frame]

    def build(self,address,size,columns,rows,num):
        sabana = pg.image.load(address).convert_alpha()
        animation = []
        right = []
        left = []
        i = 0
        # Recorta como fila
        if rows == 1:
            if not num:
                for i in range(columns):
                    image = sabana.subsurface(size[0] * i, 0, size[0], size[1])
                    right.append(image)
                    image = pg.transform.flip(image, True, False)
                    left.append(image)
            else:
                for i in num:
                    image = sabana.subsurface(size[0] * i, 0, size[0], size[1])
                    right.append(image)
                    image = pg.transform.flip(image, True, False)
                    left.append(image)
        # recorta una sabana matriz como una fila
        else:
            if not num:
                for fila in range(rows):
                    for i in range(columns):
                        image = sabana.subsurface(size[0] * i,size[1] * fila,size[0],size[1])
                        right.append(image)
                        image = pg.transform.flip(image, True, False)
                        left.append(image)
            else:
                for fila in range(rows):
                    for i in range(columns):
                        if i < num:
                            image = sabana.subsurface(size[0] * i,size[1] * fila,size[0],size[1])
                            right.append(image)
                            image = pg.transform.flip(image, True, False)
                            left.append(image)
                        i += 1
        animation.append(left)
        animation.append(right)
        return animation

    def animate(self):
        if self.object.states["direction"] == 1:
            if self.frame < (self.numberFrames - 1):
                self.frame += 1
            else:
                self.frame = 0
        elif self.object.states["direction"] == -1:
            if self.frame > 0:
                self.frame -= 1
            else:
                self.frame = (self.numberFrames - 1)

    def aux(self):
        if self.object.states["direction"] == -1:
            return 0
        else:
            return 1
