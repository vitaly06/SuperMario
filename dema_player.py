import pygame, sys
from constants import *

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    pygame.display.update()
    clock.tick(60)