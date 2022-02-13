import pygame
import main_menu
import start_page
import set_up
import constant
import buttons

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


def choice():
    f = True
    while f == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        player_1 = players_2 = players_3 = players_4 = best5 = -1
        set_up.game_layout_display.blit(constant.BOARD, (0, 0))
        # Single player button

        player_1 = buttons.centre_button("Single Player", mouse[0], mouse[1], (constant.WIDTH / 2 - 150), 250, 300, 50, constant.green_color,
                       constant.blue_green_color, 30, "s")
        # 2 player button
        players_2 = buttons.centre_button("2 Players", mouse[0], mouse[1], (constant.WIDTH / 2) - 150, 350, 300, 50, constant.green_color,
                       constant.blue_green_color, 30, 2)
        # 3 player
        players_3 = buttons.centre_button("3 Players", mouse[0], mouse[1], (constant.WIDTH / 2) - 150, 450, 300, 50, constant.green_color,
                       constant.blue_green_color, 30, 3)
        # 4 player
        players_4 = buttons.centre_button("4 Players", mouse[0], mouse[1], (constant.WIDTH / 2) - 150, 550, 300, 50, constant.green_color, constant.blue_green_color, 30, 4)
        # Back button
        best5 = buttons.centre_button("Back", mouse[0], mouse[1], 0, 650, 200, 50, constant.red_color, constant.blue_red_color, 30, 5)


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


def playing(best):
    best6 = -1
    time = 3000
    if best6 == 7:
        choice()
    set_up.game_layout_display.blit(posts, (0, 0))
    set_up.game_layout_display.blit(constant.BOARD, (constant.WIDTH / 2 - 250, constant.HEIGHT / 2 - 250))
    xcr = xcy = xcg = xcb = 406 - 25
    ycr = ycy = ycg = ycb = 606 - 25
    set_up.game_layout_display.blit(constant.COUNTER_RED_IMAGE_NAME, (xcy, ycy))
    if 5 > best > 1 or best == 21:
        set_up.game_layout_display.blit(constant.COUNTER_YELLOW_IMAGE_NAME, (xcy, ycy))

    if 5 > best > 2 or best == 21:
        set_up.game_layout_display.blit(constant.COUNTER_GREEN_IMAGE_NAME, (xcg, ycg))

    if 5 > best > 2:
        set_up.game_layout_display.blit(constant.COUNTER_BLUE_IMAGE_NAME, (xcb, ycb))
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
        set_up.game_layout_display.blit(posts, (0, 0))
        set_up.game_layout_display.blit(constant.BOARD, (constant.WIDTH / 2 - 250, constant.HEIGHT / 2 - 250))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    if best == 21:
        if button_1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, constant.red_color, constant.grey_color, 30):
            if tips == 1:
                gamer1score, less, set, six = turn(gamer1score, less, set)
                if not six:
                    tips += 1
                xcr, ycr = movement(gamer1score)
                if gamer1score == 100:
                    time = pygame.time.get_ticks()
                    while pygame.time.get_ticks() - time < 2000:
                        constant.BOARD("Player 1 Wins", 650, 50, 50, constant.blue_color)
                        # constant.message_display1_screen("Player 1 Wins", 650, 50, 50, constant.blue_color)
                        pygame.mixer.Sound.play(win)
                        pygame.display.update()
                    break

        button_1("Computer", mouse[0], mouse[1], 400, 700, 200, 50, constant.yellow_color, constant.grey_color, 30)
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
                        constant.BOARD("Computer Wins", 650, 50, 50, constant.black_color)
                        # constant.message_display1_screen("Computer Wins", 650, 50, 50, constant.black_color)
                        pygame.mixer.Sound.play()
                        pygame.display.update()
                    break
    if 5 > best > 1:
        if button_1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, constant.red_color, constant.grey_color, 30):
            if tips == 1:
                gamer1score, less, set, six = turn(gamer1score, less, set)
                xcr, ycr = movement(gamer1score)
                if not six:
                    tips += 1
                if gamer1score == 100:
                    time_clock = pygame.time.get_ticks()
                    while pygame.time.get_ticks() - time_clock < 2000:
                        constant.BOARD("Player 1 Wins", 650, 50, 50, constant.black_color)
                        # constant.message_display1_screen("Player 1 Wins", 650, 50, 50, constant.black_color)
                        pygame.mixer.Sound.play(win)
                        pygame.display.update()
                        break

        if button_1("Player 2", mouse[0], mouse[1], 400, 700, 200, 50, constant.yellow_color, constant.grey_color, 30):
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
                        constant.BOARD("Player 2 Wins", 650, 50, 50, constant.black_color)
                        # constant.message_display1_screen("Player 2 Wins", 650, 50, 50, constant.black_color)
                        pygame.mixer.Sound.play(win)
                        pygame.display.update()
                        break

    if 5 > best > 2:
        if button_1("Player 3", mouse[0], mouse[1], 700, 700, 200, 50, constant.green_color, constant.grey_color, 30):
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
                        constant.BOARD("Player 3 Wins", 650, 50, 50, constant.black_color)
                        # constant.message_display1_screen("Player 3 Wins", 650, 50, 50, constant.black_color)
                        pygame.mixer.Sound.play(win)
                        pygame.display.update()
                        break

    if 5 > best > 3:
        if button_1("Player 4", mouse[0], mouse[1], 1000, 700, 200, 50, constant.blue_color, constant.grey_color, 30):
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
                        constant.BOARD("Player 4 Wins", 650, 50, 50, constant.black_color)
                        # constant.message_display1_screen("Player 4 Wins", 650, 50, 50, constant.black_color)
                        pygame.mixer.Sound.play(win)
                        pygame.display.update()
                        break

    best6 = button("Back", mouse[0], mouse[1], 0, 0, 200, 50, constant.red_color, constant.blue_red_color, 30, 7)
    set_up.game_layout_display.blit(constant.red_color, (xcr, ycr))
    if 5 > best > 1 or best == 21:
        set_up.game_layout_display.blit(constant.yellow_color, (xcy + 2, ycy))

    if 5 > best > 2:
        set_up.game_layout_display.blit(constant.green_color, (xcg + 4, ycg))

    if 5 > best > 3:
        set_up.game_layout_display.blit(constant.blue_color, (xcb + 6, ycb))

    if less:
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 2000:
            constant.BOARD("a Ladder!", 650, 50, 35, constant.black_color)
            # constant.message_display1_screen("There's a Ladder!", 650, 50, 35, constant.black_color)
            pygame.display.update()

    if set:
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 2000:
            constant.BOARD(" a Snake!", 650, 50, 35, constant.black_color)
            # constant.message_display1_screen("There's a Snake!", 650, 50, 35, constant.black_color)
            pygame.display.update()



