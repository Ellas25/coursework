import pygame
import set_up
import message_displays
import quit

"""

class centre_button()
#button_name, xm, ym, x, y, wid, hei, initial_color, after_color, size, type):
def __init__( xm, ym, x, y, wid, hei, initial_color, after_color, size, type, bg="blue"):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Comic Sans", font)
        if buttons == "":
            self. = "text"
        else:
           self.buttons = feedback
        self.change_text(text, bg)
        def change_text(self, text, bg="black"):
        
        self.text = self.font.render(text, 1, set_up.pygame.Color())
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Oval(self.x, self.y, self.size[0], self.size[1])
 
    def butts(self):
        screen.blit(button1.surface, (self.x, self.y))
 
    def clicks_on_button(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")   
 
 
def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button1.click(event)
        button1.show()
        clock.tick(30)
        pygame.display.update()
 
 
button1 = Button(
    "Click here",
    (100, 100),
    font=30,
    bg="navy",
    feedback="You clicked me")
  

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
"""

"""
class buttons_side():
#button_name, xm, ym, x, y, wid, hei, initial_color, after_color, size, type):
def __init__( xm, ym, x, y, wid, hei, initial_color, after_color, size, type, bg="blue"):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Comic Sans", font)
        if buttons == "":
            self. = "text"
        else:
           self.buttons = feedback
        self.change_text(text, bg)
        def change_text(self, text, bg="black"):
        
        self.text = self.font.render(text, 1, set_up.pygame.Color())
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Oval(self.x, self.y, self.size[0], self.size[1])
 
    def butts(self):
        screen.blit(button1.surface, (self.x, self.y))
 
    def clicks_on_button(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
 
 
def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button1.click(event)
        button1.show()
        clock.tick(30)
        pygame.display.update()
 
 
button1 = Button(
    "Click here",
    (100, 100),
    font=30,
    bg="navy",
    feedback="You clicked me")

class play_the_button()
#button_name, xm, ym, x, y, wid, hei, initial_color, after_color, size, type):
def __init__( xm, ym, x, y, wid, hei, initial_color, after_color, size, type, bg="blue"):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Comic Sans", font)
        if buttons == "":
            self. = "text"
        else:
           self.buttons = feedback
        self.change_text(text, bg)
        def change_text(self, text, bg="black"):
        
        self.text = self.font.render(text, 1, set_up.pygame.Color())
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Oval(self.x, self.y, self.size[0], self.size[1])
 
    def butts(self):
        screen.blit(button1.surface, (self.x, self.y))
 
    def clicks_on_button(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
 
 
def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button1.click(event)
        button1.show()
        clock.tick(30)
        pygame.display.update()
 
 
button1 = Button(
    "Click here",
    (100, 100),
    font=30,
    bg="navy",
    feedback="You clicked me")
    """

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










