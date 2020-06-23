# provee funcionalidad dependiente del sistema operativo
import os

# importa la librería Pygame
import pygame

# colores
black = (0, 0, 0)

def main():
    # inicializa Pygame
    pygame.init()
    # establece el tamaño de la ventana
    screen = pygame.display.set_mode((400, 400))

    # obtiene el rectángulo que ocupa la pantalla
    screen_rect = screen.get_rect()

    # obtiene el centro de la pantalla
    screen_center = screen_rect.center

    def sprite():
        animacion = []
        sabana = pygame.image.load("./Graphics/Run (78x58).png").convert_alpha()
        for c in range(7):
            c = sabana.subsurface(78*c,0,78,58)
            animacion.append(c)
        return animacion

    image = sprite()

    def animate(_frame, _numberFrames):
        if states["direction"] == 1:
            if _frame < (_numberFrames - 1):
                _frame += 1
            else:
                _frame = 0
            return _frame
        elif states["direction"] == -1:
            if _frame > 0:
                _frame -= 1
            else:
                _frame = (_numberFrames - 1)
            return _frame

    # crea un reloj
    clock = pygame.time.Clock()

    # ¿la aplicación está ejecutándose?
    is_running = True

    states = {"direction": 1}
    frame = 0
    numberFrames = len(image)

    x = 10
    velx = 0

    while is_running:
        print(states["direction"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if states["direction"] == 1:
                states["direction"] = -1
                velx += -1
                frame = animate(frame, numberFrames)
                image[frame] = pygame.transform.flip(image[frame], True, False)
            else:
                velx += -1
                frame =  animate(frame, numberFrames)
        elif keys[pygame.K_d]:
            if states["direction"] == -1:
                states["direction"] = 1
                velx += 1
                frame =  animate(frame, numberFrames)
                image[frame] = pygame.transform.flip(image[frame], True, False)
            else:
                velx += 1
                frame = animate(frame, numberFrames)
        else:
            velx = 0


        screen.fill(black)
        x += velx
        screen.blit(image[frame], [x,50])
        pygame.display.flip()
        clock.tick(20)


if __name__ == '__main__':
    main()
