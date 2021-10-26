#   PongAIvAI
#   Authors: Michael Guerzhoy and Denis Begun, 2014-2016.
#   http://www.cs.toronto.edu/~guerzhoy/
#   Email: guerzhoy at cs.toronto.edu
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version. You must credit the authors
#   for the original parts of this code.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTIhCULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   Parts of the code are based on T. S. Hayden Dennison's PongClone (2011)
#   http://www.pygame.org/project-PongClone-1740-3032.html

#   This code runs with Python 2 and requires PyGame for Python 2
#   Download PyGame here: https://bitbucket.org/pygame/pygame/downloads


import pygame
import sys
import time
import random
import os
from pygame.locals import *

import math

from Ball import Ball
from Paddle import Paddle
from fRect import fRect



# In pygame, all colors are represented by RGB values in the format (R, G, B).
white = [255, 255, 255]
black = [0, 0, 0]

# This clock is used to control the frame rate of the game
clock = pygame.time.Clock()

def render(screen, paddles, ball, score, table_size):
    """Used for updating the score, paddle positions, and ball position on the screen

        Parameters:
            screen (pygame.display): Game window
            paddles (list): left and right paddles
            ball (Ball): ball used for the game
            score (list): score of the game
            table_size (tuple): window size dimensions

        Returns:
            None
    """
    screen.fill(black)

    pygame.draw.rect(screen, white, paddles[0].frect.get_rect())
    pygame.draw.rect(screen, white, paddles[1].frect.get_rect())

    pygame.draw.circle(screen, white, (int(ball.get_center()[0]), int(
        ball.get_center()[1])),  int(ball.frect.size[0]/2), 0)

    pygame.draw.line(screen, white, [screen.get_width(
    )/2, 0], [screen.get_width()/2, screen.get_height()])

    score_font = pygame.font.Font(None, 32)
    screen.blit(score_font.render(str(score[0]), True, white), [
                int(0.4*table_size[0])-8, 0])
    screen.blit(score_font.render(str(score[1]), True, white), [
                int(0.6*table_size[0])-8, 0])

    pygame.display.flip()


def check_point(score, ball, table_size):
    """Checks who scored the point. If the ball goes out of bounds to the right, then the left player gets a point. Otherwise, the right player gets the point.

        Parameters:
            score (list): score of the game
            ball (Ball): ball used for the game
            table_size (pygame.display): current ball used for the game

        Returns:
            tuple
    """
    # Determines if the right paddle scored the point
    if ball.frect.pos[0]+ball.size[0]/2 < 0:
        score[1] += 1
        ball = Ball(table_size, ball.size, ball.paddle_bounce,
                    ball.wall_bounce, ball.dust_error, ball.init_speed_mag)
        return (ball, score)
    # Determines if the left paddle scored the point
    elif ball.frect.pos[0]+ball.size[0]/2 >= table_size[0]:
        ball = Ball(table_size, ball.size, ball.paddle_bounce,
                    ball.wall_bounce, ball.dust_error, ball.init_speed_mag)
        score[0] += 1
        return (ball, score)

    return (ball, score)


