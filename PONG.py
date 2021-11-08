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

import pygame_menu
import pygame
import sys
import time
import random
import os
from pygame.locals import *
import glob
import mysql.connector
#from SettingsMenu import SettingsMenu

import math
from Ball import DVDCollision
from Ball import Ball
from Paddle import Paddle
from fRect import fRect
from PauseMenu import RESUMEGAME
from PauseMenu import pauseMenu
from PlayAgain import PLAYAGAIN
from PlayAgain import playagain
from PauseMenu import MAINMENU

pygame.init()
# In pygame, all colors are represented by RGB values in the format (R, G, B).
name = ""
flipped = False
white = [255, 255, 255]
black = [0, 0, 0]
global GOAL_SOUND
global THEME
global DVD
DVDimages = glob.glob("sprites/DVD/*.png")
DVD = pygame.image.load("sprites/DVD/DVDWhite.png")
DVD = pygame.transform.scale(DVD, (100, 50))
# This clock is used to control the frame rate of the game
clock = pygame.time.Clock()
global Winner
Winner = ""

def theme(screen,ball, value):
    global GOAL_SOUND
    if value == 1:
        pass
    elif value == 2:
        MICHAEL = pygame.image.load("sprites/MIKEY.png")
        MICHAEL = pygame.transform.scale(MICHAEL, (150,75))
        #placing my boy heehee right on the ball and subtracting by half the width and half the height to place the exact midpoint of heehee on the ball
        screen.blit(MICHAEL, (int(ball.get_center()[0]) - 75, int(ball.get_center()[1]) - 37.5))
        GOAL_SOUND = pygame.mixer.Sound("sounds/HEEHEE4.mp3")
        GOAL_SOUND.set_volume(0.3)
    elif value == 4:
        MATHEW = pygame.image.load("mathewpack/mathew.png")
        MATHEW = pygame.transform.scale(MATHEW, (275,150))
        screen.blit(MATHEW, (int(ball.get_center()[0]) - 137.5, int(ball.get_center()[1]) - 75))
        GOAL_SOUND = pygame.mixer.Sound("mathewpack/2.wav")
        GOAL_SOUND.set_volume(1)
    else:
        pass
        #DVD = pygame.image.load("sprites/DVD/DVDWhite.png")
        #DVD = pygame.transform.scale(DVD, (100, 50))
        #screen.blit(DVD, (int(ball.get_center()[0]) - 50, int(ball.get_center()[1]) - 25))

