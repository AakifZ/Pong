import pygame, pygame_menu


class SettingsMenu:
    global resolution
    global fps
    resolution = (440, 280)
    fps = 30
    def __init__(self, resolution = (440,280), fps = 30):
        

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
        menu.add.selector("FPS: ", [(" 30 ", 1), (" 60 ", 2), ("120", 3)], onchange=setFPS)
        menu.add.button('Save', saveSettings)
        
        menu.mainloop(WINDOW) 
        
 



def setResolution(selected, value):
    global resolution
    if(value == 1):
        resolution = (440, 280)
    elif(value == 2):
        resolution = (800, 500)
    else:
        resolution = (1200, 750)
    
def setFPS(selected, value):
    if(value == 1):
        fps = 30
    elif(value == 2):
        fps = 60
    else:
        fps = 120

def saveSettings():
    print(resolution)
    pygame.display.set_mode(resolution)
    #print(f"menu height is now {menu.get_height()}")
    pygame_menu.menu.Menu('heh', resolution[0], resolution[1])
    updateMenuSize()
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

    

#menuu = SettingsMenu()
