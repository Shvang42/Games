import pygame
import sys
from pygame.math import Vector2

white = (255, 255, 255)
grass_green = (175, 215, 70)
red = (255, 0, 0)

# creating a class in order to generate the "fruit" the snake will eat
class Fruit:
    def __init__(self, color):
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x, self.y)
        self.col = color
        
        # create an x and y position and vector
        
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, 
                                 cell_size, cell_size)
        pygame.draw.rect(screen, self.col, fruit_rect)
        # draw a square

class Apple(Fruit):
        def __init__(self, Color_Red):
            super().__init__(Color_Red)
             
# initialize basic game components, such as the display screen, FPS,
# and a test surface, along with the "grid" look for the game
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, 
                                  cell_size * cell_number))
clock = pygame.time.Clock()

apple = Apple(red)

# while loop allows the game to continuously run unless
# the EXIT button on the window is hit
while True:
    # the event is used to end the game  on EXIT click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(grass_green)
    apple.draw_fruit()
    pygame.display.update()
    clock.tick(30)
