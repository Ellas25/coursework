import pygame
import boardgame
import powerups
import pygame
import main

def powerups(x):
    if x == 95:
        return 3
    elif x == 7:
        return 83
    elif x == 17:
        return 1
    #elif x == 22:
        # return "roll again"
    #elif x == 55:
        # return miss a go

def ladders(x):
    if x == 1:
        return 38
    elif x == 4:
        return 14
    elif x == 9:
        return 31
    elif x == 28:
        return 84
    elif x == 21:
        return 42
    elif x == 51:
        return 67
    elif x == 80:
        return 99
    elif x == 72:
        return 91
    else:
        return x

def snakes(e):
    if e == 17:
        return 7
    elif e == 54:
        return 34
    elif e == 62:
        return 19
    elif e == 64:
        return 60
    elif e == 87:
        return 36
    elif e == 93:
        return 73
    elif e == 95:
        return 75
    elif e == 98:
        return 79
    else:
        return e



        
   
