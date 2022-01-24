import pygame
import constant
import time

pygame.init() # initialization of the modules
print(pygame.get_init())

ic = pygame.image.load("resources/icon.jpg")
game_layout_display = pygame.display.set_mode((constant.WIDTH, constant.HEIGHT), pygame.FULLSCREEN, pygame.WINDOWMINIMIZED) # loads display
pygame.display.set_caption("Ladders and Snakes Game ")
pygame.display.set_icon(ic)
pygame.display.update()

# Graphics: rgb values
black_color = (20, 20, 20)
white_color = (300, 300, 300)
red_color = (300, 0, 0)
blue_red_color = (260, 0, 0)
green_color = (0, 300, 0)
blue_green_color = (0, 290, 0)
blue_color = (0, 0, 300)
grey_color = (100, 100, 100)
yellow_color = (200, 200, 0)
purple_color = (43, 3, 132)
blue_purple_color = (60, 0, 190)

mother_board = pygame.image.load("resources/snake.png")
d1 = pygame.image.load("resources/dice1.png")
d2 = pygame.image.load("resources/dice2.png")
d3 = pygame.image.load("resources/dice3.png")
d4 = pygame.image.load("resources/dice4.png")
d5 = pygame.image.load("resources/dice5.png")
d6 = pygame.image.load("resources/dice6.png")

#Importing the players for the game

red_c = pygame.image.load("resources/red_c.png")
yellow_c = pygame.image.load("resources/yellow_c.png")
green_c = pygame.image.load("resources/green_c.png")
blue_c = pygame.image.load("resources/blue_c.png")
menu_background = pygame.image.load("resources/menu.jpg")
posts = pygame.image.load("resources/snake.png")

initial_background = pygame.image.load("resources/introduction_image.png")
initial_background2 = pygame.image.load("resources/introduction_image2.jpg")
initial_background3 = pygame.image.load("resources/introduction_image3.jpg")
initial_background4 = pygame.image.load("resources/introduction_image4.jpg")
initial_background5 = pygame.image.load("resources/introduction_image5.jpg")
copyrights = pygame.image.load("resources/owner.jpg")

pygame.mixer.music.load("sound/music.wav")
snake_sound = pygame.mixer.Sound("sound/snake.wav")
win = pygame.mixer.Sound("sound/Win.wav")
lose = pygame.mixer.Sound("sound/lose.wav")
ladder = pygame.mixer.Sound("sound/ladder.wav")

while True:
    game_layout_display.blit(initial_background, (0, 0))
    pygame.display.update()
    time.sleep(11)
    pygame.quit()
