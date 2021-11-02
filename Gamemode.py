import pygame
from pygame.display import update
import pygame_menu
pygame.init()

game_mode = "singleplayer"
game_diff = "easy"
LIGHT_BLUE = [17, 156, 216]
DARK_BLUE = [9, 78, 107]
WHITE = [255, 255, 255]
GRAY = [110, 110, 110]
menu = type('test', (), {})()
def create_gamemode_window(gamemode_window_size=(1080,720)):
    surface = pygame.display.set_mode((gamemode_window_size))

    global menu
    menu = pygame_menu.Menu('Gamemode', gamemode_window_size[0], gamemode_window_size[1], theme= custom_theme())

    menu.add.label('Choose Gamemode Below', max_char=-1, font_size=45, background_color=DARK_BLUE, font_color=WHITE)
    menu.add.selector('Gamemode:', [('SinglePlayer', 1), ('MultiPlayer', 2), ('Computer vs Computer', 3)], onchange=set_gamemode, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30)
    menu.add.button('Choose Difficulty', update_display, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30)
    menu.add.button('Quit', pygame_menu.events.EXIT, background_color=DARK_BLUE, font_color=WHITE, font_size=25)
    menu.mainloop(surface)

def set_gamemode(selected_item, pos):
    global game_mode
    game_mode = selected_item[0][0].lower()

def choose_difficulty(selected_item, pos):
    global game_diff
    game_diff = selected_item[0][0].lower()

from pygame_menu import Theme

def custom_theme():
    mytheme = Theme(background_color=(0, 0, 0, 0), # transparent background
                title_background_color=(4, 47, 126),
                title_font_shadow=True,
                widget_padding=20,
                widget_margin=(10,30))
    bg_img = pygame_menu.baseimage.BaseImage(
    image_path='assets\menu_background_1080x720.jpg',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
    )

    mytheme.background_color = bg_img
    return mytheme

from PONG import init_game

def start_game():
    print(game_diff)
    init_game(game_mode, game_diff)

def update_display():
    menu.clear()
    menu.add.label('Choose Difficulty Below', max_char=-1, font_size=45, background_color=DARK_BLUE, font_color=WHITE)
    menu.add.selector('Left Paddle Difficulty:', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=choose_difficulty, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add.selector('Right Paddle Difficulty:',[('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=choose_difficulty, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30,align=pygame_menu.locals.ALIGN_RIGHT)
    menu.add.button('Start Game', start_game, background_color=GRAY, font_color=WHITE, font_size=30)
    menu.add.button('Quit', pygame_menu.events.EXIT, background_color=DARK_BLUE, font_color=WHITE, font_size=25)