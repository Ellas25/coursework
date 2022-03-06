import pygame
import set_up
import message_displays
import quit



def centre_button(button_name, xm, ym, x, y, wid, hei, initial_color, after_color, size, type):
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(set_up.game_layout_display, after_color, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if type == 1:
                pass
            elif type == 5:
                return 5
            elif type == 0:
                quit.Quit()
            elif type == "s" or type == 2 or type == 3 or type == 4:
                return type
            elif type == 7:
               pass

            else:
                return True
    else:
        pygame.draw.rect(set_up.game_layout_display, initial_color, [x, y, wid, hei])
    message_displays.message_display_screen(button_name, (x + wid + x) / 2, (y + hei + y) / 2, size)

def side_button(button_name, xm, ym, x, y, wid, hei, intial_colour, after_colour, size):# mouse position
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(set_up.game_layout_display, after_colour, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
                return True
    else:
        pygame.draw.rect(set_up.game_layout_display, intial_colour, [x, y, wid, hei])
    message_displays.message_display_screen(button_name, (x + wid + x) / 2, (y + hei + y) / 2, size)

def play_button(t, xm, ym, x, y, wid, hei, int, after, fast):
    # mouse position
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(set_up.game_layout_display, after, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(set_up.game_layout_display, int, [x, y, wid, hei])
    message_displays.message_display_screen(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)
