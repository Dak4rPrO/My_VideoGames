import pygame
import random

# Inicializar pygame
pygame.init()

# Definir tamaño de pantalla
screen_width = 600
screen_height = 800

# Crear ventana
screen = pygame.display.set_mode((screen_width, screen_height))

# Definir tamaño de bloque de cuadricula
cell_width = 40
cell_height = 40

# Definir el tamaño de la cuadricula
rows = screen_height // cell_height
cols = screen_width // cell_width

# Definir colores
white = (255, 255, 255)
brown = (139, 69, 19)
beige = (222, 184, 135)

# Definir clase para los bloques
class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface(screen_width, screen_height)
        self.image.fill(color)
        self.rect = self.image.get_rect()


# Bucle principal del juego
def draw_grid():
    for x in range(0, screen_width, cell_width):
        pygame.draw.line(screen, (beige), (x, 0), (x, screen_height))
    for y in range(0, screen_height, cell_height):
        pygame.draw.line(screen, (beige), (0, y), (screen_width, y))

# Manejar eventos
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((150, 113, 23))
    draw_grid()
    pygame.display.update()
    
pygame.quit()