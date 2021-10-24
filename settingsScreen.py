import pygame, sys


pygame.init()
pygame.display.set_caption("Settings")
WIN_SIZE = (800, 500)
WINDOW = pygame.display.set_mode(WIN_SIZE)

def Settings():
    running = True
    while(running): 
        for event in pygame.event.get():
            
            if(event.type == pygame.QUIT):
                running = False
    pygame.display.update()
        
Settings()
