import pygame
from main_drawings import constants


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 0
        self.x = x
        self.y = y
        self.image = pygame.image.load('../data/0.png')
        self.rect = pygame.Rect(x, y, 22, 32)  # прямоугольный объект
        self.speed_y = 0  # вертикальная скорость
        self.onGround = False  # находится ли игрок на земле

    def update(self, left, right, up, platforms):
        if up:
            print(1)
            if self.onGround:
                print(2)
                self.speed_y = -constants.JUMP_POWER
        if left:
            self.speed = -constants.SPEED
        if right:
            self.speed = constants.SPEED
        if not (left or right):
            self.speed = 0
        if not self.onGround:
            self.speed_y += constants.GRAVITY
        self.rect.x += self.speed
        self.collide(self.speed, 0, platforms)
        self.rect.y += self.speed_y
        self.collide(0, self.speed_y, platforms)
        self.onGround = False

    def collide(self, speed_x, speed_y, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if speed_x > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо
                if speed_x < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево
                if speed_y > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.speed_y = 0  # и энергия падения пропадает
                if speed_y < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.speed_y = 0  # и энергия прыжка пропадает
