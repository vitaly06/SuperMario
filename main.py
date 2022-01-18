import pygame
from funks_to_draw import *
from constants import *
from process import *
import game_parametrs


def name_to_txt(name):
    all_players = dict()
    with open("players.txt", "r+") as file:
        for i in file:
            i = i.split(":")
            all_players[i[0]] = int(i[1])
        if name not in all_players and name:
            file.write(f"{name}: 1\n")
            all_players[name] = 1
    game_parametrs.level = (all_players[name], 50, 50)


def main():
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Super Mario')
    while True:
        if game_parametrs.what_to_draw == "start":
            authorization(screen)
        elif game_parametrs.what_to_draw == "level_menu":
            draw_level_menu(screen, game_parametrs.level[0], game_parametrs.name)
        elif game_parametrs.what_to_draw == "level":
            process_game(game_parametrs.level[0], game_parametrs.level[1], game_parametrs.level[2])
        elif game_parametrs.what_to_draw == "pause":
            pause(game_parametrs.level[0], game_parametrs.level[1], game_parametrs.level[2])
            # check


if __name__ == '__main__':
    main()
