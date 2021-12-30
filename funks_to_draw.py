import pygame
import os
import sys
import game_parametrs

pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
all_icons = pygame.sprite.Group()
pygame.display.set_caption('Super Mario')


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


image = load_image("enter_photo.jpg")


def authorization(screen):
    global image
    name = ""
    g = "Введите всой ник"
    font = pygame.font.Font('fonts/SuperMario256.ttf', 40)
    font1 = pygame.font.Font('fonts/SuperMario256.ttf', 25)
    running = True
    while running:
        for event in pygame.event.get():
            g += ""
            if event.type == pygame.QUIT:
                running = False
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    name += "a"
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_b:
                    name += "b"
                elif event.key == pygame.K_c:
                    name += "c"
                elif event.key == pygame.K_d:
                    name += "d"
                elif event.key == pygame.K_e:
                    name += "e"
                elif event.key == pygame.K_f:
                    name += "f"
                elif event.key == pygame.K_j:
                    name += "j"
                elif event.key == pygame.K_k:
                    name += "k"
                elif event.key == pygame.K_l:
                    name += "l"
                elif event.key == pygame.K_g:
                    name += "g"
                elif event.key == pygame.K_m:
                    name += "m"
                elif event.key == pygame.K_n:
                    name += "n"
                elif event.key == pygame.K_o:
                    name += "o"
                elif event.key == pygame.K_p:
                    name += "p"
                elif event.key == pygame.K_q:
                    name += "q"
                elif event.key == pygame.K_r:
                    name += "r"
                elif event.key == pygame.K_s:
                    name += "s"
                elif event.key == pygame.K_t:
                    name += "t"
                elif event.key == pygame.K_u:
                    name += "u"
                elif event.key == pygame.K_w:
                    name += "w"
                elif event.key == pygame.K_h:
                    name += "h"
                elif event.key == pygame.K_x:
                    name += "x"
                elif event.key == pygame.K_y:
                    name += "y"
                elif event.key == pygame.K_z:
                    name += "z"
                elif event.key == pygame.K_SPACE:
                    name += " "
                elif event.key == pygame.K_RETURN:
                    screen.fill((0, 0, 0))
                    game_parametrs.name = name
                    name_to_txt(name)
                    game_parametrs.what_to_draw = "level_menu"
                    return
                elif event.key == pygame.K_v:
                    name += "v"
                elif event.key == pygame.K_i:
                    name += "i"

        text = font.render(name, True, (0, 0, 0))
        description = font1.render("Enter your name\n"
                                   "And press 'Enter' button ", True, (0, 0, 0))
        x = width // 2 - description.get_width() // 2
        y = 150
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.fill((0, 0, 0))
        image1 = pygame.transform.scale(image, (1000, 600))
        screen.blit(image1, (0, 0))
        screen.blit(text, (text_x, text_y))
        screen.blit(description, (x, y))
        if text_w <= 300:
            pygame.draw.rect(screen, (0, 0, 0), (350, text_y - 10,
                                                 300, text_h + 20), 3)
        else:
            pygame.draw.rect(screen, (0, 0, 0), (text_x - 10, text_y - 10,
                                                text_w + 20, text_h + 20), 3)
        pygame.display.update()
    pygame.quit()


def name_to_txt(name):
    all_players = dict()
    with open("players.txt", "r+") as file:
        for i in file:
            i = i.split(":")
            all_players[i[0]] = int(i[1])
        if name not in all_players and name:
            file.write(f"{name}: 1\n")
            all_players[name] = 1
    game_parametrs.level = all_players[name]


