import pygame
import constant
import set_up


def Quit():
    pygame.quit()
    quit()

def main_menu():
    pygame.mixer.music.play(-1)

    m = True
    while m: # while loop  says when m.
        for event in pygame.event.get(): #fetching the items from event queue
            if event.type == pygame.QUIT:
                Quit() # quiting the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit() # clicking KEYDOWN of Escape will trigger the quitting of the game. if you press quit/ escape key it will quit the game

             # mouse position
            mouse = pygame.mouse.get_pos()

            set_up.game_layout_display.blit(set_up.menu_background, (0, 0))
            centre_button("Play", mouse[0], mouse[1], (constant.WIDTH / 2 - 100), constant.HEIGHT / 2, 200, 100, constant.green_color,
                constant.blue_color, 60, 1)

            centre_button("Quit", mouse[0], mouse[1], (constant.WIDTH / 2 - 100), (constant.HEIGHT / 2) + 200, 200, 100,
                constant.red_color, constant.grey_color, 60, 0)

            mouse = pygame.mouse.get_pos()
            if side_button("Mute Music", mouse[0], mouse[1], 1166, 0, 200, 50, constant.red_color, constant.purple_color, 25):
                pygame.mixer.music.pause()
            if side_button("Play Music", mouse[0], mouse[1], 1166, 75, 200, 50, constant.purple_color, constant.blue_color, 25):
                pygame.mixer.music.unpause()
            if side_button("Credits", mouse[0], mouse[1], 1166, 150, 200, 50, constant.grey_color, constant.red_color, 25):
                creditation()
                #pass
            pygame.display.update()


def centre_button(button_name, xm, ym, x, y, wid, hei, initial_color, after_color, size, type):
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(set_up.game_layout_display, after_color, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if type == 1:
                print(type)
            elif type == 5:
                return 5
            elif type == 0:
                Quit()
            elif type == "s" or type == 2 or type == 3 or type == 4:
                return type
            elif type == 7:
                print(type)
            else:
                return True
    else:
        pygame.draw.rect(set_up.game_layout_display, initial_color, [x, y, wid, hei])
    message_display_screen(button_name, (x + wid + x) / 2, (y + hei + y) / 2, size)

def side_button(button_name, xm, ym, x, y, wid, hei, intial_colour, after_colour, size):# mouse position
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(set_up.game_layout_display, after_colour, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
                return True

    else:
        pygame.draw.rect(set_up.game_layout_display, intial_colour, [x, y, wid, hei])
    message_display_screen(button_name, (x + wid + x) / 2, (y + hei + y) / 2, size)

def message_display_screen(text, x, y, size):
    #print(pygame.font.get_fonts())
    name_font = pygame.font.SysFont('comicsansms',size)
    #largeText = pygame.font.Font(, fs)
    TextSurf, TextRect = text_objects_screen(text, name_font)
    TextRect.center = (x, y)
    set_up.game_layout_display.blit(TextSurf, TextRect)

def text_objects_screen(text, font):
    textSurface = font.render(text, True, constant.black_color)
    return textSurface, textSurface.get_rect()

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
        if centre_button("Back", mouse[0], mouse[1], constant.WIDTH / 2 - 100, 700, 200, 50, constant.red_color, constant.white_color, 25, 20):
            main_menu()

        pygame.display.update()