def DVDHandler(screen, ball):
    
    random_DVD = random.choice(DVDimages)
    global DVD
    DVD = pygame.image.load(random_DVD)
    DVD = pygame.transform.scale(DVD, (100, 50))
    return DVD
    #screen.blit(DVD, (int(ball.get_center()[0]) - 100, int(ball.get_center()[1]) - 25))
    
    print(f"The random dvd: {random_DVD}")
    pass

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

    
    
    if(THEME == 1):
        pygame.draw.circle(screen, white, (int(ball.get_center()[0]), int(
        ball.get_center()[1])),  int(ball.frect.size[0]/2), 0)
    
    theme(screen, ball, THEME)
    
    pygame.draw.line(screen, white, [screen.get_width(
    )/2, 0], [screen.get_width()/2, screen.get_height()])

    score_font = pygame.font.Font(None, 32)
    screen.blit(score_font.render(str(score[0]), True, white), [
                int(0.4*table_size[0])-8, 0])
    screen.blit(score_font.render(str(score[1]), True, white), [
                int(0.6*table_size[0])-8, 0])
    global DVD
    
    #DVD = DVDHandler(screen, ball)
    if(THEME == 3):
        screen.blit(DVD, (int(ball.get_center()[0]) - 50, int(ball.get_center()[1]) - 25))
    
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
        if(THEME == 2 or THEME == 4):
            GOAL_SOUND.play()
        score[1] += 1
        ball = Ball(table_size, ball.size, ball.paddle_bounce,
                    ball.wall_bounce, ball.dust_error, ball.init_speed_mag, THEME)
        return (ball, score)
    # Determines if the left paddle scored the point
    elif ball.frect.pos[0]+ball.size[0]/2 >= table_size[0]:
        if(THEME == 2 or THEME == 4):
            GOAL_SOUND.play()
        ball = Ball(table_size, ball.size, ball.paddle_bounce,
                    ball.wall_bounce, ball.dust_error, ball.init_speed_mag, THEME)
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
    #SONG = pygame.mixer.Sound("sounds/pickypluckpluckyayuhya.wav")
    SONG = pygame.mixer.Sound("sounds/asuperretrofuturisticsynthwavetypebeat.wav")
    SONG.set_volume(0.3)
    global pause
    pause = False
    while max(score) < score_to_win:
        if(pygame.mixer.get_busy() == False):
            if(THEME == 1):
                SONG.play()
    
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
            if(THEME == 3 and event.type == DVDCollision):
                global DVD
                DVD = DVDHandler(screen, ball)
                #screen.blit(DVD, (0,0))
                #print(f"The string is: {random_DVD}")
                #print("dvd collided")
                
            if(event.type == pygame.KEYDOWN):
                
                if(event.key == pygame.K_p and ball.speed != (0,0)):
                    pygame.mixer.pause()
                    ballSpeed = ball.speed
                    ball.speed = (0,0)
                    paddleLeftSpeed = paddles[0].speed
                    paddleRightSpeed = paddles[1].speed
                    paddles[0].speed = 0
                    paddles[1].speed = 0
                    pauseMenu(screen.get_width(), screen.get_height())
                
                
            if(event.type == RESUMEGAME):
                print("clicked resume in event")
                ball.speed = ballSpeed
                paddles[0].speed = paddleLeftSpeed
                paddles[1].speed = paddleRightSpeed
                pygame.mixer.unpause()

            elif(event.type == MAINMENU):
                return
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
    connection = mysql.connector.connect(host='localhost',
                                        database='mydb',
                                        user='root',
                                        password='pingpong1!')
    mycursor = connection.cursor()
    cleanName = clean(name)
    
    global Winner
    Winner = cleanName
    sql = f'UPDATE pongleaderboard SET numberOfWins = numberOfWins + 1 WHERE username = "{cleanName}"'
    if score[0] > score[1]:
        if not paddles[0].isAI:
            mycursor.execute(sql)
            connection.commit()
            Winner = "Left"
        else: 
            Winner = "AI"
        screen.blit(font.render("Left wins!", True, white, black), [24, 32])
        
    else:
        if not paddles[1].isAI:
            mycursor.execute(sql)
            connection.commit()
        else: 
            Winner = "AI"
        screen.blit(font.render("Right wins!", True, white, black), [24, 32])
    pygame.display.flip()
    clock.tick(2)

    pygame.event.pump()
    
    while any(pygame.key.get_pressed()):
        pygame.event.pump()
        clock.tick(30)

    print(score)





global table_size
table_size = (440, 280)



def not_exist(cleanname):
    connection = mysql.connector.connect(host='localhost',
                                        database='mydb',
                                        user='root',
                                        password='pingpong1!')
    
    mycursor = connection.cursor()
    sql = f'SELECT * FROM pongLeaderboard WHERE userName = "{cleanname}"'
    mycursor.execute(sql)
    users = mycursor.fetchall()
    if len(users) <= 0:
        return True
    else:
        return False

def insert(cleanname):
    numwins = 0
    print("CREATING")
    connection = mysql.connector.connect(host='localhost',
                                        database='mydb',
                                        user='root',
                                        password='pingpong1!')
    
    mycursor = connection.cursor()
    sql = f'INSERT INTO pongLeaderboard (userName, numberOfWins) VALUES ("{cleanname}", "{numwins}")'
    mycursor.execute(sql)
    connection.commit()

