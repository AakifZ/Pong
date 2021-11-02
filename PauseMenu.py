import pygame
import pygame_menu


resolution = (1080, 720)
pygame.init()
pygame.display.set_caption("Pause")
WINDOW = pygame.display.set_mode(resolution)
global RESUMEGAME
RESUMEGAME = pygame.USEREVENT + 2
resume_event = pygame.event.Event(RESUMEGAME, message="resumed")

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


    pausemenu.add.button("Resume", resume)
    #pausemenu.add.button("Main Menu")
    pausemenu.add.button("Quit", pausemenu._exit)

    

    pausemenu.mainloop(WINDOW) 




