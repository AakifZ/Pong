import pygame;
import pygame_menu
import PONG

resolution = (1080, 720)
pygame.init()
pygame.display.set_caption("Play Again?")
WINDOW = pygame.display.set_mode(resolution)
global PLAYAGAIN
PLAYAGAIN = pygame.USEREVENT + 3
again_event = pygame.event.Event(PLAYAGAIN, message="gameended")

def playagain(winner, width, height, gamemode = 'singleplayer', difficulty = 'hard', resolution = (1080, 720), fps = 60, theme = 1, score = 11, paddle_size = "Medium"):
  
    customTheme = pygame_menu.Theme(background_color=(0,0,0,0), title_background_color=(0,255,200), 
        title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_color=(0,0,0),
        title_font=pygame_menu.font.FONT_BEBAS)

    if(winner == "AI"):
        customTheme.title_background_color = (255, 0, 0)
    else:
        customTheme.title_background_color = (0,255, 0 )

    playagainmenu = pygame_menu.Menu("Play Again?", WINDOW.get_width(), WINDOW.get_height(), theme=customTheme)

    
    #RESUMEGAME = USEREVENT + 1
    def again():
        PONG.init_game(gamemode, difficulty, resolution, fps, theme, score, paddle_size)
        playagainmenu._enabled = False

    def mainMenu():
        playagainmenu._enabled = False
    
    def exit():
        file = open("name.txt","r+")
        file.truncate(0)
        file.close()
        playagainmenu._exit() 
        
    fontsize = int(resolution[0] * 0.15)
    if(resolution[0] < 500):
        fontsize = 55
   

    #font_size= 200
    #font_size= 100
    if(winner == "AI"):
        playagainmenu.add.label(f"{winner} wins!", font_size =fontsize, font_color=(255, 0,0))
    else: 
        playagainmenu.add.label(f"{winner} wins!", font_size =fontsize, font_color=(0,255,0))

    playagainmenu.add.button("Play Again", again)
    playagainmenu.add.button("Menu", mainMenu)
    playagainmenu.add.button("Quit", exit)

    

    playagainmenu.mainloop(WINDOW) 



