import pygame, pygame_menu
from PONG import init_game

#class SettingsMenu:
global resolution
global fps
global theme
resolution = (440, 280)
fps = 30
theme = 1
def createSettingsMenu( resolution = (440,280), fps = 30):
    

    pygame.init()
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


    menu.add.selector("Screen Res: ", [("440x280",1), ("800x500",2), ("1200x750",3)], onchange=setResolution)
    menu.add.selector("FPS: ", [(" 30 ", 1), (" 60 ", 2), ("120", 3), ("1000", 4)], onchange=setFPS)
    menu.add.selector("Theme: ", [("Original",1), ("Mikey", 2), ("Nostalgia", 3)], onchange=setTheme)
    menu.add.button('Save', saveSettings)
    
    menu.mainloop(WINDOW) 
    


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
    

def saveSettings():
    print(resolution)
    pygame.display.set_mode(resolution)
    #print(f"menu height is now {menu.get_height()}")
    pygame_menu.menu.Menu('heh', resolution[0], resolution[1])
    updateMenuSize()
    init_game(gamemode = 'singleplayer', difficulty = 'medium', resolution= resolution, fps = fps, theme = theme)
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

    
#createSettingsMenu()
#menuu = SettingsMenu()
