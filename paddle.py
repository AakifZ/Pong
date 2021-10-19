import pygame
BLACK = (0,0,0)
 
 #Paddle class
class Paddle(pygame.sprite.Sprite):
    
    
    def __init__(self, color, width, height):
        
        super().__init__()
        
        #color of paddle and position
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        #draw
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        
        self.rect = self.image.get_rect()