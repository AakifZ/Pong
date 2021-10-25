import pygame
from PONG import init_game
from Button import Button

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
LIGHT_BLUE = [17, 156, 216]
DARK_BLUE = [9, 78, 107]
GRAY = [110, 110, 110]
mainClock = pygame.time.Clock()

class Gamemode:
    """Gamemode class used for organizing the gamemode window's attributes and styling"""
    def __init__(self, screen_width, screen_height, is_active, gamemode="singleplayer", difficulty="easy"):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.is_active = is_active
        self.gamemode = gamemode
        self.difficulty = difficulty
        
    def create_gamemode_window(self):
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        screen_rect = screen.get_rect()
        screen_center = screen_rect.center
 
        pygame.display.set_caption('Gamemode')
        background_image = pygame.image.load("./assets/menu_background_1080x720.bmp")

        button_dictionary = self.get_buttons(screen)

        gamemode_buttons = [button_dictionary["choose_gamemode_btn"], button_dictionary["difficulty_btn"], button_dictionary["single_player_btn"],button_dictionary["multi_player_btn"],button_dictionary["computer_player_btn"]]
        difficulty_buttons = [button_dictionary["choose_gamemode_btn"], button_dictionary["play_btn"], button_dictionary["easy_btn"], button_dictionary["med_btn"], button_dictionary["hard_btn"]]
        
        click = False
        while self.is_active:
            screen.blit(background_image, (0,0))
            if not button_dictionary["difficulty_btn"].clicked:
                self.draw_btns(screen, gamemode_buttons, screen_center, False)
            else:
                self.draw_btns(screen, difficulty_buttons, screen_center,True)

            mx, my = pygame.mouse.get_pos()
            self.checkMouseCollision(mx, my, button_dictionary, click)
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

            if button_dictionary["play_btn"].clicked:
                init_game(self.gamemode, self.difficulty)

    def draw_btns(self, screen, buttons, screen_center, next_screen):
        yPos = screen.get_height() / 6
        options = []
        title = ""
        next_text = ""
        gamemode_options = ["SinglePlayer", "MultiPlayer", "AI vs. AI"]
        difficulty_options = ["Easy", "Medium", "Hard", ]

        if next_screen:
            options = difficulty_options
            title = "Choose difficulty below"
            next_text = "Play!"
        else:
            options = gamemode_options
            title= "Choose gamemode below"
            next_text = "Choose Difficulty"
        pos = 0
        for button in buttons:
            if button.button_type == "title_button":
                button.rect.center = screen_center
                button.rect.y=yPos
                button.draw_button(screen)
                draw_text(title, 25, WHITE, screen, button.rect.x, button.rect.y, button.rect.center)
                yPos+=screen.get_height() / 5
            elif button.button_type == "next_button":
                button.draw_button(screen)
                draw_text(next_text, 25, WHITE, screen, button.rect.x, button.rect.y, button.rect.center)
            else:
                button.rect.center = screen_center
                button.rect.y=yPos
                button.draw_button(screen)
                draw_text(options[pos], 25, WHITE, screen, button.rect.x, button.rect.y, button.rect.center)
                pos+=1
                yPos+=screen.get_height() / 5
    def checkMouseCollision(self, mx, my, button_dictionary, click):
        if button_dictionary["single_player_btn"].rect.collidepoint((mx, my)):
            if click:
                button_dictionary["single_player_btn"].clicked = not button_dictionary["single_player_btn"].clicked
        if button_dictionary["multi_player_btn"].rect.collidepoint((mx, my)):
            if click:
                self.gamemode = "multiplayer"
                button_dictionary["multi_player_btn"].clicked = not button_dictionary["multi_player_btn"].clicked
        if button_dictionary["computer_player_btn"].rect.collidepoint((mx, my)):
            if click:
                self.gamemode = "computer"
                button_dictionary["computer_player_btn"].clicked = not button_dictionary["computer_player_btn"].clicked
        if button_dictionary["easy_btn"].rect.collidepoint((mx, my)):
            if click:
                button_dictionary["easy_btn"].clicked = not button_dictionary["easy_btn"].clicked
        if button_dictionary["med_btn"].rect.collidepoint((mx, my)):
            if click:
                self.difficulty = "medium"
                button_dictionary["med_btn"].clicked = not button_dictionary["med_btn"].clicked
        if button_dictionary["hard_btn"].rect.collidepoint((mx, my)):
            if click:
                self.difficulty = "hard"
                button_dictionary["hard_btn"].clicked = not button_dictionary["hard_btn"].clicked


        if button_dictionary["play_btn"].rect.collidepoint((mx, my)):
            if click:
                button_dictionary["play_btn"].clicked = True    

        if button_dictionary["difficulty_btn"].rect.collidepoint((mx, my)):
            if click:
                button_dictionary["difficulty_btn"].clicked = True
                button_dictionary["play_btn"].clicked = False
                button_dictionary["difficulty_btn"].rect.x = 1000

    def get_buttons(self, screen):
        button_dict = {
            "choose_gamemode_btn":Button(pygame.Rect(0, 0, screen.get_width() / 3, 50), DARK_BLUE, False, 15, GRAY, button_type="title_button"),
            "single_player_btn": Button(pygame.Rect(0, 0, screen.get_width() / 4, 50), LIGHT_BLUE, False, 15, GRAY),
            "multi_player_btn" : Button(pygame.Rect(0, 0, screen.get_width() / 4, 50), LIGHT_BLUE, False, 15, GRAY),
            "computer_player_btn" : Button(pygame.Rect(0, 0, screen.get_width() / 4, 50), LIGHT_BLUE, False, 15, GRAY),
            #TODO: Fix button position on different screen sizes
            "difficulty_btn" : Button(pygame.Rect(self.screen_width - screen.get_width() / 4, self.screen_height-50, screen.get_width() / 4, 50), GRAY, False, 15, GRAY, button_type="next_button"),
            "easy_btn": Button(pygame.Rect(0, 0, screen.get_width() / 4, 50), LIGHT_BLUE, False, 15, GRAY),
            "med_btn" : Button(pygame.Rect(0, 0, screen.get_width() / 4, 50), LIGHT_BLUE, False, 15, GRAY),
            "hard_btn" : Button(pygame.Rect(0, 0, screen.get_width() / 4, 50), LIGHT_BLUE, False, 15, GRAY),
            "play_btn" : Button(pygame.Rect(self.screen_width - screen.get_width() / 4, self.screen_height-50, screen.get_width() / 4, 50), GRAY, False, 15, GRAY, button_type="next_button")
        }
        return button_dict

def draw_text(text, font_size, color, surface, x, y, center):
    font = pygame.font.SysFont(None, font_size)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    textrect.center = center
    surface.blit(textobj, textrect)

# This makes it so that the game can only be run by this file.
if __name__ == '__main__':
    pygame.init()
    gamemode = Gamemode(1080, 720, True)
    gamemode.create_gamemode_window()
