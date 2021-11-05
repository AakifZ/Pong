import pygame
import pygame_menu
from pygame_menu.baseimage import BaseImage
import pygame_menu.font
from PONG import init_game
from pygame_menu import Theme

pygame.init()
surface = pygame.display.set_mode((1080, 720))
font = pygame_menu.font.FONT_NEVIS
globalName = ""
game_mode = "singleplayer"
game_diff = "easy"
LIGHT_BLUE = [17, 156, 216]
DARK_BLUE = [9, 78, 107]
WHITE = [255, 255, 255]
GRAY = [110, 110, 110]

class Menu():
    def draw_main_menu():
        myimage = pygame_menu.baseimage.BaseImage(
            './assets/new.jpg',
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
            )
        mytheme = pygame_menu.themes.THEME_DARK
        mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        mytheme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
        mytheme.title_font = pygame_menu.font.FONT_NEVIS
        mytheme.background_color=(myimage)

                
        mainmenu = pygame_menu.Menu("Welcome to PONG!", 1080, 720,theme=mytheme)
        gamemode_sub_menu = Gamemode.create_gamemode_window()
        settings_sub_menu = SettingsMenu.createSettingsMenu()

        mainmenu.add.text_input("Enter name: ", default= "Player", onchange=Menu.TextVal)
        mainmenu.add.button('Play',  init_game)
        mainmenu.add.button('Game Options', gamemode_sub_menu)
        mainmenu.add.button('Settings', settings_sub_menu)
        mainmenu.add.button("Leaderboard")
        mainmenu.add.button("Quit", pygame_menu.events.EXIT)

        mainmenu.mainloop(surface)


    def TextVal(name): 
        file1 = open("name.txt","w")
        file1.write(name + " \n")

