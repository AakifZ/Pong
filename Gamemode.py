import pygame
pygame.init()
from PONG import init_game

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
LIGHT_BLUE = [17, 156, 216]
DARK_BLUE = [9, 78, 107]
GRAY = [110, 110, 110]
mainClock = pygame.time.Clock()

class Gamemode:
    """Gamemode class used for organizing the gamemode window's attributes and styling"""
    def __init__(self, screen_width, screen_height, is_active):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.is_active = is_active
        
    def create_gamemode_window(self):
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        screen_rect = screen.get_rect()
        screen_center = screen_rect.center
 
        pygame.display.set_caption('Gamemode')
        background_image = pygame.image.load("./assets/menu_background1_65.jpg")

        choose_gamemode_btn = pygame.Rect(0, 0, screen.get_width() / 3, 50)
        single_player_btn = pygame.Rect(0, 0, screen.get_width() / 4, 50)
        multi_player_btn = pygame.Rect(0, 0, screen.get_width() / 4, 50)
        computer_player_btn = pygame.Rect(0, 0, screen.get_width() / 4, 50)
        #TODO: Fix button position on different screen sizes
        difficulty_btn = pygame.Rect(self.screen_width- 180, self.screen_height-60, screen.get_width() / 4, 50)
        buttons = [choose_gamemode_btn, single_player_btn, multi_player_btn, computer_player_btn]
        
        while self.is_active:
            screen.blit(background_image, (0,0))

            pygame.draw.rect(screen, GRAY, difficulty_btn, border_radius=15)
            draw_text("Choose Difficulty", 25, WHITE, screen, difficulty_btn.x, difficulty_btn.y, difficulty_btn.center)
            self.draw_gamemode_btns(screen, buttons, screen_center)

            mx, my = pygame.mouse.get_pos()
            if choose_gamemode_btn.collidepoint((mx, my)):
                if click:
                    print("button1 click!")
            if choose_gamemode_btn.collidepoint((mx, my)):
                if click:
                    print("Game Started!")
                    init_game()

    
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            mainClock.tick(60)

    def draw_gamemode_btns(self, screen, buttons, screen_center):
        yPos = screen.get_height() / 6
        options = ["SinglePlayer", "MultiPlayer", "AI vs. AI"]
        pos = 0
        for button in buttons:
            button.center = screen_center
            button.y=yPos
            if button.width == screen.get_width() / 3:
                pygame.draw.rect(screen, DARK_BLUE, button, border_radius=15)
                draw_text("Choose Gamemode", 25, WHITE, screen, button.x, button.y, button.center)
            else:
                pygame.draw.rect(screen, LIGHT_BLUE, button, border_radius=15)
                draw_text(options[pos], 25, WHITE, screen, button.x, button.y, button.center)
                pos+=1
            yPos+=screen.get_height() / 5
        
    def draw_difficulty_btns(self, screen, buttons, screen_center):
        yPos = screen.get_height() / 6
        options = ["Easy", "Medium", "Hard"]
        pos = 0
        for button in buttons:
            button.center = screen_center
            button.y=yPos
            if button.width == screen.get_width() / 3:
                pygame.draw.rect(screen, DARK_BLUE, button, border_radius=15)
                draw_text("Choose Difficulty", 25, WHITE, screen, button.x, button.y, button.center)
            else:
                pygame.draw.rect(screen, LIGHT_BLUE, button, border_radius=15)
                draw_text(options[pos], 25, WHITE, screen, button.x, button.y, button.center)
                pos+=1
            yPos+=screen.get_height() / 5

def draw_text(text, font_size, color, surface, x, y, center):
    font = pygame.font.SysFont(None, font_size)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    textrect.center = center;
    surface.blit(textobj, textrect)

gamemode = Gamemode(672, 378, True)
gamemode.create_gamemode_window()