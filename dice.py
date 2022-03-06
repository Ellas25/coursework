import pygame
import boardgame

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
        d = constant.DICE6_IMAGE_NAME

    time_clock = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time_clock < 1000:
        set_up.game_layout_display.blit(d, (300, 500))
        pygame.display.update()