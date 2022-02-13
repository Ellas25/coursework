#start

import pygame

black_color = (10, 10, 10)
green_color = (0, 200, 0)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.Font("fonts/Qarolina.ttf", 21)

while True:
    screen.fill(black_color)

    for events in pygame.event.get():  # look at all events
        if events.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            text = font.render(f"{mouse_position[0]}, {mouse_position[1]}", True, green_color)
            textRect = text.get_rect()
            textRect.center = (1280/2, 720/2)
            screen.blit(text, textRect)
            pygame.display.update()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                pygame.quit()

#end

