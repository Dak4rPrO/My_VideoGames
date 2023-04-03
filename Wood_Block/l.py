import pygame

pygame.init()

width = 600
height = 800

screen = pygame.display.set_mode((width, height))

cell_width = 50
cell_height = 50

rows = height // cell_height
cols = width // cell_width

def draw_grid():
    for x in range(0, width, cell_width):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, height))
    for y in range(0, height, cell_height):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (width, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0))
    
    draw_grid()
    
    pygame.display.update()
    
pygame.quit()
