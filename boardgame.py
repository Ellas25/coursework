import pygame
import set_up

import constant
from random import randint

import ladders
import Snakes
import message_displays

from movements import movement
#import dice
import movements
from buttons import play_button

time_clocks = pygame.time.Clock()


def dice(d):
   if d == 1:
       d = set_up.d1
   elif d == 2:
       d = set_up.d2
   elif d == 3:
       d = set_up.d3
   elif d == 4:
       d = set_up.d4
   elif d == 5:
       d = set_up.d5
   elif d == 6:
       d = set_up.d6

   time_clock = pygame.time.get_ticks() #fetches the time
   while pygame.time.get_ticks() - time_clock < 1000: #1000 milli seconds loads the image
       set_up.game_layout_display.blit(d, (300, 500)) # shows the image of the number
       pygame.display.update() # updates the image on the screen


def choice():
   t = True
   while t == True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()

     
       mouse = pygame.mouse.get_pos()
       click = pygame.mouse.get_pressed()
       p_1 = p_2 = p_3 = p_4 = best5 = -1
       set_up.game_layout_display.blit(set_up.posts, (0, 0))
       # Single player button

       p_1 = player_button("You vs Robot", mouse[0], mouse[1], (constant.WIDTH / 2 - 150), 250, 300, 50, constant.green_color,
                      constant.teal, 30, 1)
       # 2 player button
       p_2 = player_button("Duo", mouse[0], mouse[1], (constant.WIDTH / 2) - 25, 300, 300, 50, constant.teal,
                      constant.lime, 30, 2)
       # 3 player
       p_3 = player_button("Trio", mouse[0], mouse[1], (constant.WIDTH / 2) - 25, 400, 300, 50, constant.lime ,
                      constant.teal, 30, 3)
       # 4 player
       p_4 = player_button("4 Players", mouse[0], mouse[1], (constant.WIDTH / 2) - 25, 500, 300, 50, constant.teal, constant.lime, 30, 4)
       # Back button
       best5 = player_button("Back", mouse[0], mouse[1], 0, 650, 200, 50, constant.red_color, constant.blue_red_color, 30, 5)
       class best_funct():
           if best5 == 5:
               pass
           if p_1 == 1:
               game_play(1)
           if p_2 == 2:
               game_play(2)
           if p_3 == 3:
               game_play(3)
           if p_4 == 4:
               game_play(4)
       pygame.display.update()

def player_button(button_name, xm, ym, x, y, wid, hei, initial_color, after_color, size, type):
   if x + wid > xm > x and y + hei > ym > y:
       pygame.draw.rect(set_up.game_layout_display, after_color, [x - 2.5, y - 2.5, wid + 5, hei + 5])
       if pygame.mouse.get_pressed() == (1, 0, 0):
           if type == 'p':
               choice()
           elif type == 5:
               return 5
           elif type == 'q':
               pygame.quit()
           elif type == 1 or type == 2 or type == 3 or type == 4:
               return type
           elif type == 7:
               choice()
           else:
               return True
   else:
       pygame.draw.rect(set_up.game_layout_display, initial_color, [x, y, wid, hei])
       message_displays.message_display_screen(button_name, (x + wid + x) / 2, (y + hei + y) / 2, size)



