import pygame
import constant
import set_up

import quit
import buttons
#import message_displays

#import boardgame

from boardgame import player_button

def main_menu():
    pygame.mixer.music.play(-1)

    m = True
    while m: # while loop  says when m.
        for event in pygame.event.get(): #fetching the items from event queue
            if event.type == pygame.QUIT:
                quit.Quit() # quiting the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit.Quit() # clicking KEYDOWN of Escape will trigger the quitting of the game. if you press quit/ escape key it will quit the game

             # mouse position
            mouse = pygame.mouse.get_pos()

            set_up.game_layout_display.blit(set_up.menu_background, (0, 0))
            player_button("Play", mouse[0], mouse[1], (constant.WIDTH / 2 - 100), constant.HEIGHT / 2, 200, 100, constant.purple_color,
                constant.green_color, 60, 1)

            player_button("Quit", mouse[0], mouse[1], (constant.WIDTH / 2 - 100), (constant.HEIGHT / 2) + 200, 200, 100,
                constant.red_color, constant.grey_color, 60, 0)

            mouse = pygame.mouse.get_pos()
            if buttons.side_button("Mute Music", mouse[0], mouse[1], 1166, 0, 200, 50, constant.red_color, constant.purple_color, 25):
                pygame.mixer.music.pause()
            if buttons.side_button("Play Music", mouse[0], mouse[1], 1166, 75, 200, 50, constant.purple_color, constant.grey, 25):
                pygame.mixer.music.unpause()
            if buttons.side_button("Credits", mouse[0], mouse[1], 1166, 150, 200, 50, constant.grey_color, constant.red_color, 25):
                creditation()
                #pass
            pygame.display.update()







def creditation():
    while True:
        set_up.game_layout_display.blit(set_up.copyrights, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if buttons.centre_button("Back", mouse[0], mouse[1], constant.WIDTH / 2 - 100, 700, 200, 50, constant.grey_color, constant.white_color, 25, 20):
            main_menu()

        pygame.display.update()
