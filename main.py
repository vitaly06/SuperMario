import pygame
from reg import *
from menu import *
from constants import *
from process import *


def main():
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    process_game(draw_level_menu(screen, menug(name_to_txt(authorization(screen))), NAME))


if __name__ == '__main__':
    main()
