import pygame
import game_parametrs
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
        self.rect = pygame.Rect(x, y, 22, 32)
        self.speed_y = 0
        self.onGround = False  # нахождение на земле
        self.image.set_colorkey(pygame.Color(COLOR))  # прозрачный фон
        # right
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        # left
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))

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
            if up:
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
            if pygame.sprite.collide_rect(self, p):  # пересечение платформы и игрока
                if speed_x > 0:
                    self.rect.right = p.rect.left
                if speed_x < 0:
                    self.rect.left = p.rect.right
                if speed_y > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.speed_y = 0
                if speed_y < 0:
                    self.rect.top = p.rect.bottom
                    self.speed_y = 0
                if isinstance(p, blocks.BlockDie):  # пересечение с колючками
                    self.die()

                elif isinstance(p, blocks.Door):  # дверь для прохождения уровня
                    level = game_parametrs.level[0]
                    print(level)
                    all_players = dict()
                    with open("players.txt", "r+") as file:
                        for i in file:
                            i = i.split(":")
                            all_players[i[0]] = int(i[1])
                    if level < all_players[game_parametrs.name]:
                        # game_parametrs.what_to_draw = "level_menu"
                        pass
                    else:
                        all_players[game_parametrs.name] += 1
                        with open("players.txt", "w") as file:
                            for i in all_players:
                                file.write(f"{i}: {all_players[i]} \n")
                        # game_parametrs.what_to_draw = "level_menu"
                    game_parametrs.end_level = True

    def die(self):
        # pygame.time.wait(500)
        # self.teleporting(self.x, self.y)
        game_parametrs.game_over = True

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
