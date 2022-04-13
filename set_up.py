import pygame
import constant
pygame.init() # initialization of the modules
print(pygame.get_init())

ic = pygame.image.load(constant.ICON)
game_layout_display = pygame.display.set_mode((constant.WIDTH, constant.HEIGHT), pygame.FULLSCREEN) # loads display
pygame.display.set_caption(constant.CAPTIONS)
pygame.display.set_icon(ic)
pygame.display.update()



mother_board = pygame.image.load(constant.MOTHERBOARD_IMAGE_NAME)
d1 = pygame.image.load(constant.DICE1_IMAGE_NAME)
d2 = pygame.image.load(constant.DICE2_IMAGE_NAME)
d3 = pygame.image.load(constant.DICE3_IMAGE_NAME)
d4 = pygame.image.load(constant.DICE4_IMAGE_NAME)
d5 = pygame.image.load(constant.DICE5_IMAGE_NAME)
d6 = pygame.image.load(constant.DICE6_IMAGE_NAME)

#Importing the players for the game

teal_c = pygame.image.load(constant.COUNTER_TEAL_IMAGE_NAME)
whitec = pygame.image.load(constant.COUNTER_WHITE_IMAGE_NAME)
grey_c = pygame.image.load(constant.COUNTER_GREY_IMAGE_NAME)
purple_c = pygame.image.load(constant.COUNTER_PURPLE_IMAGE_NAME)
menu_background = pygame.image.load(constant.MENU_BACKGROUND)
posts = pygame.image.load(constant.POSTS)

initial_background = pygame.image.load(constant.INITIAL_BACKGROUND_IMAGE_NAME)
initial_background1 = pygame.image.load(constant.INITIAL_BACKGROUND1_IMAGE_NAME)
initial_background2 = pygame.image.load(constant.INITIAL_BACKGROUND2_IMAGE_NAME)
initial_background3 = pygame.image.load(constant.INITIAL_BACKGROUND3_IMAGE_NAME)
initial_background4 = pygame.image.load(constant.INITIAL_BACKGROUND4_IMAGE_NAME)
initial_background5 = pygame.image.load(constant.INITIAL_BACKGROUND5_IMAGE_NAME)
copyrights = pygame.image.load(constant.OWNER)

pygame.mixer.music.load(constant.PYGAME_MIXER_SOUND)
snake_sound = pygame.mixer.Sound(constant.SNAKE_SOUND)
win = pygame.mixer.Sound(constant.WIN_SOUND)
lose = pygame.mixer.Sound(constant.LOSE_SOUND)
ladder = pygame.mixer.Sound(constant.LADDER_SOUND)

button_1 = pygame.image.load(constant.COUNTER_RED_IMAGE_NAME)
button_2 = pygame.image.load(constant.COUNTER_YELLOW_IMAGE_NAME)
button_3 = pygame.image.load(constant.COUNTER_GREEN_IMAGE_NAME)
button_4 = pygame.image.load(constant.COUNTER_BLUE_IMAGE_NAME)
