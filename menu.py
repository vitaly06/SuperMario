import pygame

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
    #if key[pygame.K_RETURN]:
    #    if pos == 'up':  # нажатие кнопки играть
     #       enter = True
     #   elif pos == 'down':  # нажатие кнопки выход
     #       pygame.quit()
     #       exit()
    screen.blit(screen2, (0, 0))
    screen.blit(text1, (text_x1, text_y1))
    screen.blit(text2, (text_x2, text_y2))
    screen.blit(title, (title_x1, title_y1))


if __name__ == '__main__':
    menug(1)