def init_game(gamemode = 'singleplayer', difficulty = 'hard', resolution = (1080, 720), fps = 60, theme = 1, score = 11, paddleSize = "Medium"):
    """Sets up the game by initializing the game window, paddles, and the ball. Sets default values for the paddle speed, ball size, paddle size, and FPS.
    """
    pygame.init()
    file1 = open("name.txt","r+")
    global name
    name = file1.read()

    cleanName = clean(name)
    if not_exist(cleanName):
        insert(cleanName)
    global THEME
    THEME = theme
    table_size = resolution
    #paddle_size = (10, 110)
    if(paddleSize == "Small"):
        paddle_size = (10, resolution[0] * 0.10) 
    elif(paddleSize == "Medium"):
        paddle_size = (10, resolution[0] * 0.15)
    elif(paddleSize == "Large"):
        paddle_size = (10, resolution[0] * 0.20)
    else:
        paddle_size = (10, resolution[0] * 0.01)
    if(theme == 1):
        ball_size = (15, 15)
    elif(theme == 2):
        ball_size = (40,50)
    else:
        ball_size = (95, 60)

    paddle_speed = 5
    max_angle = 45

    paddle_bounce = 1.2
    wall_bounce = 1.00
    dust_error = 0.00
    init_speed_mag = 5
    global clock_rate
    clock_rate = fps
    turn_wait_rate = 3
    score_to_win = score

    screen = pygame.display.set_mode(table_size)
    pygame.display.set_caption('Pong')

    import AI
    """paddles = [Paddle((20, table_size[1]/2), paddle_size, paddle_speed, max_angle,  1),
               Paddle((table_size[0]-20, table_size[1]/2), paddle_size, paddle_speed, max_angle, 0)]
    ball = Ball(table_size, ball_size, paddle_bounce,
                wall_bounce, dust_error, init_speed_mag, theme)
"""
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
                wall_bounce, dust_error, init_speed_mag, theme)

    game_loop(screen, paddles, ball, table_size,
              clock_rate, turn_wait_rate, score_to_win, 1)

    # screen.blit(pygame.font.Font(None, 32).render(
    #     str('SWITCHING SIDES'), True, white), [int(0.6*table_size[0])-8, 0])

    pygame.display.flip()
    clock.tick(4)

    print(f"The 0 paddle has AI is {paddles[0].isAI} and 1 paddle has AI is {paddles[1].isAI}")
    paddles[0].move_getter, paddles[1].move_getter = paddles[1].move_getter, paddles[0].move_getter

    
    #paddles[0], paddles[1] = paddles[1], paddles[0]
    print(f"The 0 paddle has AI is {paddles[0].isAI} and 1 paddle has AI is {paddles[1].isAI}")

    global Winner
    if Winner:
        playagain(Winner, resolution[0], resolution[1], gamemode, difficulty, resolution, fps, theme, score, paddleSize)
    
    # game_loop(screen, paddles, ball, table_size,
    #           clock_rate, turn_wait_rate, score_to_win, 1)

    # pygame.quit()


    
# This makes it so that the game can only be run by this file.
if __name__ == '__main__':
    
    #pygame.mixer.pre_init()
    pygame.mixer.init()
    
    pygame.init()

def clean(name):
    answ = ""
    for char in name:
        if char.isalpha():
            answ+=char
    return answ

# def test():
#             file1 = open("name.txt","r+")
#             name = file1.read()
#             name = clean(name)

#             connection = mysql.connector.connect(host='localhost',
#                                         database='mydb',
#                                         user='root',
#                                         password='pingpong1!')
#             mycursor = connection.cursor()
#             # sql = "UPDATE pongleaderboard SET numberOfWins = numberOfWins + 1 WHERE username = 'Aakif' "
#             sql = f'UPDATE pongleaderboard SET numberOfWins = numberOfWins + 1 WHERE username = "{name}"'
#             val = name
#             print(val)
#             mycursor.execute(sql)
#             connection.commit()
# test()