def game_loop(screen, paddles, ball, table_size, clock_rate, turn_wait_rate, score_to_win, display):
    """This is the loop that the game runs inside of. The game keeps going as long as one of the players hasn't reached the score_to_win

        Parameters:
            screen (pygame.display): game window
            paddles (list): left and right paddles
            ball (Ball): ball used for the game
            table_size (tuple): size of the game window
            clock_rate (int): FPS of the game. Set at 80 by default
            turn_wait_rate (): used to control the framerate of the game. Set to a constant factor of 3 by default
            score_to_win (int): Score needed to win the game. Set to 10 by default.
            display (int): constant always set to 1

        Returns:
            None
    """
    score = [0, 0]

    while max(score) < score_to_win:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
       

        old_score = score[:]
        ball, score = check_point(score, ball, table_size)
        paddles[0].move(paddles[1].frect, ball.frect, table_size)
        paddles[1].move(paddles[0].frect, ball.frect, table_size)

        inv_move_factor = int((ball.speed[0]**2+ball.speed[1]**2)**.5)
        if inv_move_factor > 0:
            for i in range(inv_move_factor):
                ball.move(paddles, table_size, 1./inv_move_factor)
        else:
            ball.move(paddles, table_size, 1)

        if not display:
            continue
        if score != old_score:
            font = pygame.font.Font(None, 32)
            if score[0] != old_score[0]:
                screen.blit(font.render("Left scores!",
                            True, white, black), [0, 32])
            else:
                screen.blit(font.render("Right scores!", True, white, black), [
                            int(table_size[0]/2+20), 32])

            pygame.display.flip()
            clock.tick(turn_wait_rate)

        render(screen, paddles, ball, score, table_size)

        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[K_q]:
            return

        clock.tick(clock_rate)

    font = pygame.font.Font(None, 64)
    if score[0] > score[1]:
        screen.blit(font.render("Left wins!", True, white, black), [24, 32])
    else:
        screen.blit(font.render("Right wins!", True, white, black), [24, 32])
    pygame.display.flip()
    clock.tick(2)

    pygame.event.pump()
    
    while any(pygame.key.get_pressed()):
        pygame.event.pump()
        clock.tick(30)

    print(score)


def init_game(gamemode = 'singleplayer', difficulty = 'easy' ):
    """Sets up the game by initializing the game window, paddles, and the ball. Sets default values for the paddle speed, ball size, paddle size, and FPS.
    """
    
    table_size = (440, 280)
    paddle_size = (10, 70)
    ball_size = (15, 15)
    max_angle = 45

    paddle_bounce = 1.2
    wall_bounce = 1.00
    dust_error = 0.00
    init_speed_mag = 2
    clock_rate = 80
    turn_wait_rate = 3
    score_to_win = 10

    screen = pygame.display.set_mode(table_size)
    pygame.display.set_caption('Pong')

    import AI

    paddles = []
    if gamemode == "singleplayer":
        # player vs computer
        paddles = [AI.get_paddle_difficulty(difficulty, (20, table_size[1]/2), paddle_size, max_angle, 1, True),AI.get_paddle_difficulty(difficulty,(table_size[0]-20, table_size[1]/2), paddle_size, max_angle, 0, False)]
        paddles[0].move_getter = AI.get_move_ai
        paddles[1].move_getter = AI.get_move_player_right

    elif gamemode == "multiplayer":
        # player vs player
        paddles = [AI.get_paddle_difficulty(difficulty, (20, table_size[1]/2), paddle_size, max_angle, 1, False),AI.get_paddle_difficulty(difficulty,(table_size[0]-20, table_size[1]/2), paddle_size, max_angle, 0, False)]
        paddles[0].move_getter = AI.get_move_player_left
        paddles[1].move_getter = AI.get_move_player_right
    else:
        # computer vs computer
        paddles = [AI.get_paddle_difficulty(difficulty, (20, table_size[1]/2), paddle_size, max_angle, 1, True),AI.get_paddle_difficulty(difficulty,(table_size[0]-20, table_size[1]/2), paddle_size, max_angle, 0, True)]
        paddles[0].move_getter = AI.get_move_ai
        paddles[1].move_getter = AI.get_move_ai
    ball = Ball(table_size, ball_size, paddle_bounce,
                wall_bounce, dust_error, init_speed_mag)

    game_loop(screen, paddles, ball, table_size,
              clock_rate, turn_wait_rate, score_to_win, 1)

    screen.blit(pygame.font.Font(None, 32).render(
        str('SWITCHING SIDES'), True, white), [int(0.6*table_size[0])-8, 0])

    pygame.display.flip()
    clock.tick(4)

    paddles[0].move_getter, paddles[1].move_getter = paddles[1].move_getter, paddles[0].move_getter

    game_loop(screen, paddles, ball, table_size,
              clock_rate, turn_wait_rate, score_to_win, 1)

    pygame.quit()