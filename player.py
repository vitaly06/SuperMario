import pygame
from constants import *
import pyganim
import blocks


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 0
        self.x = x
        self.y = y
        self.image = pygame.image.load('data/0.png')
        self.rect = pygame.Rect(x, y, 22, 32)  # прямоугольный объект
        self.speed_y = 0  # вертикальная скорость
        self.onGround = False  # находится ли игрок на земле
        self.image.set_colorkey(pygame.Color(COLOR))  # делаем фон прозрачным
        #        Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:
                self.speed_y = -JUMP_POWER
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))
        if left:
            self.speed = -SPEED
            self.image.fill(pygame.Color(COLOR))
            if up:  # для прыжка влево есть отдельная анимация
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))
        if right:
            self.speed = SPEED
            self.image.fill(pygame.Color(COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))
        if not (left or right):
            self.speed = 0
            if not up:
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))
        if not self.onGround:
            self.speed_y += GRAVITY
        self.onGround = False
        self.rect.x += self.speed
        self.collide(self.speed, 0, platforms)
        self.rect.y += self.speed_y
        self.collide(0, self.speed_y, platforms)

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
                if isinstance(p, blocks.BlockDie):  # если пересакаемый блок - blocks.BlockDie
                    self.die()  # умираем
                elif isinstance(p, blocks.Door):
                    print('COOL')  # ДЁМА СЮДА

    def die(self):
        pygame.time.wait(500)
        self.teleporting(self.x, self.y)  # перемещаемся в начальные координаты

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
