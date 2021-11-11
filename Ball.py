import pygame
import sys
import time
import random
import os
from pygame.locals import *

import math
import random
from fRect import fRect
class Ball:

    """Ball used for playing the game. Only one ball gets initialized."""


    def __init__(self, table_size, size, paddle_bounce, wall_bounce, dust_error, init_speed_mag, theme):
        rand_ang = (.4+.4*random.random())*math.pi * \
            (1-2*(random.random() > .5))+.5*math.pi
        speed = (init_speed_mag*math.cos(rand_ang) ,
                 init_speed_mag*math.sin(rand_ang))
    
        pos = (table_size[0]/2, table_size[1]/2)
        self.frect = fRect((pos[0]-size[0]/2, pos[1]-size[1]/2), size)
        self.speed = speed
        self.size = size
        self.paddle_bounce = paddle_bounce
        self.wall_bounce = wall_bounce
        self.dust_error = dust_error
        self.init_speed_mag = init_speed_mag
        self.prev_bounce = None
        global SOUND_EFFECT
        global THEME
        THEME = theme
        self.setThemeSound()

    
    def setThemeSound(self):
        global SOUND_EFFECT
        rand_num = random.randint(1,5)
        if(THEME == 1 or THEME == 3):
            pass
        elif(THEME == 4):
            SOUND_EFFECT = pygame.mixer.Sound(f'mathewpack/{rand_num}.wav')
            SOUND_EFFECT.set_volume(1)
        elif(THEME == 2):
            SOUND_EFFECT = pygame.mixer.Sound("sounds/AUDIO_CORRECTED_SHAMONE.wav")
            SOUND_EFFECT.set_volume(0.2)
        elif(THEME == 5):
            global SOUND_EFFECT_LEFT 
            SOUND_EFFECT_LEFT = pygame.mixer.Sound("sounds/nomnomnom.wav")
            SOUND_EFFECT_LEFT.set_volume(0.5)
            global SOUND_EFFECT_RIGHT
            SOUND_EFFECT_RIGHT = pygame.mixer.Sound("sounds/MILKLOWERED.wav")
            SOUND_EFFECT_RIGHT.set_volume(0.5)


    def get_center(self):
        """Finds the (x,y) coordinates for the middle of the ball

        Parameters:
        self (Ball): The current ball that the game is using

        Returns:
        tuple: The (x,y) coordinates of the center of the ball
        """

        return (self.frect.pos[0] + .5*self.frect.size[0], self.frect.pos[1] + .5*self.frect.size[1])

    def get_speed_mag(self):
        """Calculates the magnitude of the ball. In physics, magnitude is a value that describes the size of an entity, or its speed when moving

        Parameters:
            self (Ball): The current ball that the game is using

        Returns:
            int: The magnitude of the ball
        """

        return math.sqrt(self.speed[0]**2+self.speed[1]**2)

    def move(self, paddles, table_size, move_factor):
        
        """responsible for moving the ball

        Parameters:
            self (Ball): The current ball that the game is using
            paddles (list): left and right paddles
            table_size (tuple): size of the game window
            move_factor (int): constant factor always set to 1

        Returns:
            None
        """
        moved = 0
        # Array of rtwo rectangles that represent the wall boundaries
        walls_Rects = [Rect((-100, -100), (table_size[0]+200, 100)),
                       Rect((-100, table_size[1]), (table_size[0]+200, 100))]

        for wall_rect in walls_Rects:
            # Determines if the ball has collided with the wall
            if self.frect.get_rect().colliderect(wall_rect):
                c = 0
                detectCollision(self)
                while self.frect.get_rect().colliderect(wall_rect):
                    self.frect.move_ip(-.1 *
                                       self.speed[0], -.1*self.speed[1], move_factor)
                    c += 1  # this basically tells us how far the ball has traveled into the wall
                r1 = 1+2*(random.random()-.5)*self.dust_error
                r2 = 1+2*(random.random()-.5)*self.dust_error

                self.speed = (
                    self.wall_bounce*self.speed[0]*r1, -self.wall_bounce*self.speed[1]*r2)

                while c > 0 or self.frect.get_rect().colliderect(wall_rect):
                    self.frect.move_ip(.1 *
                                       self.speed[0], .1*self.speed[1], move_factor)
                    c -= 1  # move by roughly the same amount as the ball had traveled into the wall
                moved = 1

       
        for paddle in paddles:
         # Determines if the ball has collided with either of the two paddles
            
            if self.frect.intersect(paddle.frect):
                detectCollision(self)
                if(THEME == 2):
                    SOUND_EFFECT.play()
                elif(THEME == 4):
                    self.setThemeSound()
                    SOUND_EFFECT.play()
                    if(pygame.mixer.get_busy() == False):
                        SOUND_EFFECT.play()
                elif(THEME == 5):
                    global SOUND_EFFECT_LEFT
                    global SOUND_EFFECT_RIGHT
                    self.setThemeSound()
                    if (paddle == paddles[0]):
                        SOUND_EFFECT_LEFT.play()
                    elif(paddle == paddles[1]):
                        SOUND_EFFECT_RIGHT.play()
        
                if (paddle.facing == 1 and self.get_center()[0] < paddle.frect.pos[0] + paddle.frect.size[0]/2) or \
                        (paddle.facing == 0 and self.get_center()[0] > paddle.frect.pos[0] + paddle.frect.size[0]/2):
                    continue

                c = 0

                while self.frect.intersect(paddle.frect) and not self.frect.get_rect().colliderect(walls_Rects[0]) and not self.frect.get_rect().colliderect(walls_Rects[1]):
                    self.frect.move_ip(-.1 *
                                       self.speed[0], -.1*self.speed[1], move_factor)

                    c += 1
                theta = paddle.get_angle(
                    self.frect.pos[1]+.5*self.frect.size[1])

                v = self.speed

                v = [math.cos(theta)*v[0]-math.sin(theta)*v[1],
                     math.sin(theta)*v[0]+math.cos(theta)*v[1]]

                v[0] = -v[0]

                v = [math.cos(-theta)*v[0]-math.sin(-theta)*v[1],
                     math.cos(-theta)*v[1]+math.sin(-theta)*v[0]]

                # Bona fide hack: enforce a lower bound on horizontal speed and disallow back reflection
                # ball is not traveling (a) away from paddle (b) at a sufficient speed
                if v[0]*(2*paddle.facing-1) < 1:
                    # transform y velocity so as to maintain the speed
                    v[1] = (v[1]/abs(v[1]))*math.sqrt(v[0]**2 + v[1]**2 - 1)
                    # note that minimal horiz speed will be lower than we're used to, where it was 0.95 prior to the  increase by 1.2
                    v[0] = (2*paddle.facing-1)

                # a bit hacky, prevent multiple bounces from accelerating
                # the ball too much
                if not paddle is self.prev_bounce:
                    self.speed = (v[0]*self.paddle_bounce,
                                  v[1]*self.paddle_bounce)
                else:
                    self.speed = (v[0], v[1])
                self.prev_bounce = paddle

                while c > 0 or self.frect.intersect(paddle.frect):

                    self.frect.move_ip(.1 *
                                       self.speed[0], .1*self.speed[1], move_factor)

                    c -= 1

                moved = 1

        if not moved:
            self.frect.move_ip(self.speed[0], self.speed[1], move_factor)

global DVDCollision
DVDCollision = USEREVENT + 1
my_event = pygame.event.Event(DVDCollision, message="Collision")

def detectCollision(self):
    global my_event
    pygame.event.post(my_event)
    #DVD = pygame.image.load("sprites/DVD/DVDBlue.png")
    #DVD = pygame.transform.scale(DVD, (100, 50))

    #return DVD
    