import pygame
from constants import *
from player import Player
from blocks import Platform, LuckyBox


def process_game(lvl):
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Super Mario')

    running = True
    clock = pygame.time.Clock()
    player = Player(50, 50)
    left = right = False
    up = False
    entities = pygame.sprite.Group()
    platforms = []  # все блоки и т.д
    entities.add(player)
    level = [
        "--------------------------------",
        "-                              -",
        "-                              -",
        "-                              -",
        "-            --                -",
        "-                              -",
        "--                             -",
        "-                              -",
        "-                        -?-   -",
        "-                              -",
        "-                              -",
        "-      ---                     -",
        "-                              -",
        "-   ----?------                -",
        "-                             --",
        "-                -           ---",
        "-                   --      ----",
        "-                          -----",
        "--------------------------------"]
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                # создаем блок, заливаем его цветом и рисеум его
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == '?':
                lb = LuckyBox(x, y)
                entities.add(lb)
                platforms.append(lb)
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0
    while running:
        screen.fill(pygame.Color('green'))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
        player.update(left, right, up, platforms)
        entities.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


# if __name__ == '__main__':
#     process_game()
