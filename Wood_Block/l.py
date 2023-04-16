import pygame

# Inicializamos pygame
pygame.init()

# Asignamos el ancho y el alto de la pantalla
width = 1080
height = 720

# Asignamos el ancho y alto de la celda
cell_size = 0
if width < height:
    cell_size = width // 10
else:
    cell_size = height // 10

# Calcular el numero de regillas segun el alto y ancho
rows = height // cell_size
cols = width // cell_size

# Inicializamos la pantalla
screen = pygame.display.set_mode((width, height))

# Esta matriz almacenará True si un cuadrado está seleccionado y False en caso contrario.
grid = [[False for col in range(cols)] for row in range(rows)]


def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (width, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((0, 0, 0))
    draw_grid()
    pygame.display.update()
