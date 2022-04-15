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


def choice(t):
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
        p1 = p_2 = p_3 = p_4 = best5 = -1
        set_up.game_layout_display.blit(set_up.posts, (0, 0))
        # Single player button

        p_1 = player_button("You vs Robot", mouse[0], mouse[1], (constant.WIDTH / 2 - 150), 250, 300, 50, constant.green_color,
                       constant.blue_green_color, 30, "s")
        # 2 player button
        players_2 = player_button("Duo", mouse[0], mouse[1], (constant.WIDTH / 2) - 150, 350, 300, 50, constant.green_color,
                       constant.blue_green_color, 30, 2)
        # 3 player
        players_3 = player_button("Trio", mouse[0], mouse[1], (constant.WIDTH / 2) - 150, 450, 300, 50, constant.green_color,
                       constant.blue_green_color, 30, 3)
        # 4 player
        players_4 = player_button("4 Players", mouse[0], mouse[1], (constant.WIDTH / 2) - 150, 550, 300, 50, constant.green_color, constant.blue_green_color, 30, 4)
        # Back button
        best5 = player_button("Back", mouse[0], mouse[1], 0, 650, 200, 50, constant.red_color, constant.blue_red_color, 30, 5)
        class best_funct():
             if best5 == 5:
            pass
        if player_1 == "s":
            playing(21)
        if players_2 == 2:
            playing(2)
        if players_3 == 3:
            playing(3)
        if players_4 == 4:
            playing(4)
        pygame.display.update()

