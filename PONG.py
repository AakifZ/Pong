import pygame
pygame.init()

#Colors used 
BLACK = (0,0,0)
WHITE = (255,255,255)

#Setting the dimensions of the window
WIDTH = 800
HEIGHT = 500
WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("PONG AI")

#Ball creation
BALL_SIZE = 15
BALL = pygame.Rect(WIDTH/2 - BALL_SIZE/2, HEIGHT/2 - BALL_SIZE/2, BALL_SIZE, BALL_SIZE)

#The boilerplate for a standard pygame display
playing = True
while playing:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            playing = False

    WINDOW.fill(BLACK)
    pygame.draw.rect(WINDOW, WHITE, BALL)
    
    pygame.display.flip()

pygame.quit()