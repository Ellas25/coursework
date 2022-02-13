import pygame
import set_up
def introduction():
    time_clock = pygame.time.get_ticks()

    while pygame.time.get_ticks() - time_clock < 2500:
        set_up.game_layout_display.blit(set_up.initial_background, (0, 0))
        pygame.display.update()

    while True:
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            set_up.game_layout_display.blit(set_up.initial_background2, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()

        while pygame.time.get_ticks() - time_clock < 500:
            set_up.game_layout_display.blit(set_up.initial_background3, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()

        while pygame.time.get_ticks() - time_clock < 500:
                set_up.game_layout_display.blit(set_up.initial_background4, (0, 0))
                pygame.display.update()
        time_clock = pygame.time.get_ticks()

        while pygame.time.get_ticks() - time_clock < 500:
                    set_up.game_layout_display.blit(set_up.initial_background5, (0, 0))
                    pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
        pygame.display.update()