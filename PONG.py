import pygame
from paddle import Paddle


pygame.init()

#Colors used 
BLACK = (0,0,0)
WHITE = (255,255,255)

#Setting the dimensions of the window
WIDTH = 900
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("PONG AI")

#fps for our game, 60 should run smooth on most devices
FPS = 60

#paddle creation
paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 20
paddle1.rect.y = 200
 
paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 870
paddle2.rect.y = 200

#list of "sprites" which are the paddles
all_paddles_list = pygame.sprite.Group()
all_paddles_list.add(paddle1)
all_paddles_list.add(paddle2)


#Ball creation
BALL_SIZE = 15
BALL = pygame.Rect(WIDTH/2 - BALL_SIZE/2, HEIGHT/2 - BALL_SIZE/2, BALL_SIZE, BALL_SIZE)


#The boilerplate for a standard pygame display
playing = True
clock = pygame.time.Clock()
while playing:
    clock.tick(FPS)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            playing = False

    screen.fill(BLACK)
   
    all_paddles_list.update()
    pygame.draw.rect(screen, WHITE, BALL)
    all_paddles_list.draw(screen)
    
    pygame.display.flip()
    

pygame.quit()

