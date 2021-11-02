import pygame
def moveUp(self):
    self.x = self.x + self.speed

def moveDown(self):
    self.x = self.x - self.speed

def on_execute(self, key_state_function):

    # While game is running
    while( self._running ):
        pygame.event.pump()

        keys = key_state_function() 
        print(keys)

        if (keys[K_UP]):
            self.player.moveUp()

        if (keys[K_Down]):
            self.player.moveDown()

        self.on_render()




def create_key_mock(pressed_key):
    def helper():
        tmp = [0] * 300
        tmp[pressed_key] = 1
        
        return tmp
    return helper
    

pygame.key.get_pressed = create_key_mock(K_UP)

def create_key_mock(pressed_key):
    def helper():
        tmp = [0] * 300
        tmp[pressed_key] = 2
        return tmp
    return helper
pygame.key.get_pressed = create_key_mock(K_Down)



