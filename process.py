import pygame

import game_parametrs
from constants import *
from player import Player
from blocks import Platform, LuckyBox, BlockDie, Door


def check(name):
    all_players = dict()
    with open("players.txt", "r") as file:
        for i in file:
            i = i.split(":")
            all_players[i[0]] = int(i[1])
    return all_players[name]

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIDTH / 2, -t + HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return pygame.Rect(l, t, w, h)


def process_game(lvl, x, y):
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Super Mario')

    running = True
    clock = pygame.time.Clock()
    player = Player(x, y)
    left = right = False
    up = False
    entities = pygame.sprite.Group()
    platforms = []  # все блоки и т.д
    entities.add(player)
    level = LEVELS[lvl]  # получаем уровень игрока
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-" and lvl != 3:
                # создаем блок, заливаем его цветом и рисеум его
                pf = Platform(x, y, 'data/platform.png')
                entities.add(pf)
                platforms.append(pf)
            elif lvl == 3 and col == '-':
                pf = Platform(x, y, 'data/snow_block.jpg')
                entities.add(pf)
                platforms.append(pf)
            if col == '?':
                lb = LuckyBox(x, y)
                entities.add(lb)
                platforms.append(lb)
            if col == "*":
                bd = BlockDie(x, y, "data/dieBlock.png")
                entities.add(bd)
                platforms.append(bd)
            if col == 'l':
                bd = BlockDie(x, y, "data/lava.jpg")
                entities.add(bd)
                platforms.append(bd)
            if col == 'd':
                door = Door(x, y - 32, 'data/door.png')
                entities.add(door)
                platforms.append(door)
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0
    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту
    camera = Camera(camera_configure, total_level_width, total_level_height)
    while running:
        screen.fill(pygame.Color('green'))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            if game_parametrs.end_level:
                game_parametrs.what_to_draw = "level_menu"
                # game_parametrs.level[0] = check(game_parametrs.name)
                game_parametrs.level = (lvl, player.x, player.y)
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                game_parametrs.what_to_draw = "pause"
                print(player.x, player.y)
                game_parametrs.level = (lvl, player.x, player.y)
                return

            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
        player.update(left, right, up, platforms)
        camera.update(player)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        pygame.display.flip()
        clock.tick(FPS)

# if __name__ == '__main__':
#     process_game()