def game_play(user):
   time = 3000
   set_up.game_layout_display.blit(set_up.posts, (0, 0)) #post is a variable loads the image
   set_up.game_layout_display.blit(set_up.mother_board,(350, 35))#loads the board image on the post image
   xcr = xcy = xcg = xcb = 200 # variables being initiated
   ycr = ycy = ycg = ycb = 600 # variables being initiated
   set_up.game_layout_display.blit(set_up.teal_c, (xcy, ycy))

   if 5 > user > 1 or user == 1:
       y_cor = 500
       set_up.game_layout_display.blit(set_up.white_c, (xcy, y_cor)) # blit is the position and the second is the coordinates

   if 5 > user > 2 or user == 1:
       yg_cor = 400
       set_up.game_layout_display.blit(set_up.grey_c, (xcg, yg_cor))

   if 5 > user > 2:
       yb_cor = 300
       set_up.game_layout_display.blit(set_up.purple_c, (xcb, yb_cor))
   gamer1 = "Player 1"
   gamer1score = 0
   if user == 1:
       gamer2 = "Computer"
       gamer2score = 0
   if 5 > user > 1:
       gamer2 = "Player 2"
       gamer2score = 0
   if 5 > user > 2:
       gamer3 = "Player 3"
       gamer3score = 0
   if 5 > user > 3:
       gamer4 = "Player 4"
       gamer4score = 0
   tips = 1
   play = True
   while True:
       is_ladder = is_snake = False
       time = 3000
       set_up.game_layout_display.blit(set_up.posts, (0, 0))
       set_up.game_layout_display.blit(set_up.mother_board, (350, 35))
       mouse = pygame.mouse.get_pos()

       for event in pygame.event.get():

           if event.type == pygame.QUIT:
               pygame.quit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
       if user == 1:
           if play_button("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, constant.teal, constant.grey_color, 30):
               if tips == 1:
                   gamer1score, is_ladder, is_snake, rolled_six = roll_dice(gamer1score)
                   if not rolled_six:
                       tips += 1
                   xcr, ycr = movement(gamer1score)
                   if gamer1score == 100:
                       time = pygame.time.get_ticks()
                       while pygame.time.get_ticks() - time < 2000:
                           message_displays.message_display_screen("Player 1 Wins", 650, 50, 50, constant.grey_color)
                           pygame.mixer.Sound.play(constant.WIN_SOUND)
                           pygame.display.update()
                       break
                      
           play_button("Computer", mouse[0], mouse[1], 400, 700, 200, 50, constant.yellow_color, constant.grey_color, 30)
           if True:
               if tips == 2:
                   gamer2score, is_ladder, is_snake, rolled_six = roll_dice(gamer2score)
                   xcy, ycy = movement(gamer2score)
                   if not rolled_six:
                       tips += 1
                       if user < 3 or user == 1:
                           tips = 1

                   if gamer2score == 100:
                       time_clock = pygame.time.get_ticks()
                       while pygame.time.get_ticks() - time_clock < 2000:
                           message_displays.message_display_screen("Computer Wins", 650, 50, 50, constant.grey_color)
                           pygame.mixer.Sound.play(constant.LOSE_SOUND)
                           pygame.display.update()
                       break
       if 5 > user > 1:
           if play_button("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, constant.red_color, constant.grey_color, 30):
               if tips == 1:
                   gamer1score, is_ladder, is_snake, rolled_six = roll_dice(gamer1score)
                   xcr, ycr = movement(gamer1score)
                   if not rolled_six:
                       tips += 1
                   if gamer1score == 100:
                       time_clock = pygame.time.get_ticks()
                       while pygame.time.get_ticks() - time_clock < 2000:
                           message_displays.message_display1_screen("Player 1 Wins", 650, 50, 50, constant.grey_color)
                           pygame.mixer.Sound.play(constant.WIN_SOUND)
                           pygame.display.update()
                       break

           if play_button("Player 2", mouse[0], mouse[1], 400, 700, 200, 50, constant.yellow_color, constant.grey_color, 30):
               if tips == 2:
                   gamer2score, is_ladder, is_snake, rolled_six = roll_dice(gamer2score)
                   xcy, ycy = movement(gamer2score)
                   if not rolled_six:
                       tips += 1
                       if user < 3:
                           tips = 1

                   if gamer2score == 100:
                       time_clock = pygame.time.get_ticks()
                       while pygame.time.get_ticks() - time_clock < 2000:
                           message_displays.message_display1_screen("Player 2 Wins", 650, 50, 50, constant.grey_color)
                           pygame.mixer.Sound.play(constant.WIN_SOUND)
                           pygame.display.update()
                       break

       if 5 > user > 2:
           if play_button("Player 3", mouse[0], mouse[1], 700, 700, 200, 50, constant.green_color, constant.grey_color, 30):
               if tips == 3:
                   gamer3score, is_ladder, is_snake, rolled_six = roll_dice(gamer3score)
                   xcg, ycg = movement(gamer3score)
                   if not rolled_six:
                       tips += 1
                       if user < 4:
                           tips = 1

                   if gamer3score == 100:
                       time_clock = pygame.time.get_ticks()
                       while pygame.time.get_ticks() - time_clock < 2000:
                           message_displays.message_display1_screen("Player 3 Wins", 650, 50, 50, constant.grey_color)
                           pygame.mixer.Sound.play(constant.WIN_SOUND)
                           pygame.display.update()
                       break

       if 5 > user > 3:
           if play_button("Player 4", mouse[0], mouse[1], 1000, 700, 200, 50, constant.blue_color, constant.grey_color, 30):
               if tips == 4:
                   gamer4score, is_ladder, is_snake, rolled_six = roll_dice(gamer4score)
                   xcb, ycb = movement(gamer4score)
                   if not rolled_six:
                       tips += 1
                       if user < 5:
                           tips = 1

                   if gamer4score == 100:
                       time_clock = pygame.time.get_ticks()
                       while pygame.time.get_ticks() - time_clock < 2000:
                           message_displays.message_display1_screen("Player 4 Wins", 650, 50, 50, constant.grey_color)
                           pygame.mixer.Sound.play(constant.WIN_SOUND)
                           pygame.display.update()
                       break

       player_button("Back", mouse[0], mouse[1], 0, 0, 200, 50, constant.red_color, constant.blue_color, 30, 7)
       set_up.game_layout_display.blit(set_up.teal_c, (xcr, ycr))
       if 5 > user > 1 or user == 1:
           set_up.game_layout_display.blit(set_up.white_c, (xcy + 2, 500))

       if 5 > user > 2:
           set_up.game_layout_display.blit(set_up.grey_c, (xcg + 4, 400))


       if 5 > user > 3:
           set_up.game_layout_display.blit(set_up.purple_c, (xcb + 6, 300))

       if is_ladder:
           time_clock = pygame.time.get_ticks()
           while pygame.time.get_ticks() - time_clock < 2000:
               message_displays.message_display1_screen("There's a Ladder! Yes you go up the ladder", 650, 50, 35, constant.black_color)
               pygame.display.update()
       if is_snake:
           time_clock = pygame.time.get_ticks()
           while pygame.time.get_ticks() - time_clock < 2000:
               message_displays.message_display_screen("There’s a Snake! Sorry you go down to the bottom of the snake!", 650, 50, 35, constant.black_color)
               pygame.display.update()
       time_clocks.tick(7)
       pygame.display.update()
"""     
        if powerup:
           time_clock = pygame.time.get_ticks()
           while pygame.time.get_ticks() - time_clock < 2000:
               message_displays.message_display_screen("Yay a powerup", 650, 50, 35, constant.blue_color)
               pygame.display.update()
"""

def roll_dice(player_score):
   dice_face = randint(1, 6)  # player dice roll
   rolled_six = False
   if dice_face == 6:
       rolled_six = True
   p = dice(dice_face)
   player_score += dice_face
   if player_score <= 100:
       updated_score, is_ladder = ladders.ladders(player_score)  # checking for ladders for player
       if is_ladder:
           pygame.mixer.Sound.play(set_up.ladder)
           time_clock = pygame.time.get_ticks()
           player_score = updated_score

       updated_score, is_snake = Snakes.snakes(player_score)
       if is_snake:  # checking for snakes for player
           pygame.mixer.Sound.play(set_up.snake_sound)
           player_score = updated_score

   else:  # checks if player score is not grater than 100
       player_score -= dice_face
       time_clock = pygame.time.get_ticks()
       while pygame.time.get_ticks() - time_clock < 1500:
           message_displays.message_display_screen("Can't move!", 650, 50, 35, constant.green_color)
           pygame.display.update()
   return player_score, is_ladder, is_snake, rolled_six







