import pygame, sys, PONG


pygame.init()
pygame.display.set_caption("Settings")


WIN_SIZE = PONG.table_size
WINDOW = pygame.display.set_mode(WIN_SIZE, pygame.RESIZABLE)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
SMALLSCREEN = (440, 280)
MEDIUMSCREEN = (880, 560)
LARGESCREEN = (1760, 1120)

smallScreenButton = pygame.Rect(WIN_SIZE[0] * 0.15, WIN_SIZE[1] *0.3, WIN_SIZE[0] * 0.2, WIN_SIZE[1] * 0.2)
mediumScreenButton = pygame.Rect(WIN_SIZE[0] * 0.5, WIN_SIZE[1] * 0.3, WIN_SIZE[0] * 0.2, WIN_SIZE[1] * 0.2)
#largeScreenButton = pygame.Rect(WIN_SIZE[0] * 0.8, WIN_SIZE[1] * 0.3, width, height)

def buttonHover(Button, event, size):
    pygame.draw.rect(WINDOW, GRAY, Button)
    if(event.type == pygame.MOUSEBUTTONDOWN):
        PONG.table_size = size
        pygame.display.set_mode(PONG.table_size)


def Settings():
    running = True
    while(running): 
        for event in pygame.event.get():
            
            if(event.type == pygame.QUIT):
                running = False

            #Draw buttons
            pygame.draw.rect(WINDOW, WHITE, smallScreenButton)
            pygame.draw.rect(WINDOW, WHITE, mediumScreenButton)
            hoverSmall = smallScreenButton.collidepoint(pygame.mouse.get_pos())

            buttonHover(smallScreenButton, event, SMALLSCREEN)
            buttonHover(mediumScreenButton, event, MEDIUMSCREEN)
            """if(hoverSmall):
                pygame.draw.rect(WINDOW, (200,200,200), smallScreenButton)
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    PONG.table_size = (200,200)
                    pygame.display.set_mode(PONG.table_size)
                    smallScreenButton.height = 10
                
            """
            
            """redButton = pygame.draw.rect(WINDOW, (255,0,0), pygame.Rect(PONG.table_size[0] * 0.3 - 150, PONG.table_size[1] * 0.1 - 50, 300, 100))
            if(redButton.collidepoint(pygame.mouse.get_pos())):
                pygame.draw.rect(WINDOW, (240, 100, 100), redButton)
                PONG.table_size = (440, 280)
                pygame.display.set_mode(PONG.table_size)
                redButton.height = 180

    """
            pygame.display.flip()
Settings()
