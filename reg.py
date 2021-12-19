import pygame
import os
import sys

pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)


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
    font = pygame.font.Font('fonts/SuperMario256.ttf', 40)
    font1 = pygame.font.Font('fonts/SuperMario256.ttf', 25)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
                    return name
                elif event.key == pygame.K_v:
                    name += "v"
                elif event.key == pygame.K_i:
                    name += "i"

        text = font.render(name, True, (0, 0, 0))
        description = font1.render("Напишите свой ник", True, (0, 0, 0))
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
        pygame.draw.rect(screen, (0, 0, 0), (text_x - 10, text_y - 10,
                                             text_w + 20, text_h + 20), 3)
        pygame.display.flip()
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
    return all_players[name]


def draw_level_menu(screen, level, name):
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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            j = 0
            for i in all_icons:
                if event.type == pygame.MOUSEBUTTONDOWN and \
                        i.rect.collidepoint(event.pos):
                    print(j + 1)
                    return
                j += 1
        all_icons.draw(screen)
        pygame.display.flip()
    pygame.quit()

# draw_level_menu(screen, name_to_txt(authorization(screen)), "ggg")