def draw_levels(screen, level):
    global all_icons
    k = 100
    x = 200
    n = 75
    y = 150
    m = 150
    screen.fill((255, 255, 255))
    image = pygame.transform.scale(load_image("nebo.jpg"), (1000, 600))
    screen.blit(image, (0, 0))
    all_icons = pygame.sprite.Group()
    font = pygame.font.Font('fonts/SuperMario256.ttf', 15)
    for i in range(3):
        text = font.render(f"level {i + 1}", True, (0, 0, 0))
        if level >= i + 1:
            icon = pygame.sprite.Sprite()
            icon.image = pygame.transform.scale(load_image("level_icon.jpg"), (x, y))
            icon.rect = icon.image.get_rect()
            all_icons.add(icon)
            icon.rect.x = k + (k * i) + (x * i)
            icon.rect.y = n
        else:
            icon = pygame.sprite.Sprite()
            icon.image = pygame.transform.scale(load_image("lock.jpg"), (x, y))
            icon.rect = icon.image.get_rect()
            all_icons.add(icon)
            icon.rect.x = k + (k * i) + (x * i)
            icon.rect.y = n
        screen.blit(text, (k + (k * i) + (x * i), n + 10))
    for i in range(3):
        text = font.render(f"level {i + 4}", True, (0, 0, 0))
        if level >= i + 4:
            icon = pygame.sprite.Sprite()
            icon.image = pygame.transform.scale(load_image("level_icon.jpg"), (x, y))
            icon.rect = icon.image.get_rect()
            all_icons.add(icon)
            icon.rect.x = k + (k * i) + (x * i)
            icon.rect.y = n + m + y
        else:
            icon = pygame.sprite.Sprite()
            icon.image = pygame.transform.scale(load_image("lock.jpg"), (x, y))
            icon.rect = icon.image.get_rect()
            all_icons.add(icon)
            icon.rect.x = k + (k * i) + (x * i)
            icon.rect.y = n + m + y
        screen.blit(text, (k + (k * i) + (x * i), n + m + y + 10))


def draw_level_menu(screen, level, name):
    global all_icons
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit(0)
            j = 0
            for i in all_icons:
                if event.type == pygame.MOUSEBUTTONDOWN and \
                        i.rect.collidepoint(event.pos) and event.button == 1:
                    game_parametrs.level = j + 1
                    game_parametrs.what_to_draw = "level"
                    return
                j += 1
        draw_levels(screen, level)
        all_icons.draw(screen)
        pygame.display.flip()
    pygame.quit()


pos = 'up'  # где находится стрелка
bg = pygame.image.load('data/bg_menu.jpg')  # фон меню
text_x1, textwidth1, textheight1, text_y1 = 0, 0, 0, 0  # координаты текста
text_x2, textwidth2, textheight2, text_y2 = 0, 0, 0, 0
enter = False


def menug(lvl):
    global text_x1, text_x2, text_y2, text_y1, textheight2, textheight1, textwidth1, textwidth2, enter
    pygame.init()
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('меню')
    running = True
    clock = pygame.time.Clock()
    fps = 60
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if text_x1 <= event.pos[0] <= text_x1 + textwidth1 and text_y1 <= event.pos[1] <= text_y1 + textheight1:
                    return lvl  # начать игру
                if text_x2 <= event.pos[0] <= text_x2 + textwidth2 and text_y2 <= event.pos[1] <= text_y2 + textheight2:
                    exit()
            if enter:
                enter = False
                return lvl
        draw(screen, width, height, lvl)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


def draw(screen, width, height, lvl):
    global pos, bg, enter
    global text_x1, text_x2, textwidth1, textwidth2, textheight1, textheight2, text_y2, text_y1
    # текст
    font = pygame.font.Font('fonts/SuperMario256.ttf', 50)
    text1 = font.render('START', True, pygame.Color('black'))
    text2 = font.render('EXIT', True, pygame.Color('black'))
    text_x1 = width // 2 - text1.get_width() // 2
    text_y1 = height // 3
    text_x2 = width // 2 - text2.get_width() // 2
    text_y2 = height // 1.5
    title_font = pygame.font.Font('fonts/SuperMario256.ttf', 100)
    title = font.render('SUPER MARIO', True, pygame.Color('black'))
    title_x1 = width // 2 - title.get_width() // 2
    title_y1 = height // 15
    textwidth1 = text1.get_width()
    textwidth2 = text2.get_width()
    textheight1, textheight2 = text1.get_height(), text2.get_height()

    # работа со стрелочкой
    arr = pygame.image.load('data/red_arrow.png')
    key = pygame.key.get_pressed()
    screen2 = pygame.display.set_mode((width, height))
    screen2.blit(bg, (0, 0))
    if key[pygame.K_DOWN]:
        pos = 'down'
    if key[pygame.K_UP]:
        pos = 'up'
    if pos == 'up':
        screen2.blit(arr, (text_x1 + text1.get_width() + 5, text_y1))
    elif pos == 'down':
        screen2.blit(arr, (text_x2 + text2.get_width() + 5, text_y2))

    screen.blit(screen2, (0, 0))
    screen.blit(text1, (text_x1, text_y1))
    screen.blit(text2, (text_x2, text_y2))
    screen.blit(title, (title_x1, title_y1))


