import pygame
import boardgame
import random 
"""
def dice(d):
    if d == 1:
        d = constant.DICE1_IMAGE_NAME
    elif d == 2:
        d = constant.DICE2_IMAGE_NAME
    elif d == 3:
        d = constant.DICE3_IMAGE_NAME
    elif d == 4:
        d = constant.DICE4_IMAGE_NAME
    elif d == 5:
        d = constant.DICE5_IMAGE_NAME
    elif d == 6:
        d = constant.DICE6_IMAGE_NAME This was apparently plagarised 
"""
def dice(di):
    minimum_value = 1
    maximum_value = 7
    rolls_dice = "Yes" or "yes" or "y" or "Y"
    
    while rolls_dice = "Yes" or "yes" or "y" or "Y":
        print random.randint (minimum_value,maximum_value)
        print random.randint( minimum_value,emaximum_value )

    clock_times = pygame.time.get_ticks()
    while pygame.time.get_ticks() - clock_time < 3000:
        set_up.game_layout_display.blit(d, (300, 500))
        pygame.display.update()
