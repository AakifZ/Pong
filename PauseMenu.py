import pygame;
import pygame_menu


resolution = (1080, 720)
pygame.init()
pygame.display.set_caption("Pause")
WINDOW = pygame.display.set_mode(resolution)
global RESUMEGAME
RESUMEGAME = pygame.USEREVENT + 2
resume_event = pygame.event.Event(RESUMEGAME, message="resumed")

global MAINMENU
MAINMENU = pygame.USEREVENT + 4
mainmenuevent = pygame.event.Event(MAINMENU, message = "menu")
def pauseMenu(width, height):
  
    customTheme = pygame_menu.Theme(background_color=(0,0,0,0), title_background_color=(0,255,200), 
        title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_color=(0,0,0),
        title_font=pygame_menu.font.FONT_BEBAS)

    pausemenu = pygame_menu.Menu("Pause", WINDOW.get_width(), WINDOW.get_height(), theme=customTheme)

    
    #RESUMEGAME = USEREVENT + 1
    def resume():
        
        pausemenu._enabled = False
        global resume_event
        pygame.event.post(resume_event)


    def mainmenu():
        pausemenu._enabled = False
        global mainmenuevent
        pygame.event.post(mainmenuevent)

    def exit():
        file = open("name.txt","r+")
        file.truncate(0)
        file.close()
        pausemenu._exit() 

    pausemenu.add.button("Resume", resume)
    pausemenu.add.button("Menu", mainmenu)
    pausemenu.add.button("Quit", exit)

    

    pausemenu.mainloop(WINDOW) 




