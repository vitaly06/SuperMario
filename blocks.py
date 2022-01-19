from constants import *
import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, place):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(place)
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class BlockDie(Platform):
    def __init__(self, x, y, place):
        Platform.__init__(self, x, y, place)
        self.image = pygame.image.load(place)


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, place):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(place)
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT + 32)