class Gamemode():

    def __init__(self) -> None:
        pass
    def create_gamemode_window(gamemode_window_size=(1080,720)):
        surface = pygame.display.set_mode((gamemode_window_size))

        global gamememode_menu
        gamememode_menu = pygame_menu.Menu('Gamemode', gamemode_window_size[0], gamemode_window_size[1], theme=Gamemode.custom_theme())
        global choose_gamemode_label
        choose_gamemode_label = gamememode_menu.add.label('Choose Gamemode Below', max_char=-1, font_size=45, background_color=DARK_BLUE, font_color=WHITE)
        global choose_gamemode_selector
        choose_gamemode_selector = gamememode_menu.add.selector('Gamemode:', [('SinglePlayer', 1), ('MultiPlayer', 2), ('Computer vs Computer', 3)], onchange=Gamemode.set_gamemode, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30)
        global next_screen_btn_gamemode
        next_screen_btn_gamemode = gamememode_menu.add.button('Choose Difficulty', Gamemode.update_display, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30)
        global first_gamemode_quit_btn
        first_gamemode_quit_btn = gamememode_menu.add.button('Quit', pygame_menu.events.EXIT, background_color=DARK_BLUE, font_color=WHITE, font_size=25)
        global first_gamemode_back_btn
        first_gamemode_back_btn = gamememode_menu.add.button('Back to Menu', pygame_menu.events.BACK,
                                            cursor=pygame_menu.locals.CURSOR_HAND)
        return gamememode_menu

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

    def start_game():
        print(game_diff)
        init_game(game_mode, game_diff)

    def update_display():
        gamememode_menu.remove_widget(choose_gamemode_label)
        gamememode_menu.remove_widget(choose_gamemode_selector)
        gamememode_menu.remove_widget(next_screen_btn_gamemode)
        gamememode_menu.remove_widget(first_gamemode_back_btn)
        gamememode_menu.remove_widget(first_gamemode_quit_btn)
        gamememode_menu.add.label('Choose Difficulty Below', max_char=-1, font_size=45, background_color=DARK_BLUE, font_color=WHITE)
        gamememode_menu.add.selector('Left Paddle Difficulty:', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=Gamemode.choose_difficulty, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30,align=pygame_menu.locals.ALIGN_LEFT)
        gamememode_menu.add.selector('Right Paddle Difficulty:',[('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=Gamemode.choose_difficulty, background_color=LIGHT_BLUE, font_color=WHITE, font_size=30,align=pygame_menu.locals.ALIGN_RIGHT)
        gamememode_menu.add.button('Start Game', Gamemode.start_game, background_color=DARK_BLUE, font_color=WHITE, font_size=30)
        gamememode_menu.add.button('Quit', pygame_menu.events.EXIT, background_color=GRAY, font_color=WHITE, font_size=25)
        gamememode_menu.add.button('Back to Menu', pygame_menu.events.BACK,
                                            cursor=pygame_menu.locals.CURSOR_HAND)

#class SettingsMenu:
global resolution
global fps
global theme
global score
score = 3
resolution = (440, 280)
fps = 30
theme = 1

class SettingsMenu():
    def createSettingsMenu( resolution = (1080,720), fps = 30):
        
        pygame.display.set_caption("Settings")
        WINDOW = pygame.display.set_mode(resolution)
        


        #Creating a custom theme
        customTheme = pygame_menu.Theme(background_color=(0,0,0,0), title_background_color=(0,255,200), 
            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
            widget_font=pygame_menu.font.FONT_BEBAS,
            title_font_color=(0,0,0),
            title_font=pygame_menu.font.FONT_BEBAS)

        

        global menu
        menu = pygame_menu.Menu("Settings", WINDOW.get_width(), WINDOW.get_height(), theme=customTheme)
        menu.add.selector("Screen Res: ", [("440x280",1), ("800x500",2), ("1200x750",3)], onchange=SettingsMenu.setResolution)
        menu.add.selector("FPS: ", [(" 30 ", 1), (" 60 ", 2), ("120", 3), ("1000", 4)], onchange=SettingsMenu.setFPS)
        menu.add.selector("Theme: ", [("Original",1), ("Mikey", 2), ("Nostalgia", 3)], onchange=SettingsMenu.setTheme)
        menu.add.selector('Score to Win: ',[('3',3),('7',7),('11',11),('15',15)], onchange=SettingsMenu.setScore)
        menu.add.button('Save', SettingsMenu.saveSettings)
        menu.add.button('Back to Menu', pygame_menu.events.BACK,
                                            cursor=pygame_menu.locals.CURSOR_HAND)
        
        return menu
        

    def setTheme(selected, value):
        global theme
        theme = value

    def setResolution(selected, value):
        global resolution
        if(value == 1):
            resolution = (440, 280)
        elif(value == 2):
            resolution = (800, 500)
        else:
            resolution = (1200, 750)
        
    def setFPS(selected, value):
        global fps
        if(value == 1):
            fps = 30
        elif(value == 2):
            fps = 60
        elif(value == 3):
            fps = 120
        else:
            fps = 1000

    def setScore(selected,value):
        global score 
        if (value == 3):
            score = 3
        elif(value == 7):
            score = 7
        elif (value == 11):
            score = 11
        else:
            score = 15
        

    def saveSettings():
        print(resolution)
        pygame.display.set_mode(resolution)
        #print(f"menu height is now {menu.get_height()}")
        pygame_menu.menu.Menu('heh', resolution[0], resolution[1])
        SettingsMenu.updateMenuSize()
        init_game(gamemode = 'computer', difficulty = 'medium', resolution= resolution, fps = fps, theme = theme, score = score)
        #updateMenuSize()
        #print(f"Changing to {resolution}")
            
    def updateMenuSize():
        menu._width = resolution[0]
        menu._height = resolution[1]
        menu.resize(resolution[0], resolution[1])
        print(menu.get_window_size())
        
        #menu._width = resolution[0]
        #menu._height = resolution[1]
        #menu._window_size = (resolution[0], resolution[1])
        
        #print(f"The menu size is from get: {menu.get_window_size()}")
        pass

Menu.draw_main_menu()