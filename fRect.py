import pygame
import sys
import time
import random
import os
from pygame.locals import *

import math

class fRect:
    """By default, pygame already has a built-in class for rectangular coordinates called 'Rect'. The built-in 'Rect' class uses integers for its coordinates. 
       The purpose of this custom class called 'fRect' is to give us access to floating point coordinates instead of integer coordinates. 
       By doing this, our collisions and game movement are a lot more accurate. In the 'background' of the game, both
       the paddles and the ball will have 'fRect' coordinates instead of 'Rect' coordinates."""

    def __init__(self, pos, size):
        self.pos = (pos[0], pos[1])
        self.size = (size[0], size[1])

    def move(self, x, y):
        """Moves the rectangle based on the x and y values. Returns a new object"""
        return fRect((self.pos[0]+x, self.pos[1]+y), self.size)

    def move_ip(self, x, y, move_factor=1):
        """Moves the rectangle based on the x and y values. Does not return a new object"""
        self.pos = (self.pos[0] + x*move_factor, self.pos[1] + y*move_factor)

    def get_rect(self):
        return Rect(self.pos, self.size)

    def copy(self):
        return fRect(self.pos, self.size)

    def intersect(self, other_frect):
        """Determines if two rectangles intersect. In our game, a collision happens when two rectangles intersect with each other."""

        # two rectangles intersect iff both x and y projections intersect
        for i in range(2):
            if self.pos[i] < other_frect.pos[i]:  # projection of self begins to the left
                if other_frect.pos[i] >= self.pos[i] + self.size[i]:
                    return 0
            elif self.pos[i] > other_frect.pos[i]:
                if self.pos[i] >= other_frect.pos[i] + other_frect.size[i]:
                    return 0
        return 1  # self.size > 0 and other_frect.size > 0