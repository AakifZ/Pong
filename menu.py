import pygame
import pygame_menu
from PONG import init_game
from Gamemode import Gamemode

pygame.init()
surface = pygame.display.set_mode((600, 400))
class menu():

        mainmenu = pygame_menu.Menu("Welcome to PONG!", 400, 300)
        mainmenu.add.button('Play', init_game)
        game = Gamemode(1080, 720, True)
        mainmenu.add.button("Game Play Options", game.create_gamemode_window())
        mainmenu.add.button("Leaderboard")
        mainmenu.add.button("Quit", pygame_menu.events.EXIT)

        mainmenu.mainloop(surface)
        #mouse movement may be issue, check key command to select options
        #'pygame.mouse' has no attribute 'get_cursor'
        #/Users/adamchaplin/Desktop/Pong/assets/menu_background_1080x720.jpg