def player_button(button_name, xm, ym, x, y, wid, hei, initial_color, after_color, size, type):
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(set_up.game_layout_display, after_color, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if type == 1:
                choice()
            elif type == 5:
                return 5
            elif type == 0:
                pygame.quit()
            elif type == "s" or type == 2 or type == 3 or type == 4:
                return type
            elif type == 7:
                choice()
            else:
                return True
    else:
        pygame.draw.rect(set_up.game_layout_display, initial_color, [x, y, wid, hei])
        message_displays.message_display_screen(button_name, (x + wid + x) / 2, (y + hei + y) / 2, size)



def playing(best):
    best6 = -1
    time = 3000
    #if best6 == 7:
        #choice()
    set_up.game_layout_display.blit(set_up.posts, (0, 0)) #post is a variable loads the image
    set_up.game_layout_display.blit(set_up.mother_board,(350, 35))#loads the board image on the post image
    xcr = xcy = xcg = xcb = 406 - 25 # variables being initiated
    ycr = ycy = ycg = ycb = 606 - 25 # variables being initiated
    set_up.game_layout_display.blit(set_up.teal_c, (xcy, ycy))

    if 5 > best > 1 or best == 21:
        set_up.game_layout_display.blit(set_up.white_c, (xcy, ycy)) # blit is the position and the second is the coordinates

    if 5 > best > 2 or best == 21:
        set_up.game_layout_display.blit(set_up.grey_c, (xcg, ycg))

    if 5 > best > 2:
        set_up.game_layout_display.blit(set_up.purple_c, (xcb, ycb))
    gamer1 = "Player 1"
    gamer1score = 0
    if best == 21:
        gamer2 = "Computer"
        gamer2score = 0
    if 5 > best > 1:
        gamer2 = "Player 2"
        gamer2score = 0
    if 5 > best > 2:
        gamer3 = "Player 3"
        gamer3score = 0
    if 5 > best > 3:
        gamer4 = "Player 4"
        gamer4score = 0
    tips = 1
    play = True
    while True:
        less = False
        set = False
        time = 3000
        set_up.game_layout_display.blit(set_up.posts, (0, 0))
        set_up.game_layout_display.blit(set_up.mother_board, ( 350, 35))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if best == 21:
            if play_button("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, constant.red_color, constant.grey_color, 30):
                if tips == 1:
                    gamer1score, less, set, six = turn(gamer1score, less, set)
                    if not six:
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
                    gamer2score, less, set, six = turn(gamer2score, less, set)
                    xcy, ycy = movement(gamer2score)
                    if not six:
                        tips += 1
                        if best < 3 or best == 21:
                            tips = 1

                    if gamer2score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            message_displays.message_display_screen("Computer Wins", 650, 50, 50, constant.grey_color)
                            pygame.mixer.Sound.play(constant.LOSE_SOUND)
                            pygame.display.update()
                        break
        if 5 > best > 1:
            if play_button("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, constant.red_color, constant.grey_color, 30):
                if tips == 1:
                    gamer1score, less, set, six = turn(gamer1score, less, set)
                    xcr, ycr = movement(gamer1score)
                    if not six:
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
                    gamer2score, less, set, six = turn(gamer2score, less, set)
                    xcy, ycy = movement(gamer2score)
                    if not six:
                        tips += 1
                        if best < 3:
                            tips = 1

                    if gamer2score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            message_displays.message_display1_screen("Player 2 Wins", 650, 50, 50, constant.grey_color)
                            pygame.mixer.Sound.play(constant.WIN_SOUND)
                            pygame.display.update()
                        break

        if 5 > best > 2:
            if play_button("Player 3", mouse[0], mouse[1], 700, 700, 200, 50, constant.green_color, constant.grey_color, 30):
                if tips == 3:
                    gamer3score, less, set, six = turn(gamer3score, less, set)
                    xcg, ycg = movement(gamer3score)
                    if not six:
                        tips += 1
                        if best < 4:
                            tips = 1

                    if gamer3score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            message_displays.message_display1_screen("Player 3 Wins", 650, 50, 50, constant.grey_color)
                            pygame.mixer.Sound.play(constant.WIN_SOUND)
                            pygame.display.update()
                        break

        if 5 > best > 3:
            if play_button("Player 4", mouse[0], mouse[1], 1000, 700, 200, 50, constant.blue_color, constant.grey_color, 30):
                if tips == 4:
                    gamer4score, less, set, six = turn(gamer4score, less, set)
                    xcb, ycb = movement(gamer4score)
                    if not six:
                        tips += 1
                        if best < 5:
                            tips = 1

                    if gamer4score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            message_displays.message_display1_screen("Player 4 Wins", 650, 50, 50, constant.grey_color)
                            pygame.mixer.Sound.play(constant.WIN_SOUND)
                            pygame.display.update()
                        break

        best6 = player_button("Back", mouse[0], mouse[1], 0, 0, 200, 50, constant.red_color, constant.blue_color, 30, 7)
        set_up.game_layout_display.blit(set_up.teal_c, (xcr, ycr))
        if 5 > best > 1 or best == 21:
            set_up.game_layout_display.blit(set_up.white_c, (xcy + 2, ycy))

        if 5 > best > 2:
            set_up.game_layout_display.blit(set_up.grey_c, (xcg + 4, ycg))


        if 5 > best > 3:
            set_up.game_layout_display.blit(set_up.purple_c, (xcb + 6, ycb))

        if less:
            time_clock = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time_clock < 2000:
                message_displays.message_display1_screen("There's a Ladder! Yes you go up the ladder", 650, 50, 35, constant.black_color)
                pygame.display.update()
        if set:
            time_clock = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time_clock < 2000:
                message_displays.message_display_screen("There’s a Snake! Sorry you go down to the bottom of the snake!", 650, 50, 35, constant.black_color)
                pygame.display.update()
          """      
         if powerup:
            time_clock = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time_clock < 2000:
                message_displays.message_display_screen("Yay a powerup", 650, 50, 35, constant.blue_color)
                pygame.display.update()

"""
        time_clocks.tick(7)
        pygame.display.update()


def turn(score, lefted, section):
    d = randint(1, 6)  # player dice roll
    if d == 6:
        six = True
    else:
        six = False
    p = dice(d)
    score += d
    if score <= 100:
        laddle = ladders.ladders(score)  # checking for ladders for player
        if laddle != score:
            lefted = True
            pygame.mixer.Sound.play(set_up.ladder)
            time_clock = pygame.time.get_ticks()
            score = laddle

        sink = Snakes.snakes(score)
        if sink != score:  # checking for snakes for player
            section = True
            pygame.mixer.Sound.play(set_up.snake_sound)
            score = sink

    else:  # checks if player score is not grater than 100
        score -= d
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 1500:
            message_displays.message_display_screen("Can't move!", 650, 50, 35, constant.green_color)
            pygame.display.update()
    return score, lefted, section, six




