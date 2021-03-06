import pygame
import constant
import set_up
import pygame
import constant
import set_up

def message_display_screen(text, x, y, size):
    #print(pygame.font.get_fonts())
    #name_font = pygame.font.SysFont('comicsansms',size)
    largeText = pygame.font.Font(constant.BUTTON_FONTS, size)
    TextSurf, TextRect = text_objects_screen(text, largeText)
    TextRect.center = (x, y)
    set_up.game_layout_display.blit(TextSurf, TextRect)

def text_objects_screen(text, font):
    textSurface = font.render(text, True, constant.black_color)
    return textSurface, textSurface.get_rect()

def message_display1_screen(text, x, y, fs, c):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x, y)
    set_up.game_layout_display.blit(TextSurf, TextRect)

def text_objects1(text, font):
    textSurface = font.render(text, True, constant.blue_color)
    return textSurface, textSurface.get_rect(
