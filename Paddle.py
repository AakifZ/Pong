import pygame
import sys
import time
import random
import os
from pygame.locals import *

import math

from fRect import fRect

class Paddle:
    """Represents each paddle used for playing the game. Only two paddles get initialized"""

    def __init__(self, pos, size, speed, max_angle, facing, isAI):
        self.frect = fRect((pos[0]-size[0]/2, pos[1]-size[1]/2), size)
        self.speed = speed
        self.size = size
        self.facing = facing
        self.max_angle = max_angle
        self.isAI = isAI

    def move(self, enemy_frect, ball_frect, table_size):
        """responsible for moving the paddle

        Parameters:
            self (Paddle): The current paddle
            enemy_frect (fRect): coordinates of the enemy paddle
            ball_frect (fRect): coordinates of the ball
            table_size (tuple): dimensions of the game window

        Returns:
            None
        """

        direction = self.get_direction(enemy_frect, ball_frect, table_size)

        if direction == "up":
            self.frect.move_ip(0, -self.speed)
        elif direction == "down":
            self.frect.move_ip(0, self.speed)

        to_bottom = (self.frect.pos[1]+self.frect.size[1])-table_size[1]

        if to_bottom > 0:
            self.frect.move_ip(0, -to_bottom)
        to_top = self.frect.pos[1]
        if to_top < 0:
            self.frect.move_ip(0, -to_top)

    def get_angle(self, y):
        """determines the angle that the ball will travel

        Parameters:
            self (Paddle): The current paddle
            y (int): y coordinate of the ball

        Returns:
            int: The angle the ball will travel
        """
        center = self.frect.pos[1]+self.size[1]/2
        rel_dist_from_c = ((y-center)/self.size[1])
        rel_dist_from_c = min(0.5, rel_dist_from_c)
        rel_dist_from_c = max(-0.5, rel_dist_from_c)
        sign = 1-2*self.facing

        return sign*rel_dist_from_c*self.max_angle*math.pi/180
    
    def get_direction(self, enemy_frect, ball_frect, table_size):
        if self.isAI:
            return self.move_getter(self.frect.copy(), enemy_frect.copy(), ball_frect.copy(), tuple(table_size))
        else:
            return self.move_getter()