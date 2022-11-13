import pygame
import sys

white = (255, 255, 255)

# creating a class in order to generate the "fruit" the snake will eat
class APPLE:
    def __init__(self):
        self.x = 5
        self.y = 4

        # create an x and y position
        # draw a square


# initialize basic game components, such as the display screen, FPS,
# and a test surface, along with the "grid" look for the game
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 200))

# colors for the display screen
screen.fill((175, 215, 70))

# while loop allows the game to continuously run unless
# the EXIT button on the window is hit
while True:
    # the event is used to end the game  on EXIT click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175, 215, 70))
    pygame.display.update()
    clock.tick(30)
