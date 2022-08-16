from turtle import back, screensize
import pygame
import sys
from button import Button

pygame.init()

# colours
CREAM = (255, 255, 224)
BLACK = (0, 0, 0)
TURQUOISE = (72, 209, 204)
ORANGE = (255, 165, 0)

# window setup
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)
pygame.display.set_caption("Hello World")
# background = pygame.Surface(window_dimen)

def my_font(font_size):
    return pygame.font.SysFont("Roboto", font_size)

# menu loop
def main_menu():
    running = True
    while running:
        screen.fill(BLACK)
        mouse_pos = pygame.mouse.get_pos()

        # main title
        tetris_title = my_font(200).render("Tetris", True, CREAM)
        title_rect = tetris_title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT*0.15))
        screen.blit(tetris_title, title_rect)

        # instantiating buttons
        play_button = Button("PLAY!", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.3), my_font(100), CREAM)
        configure_button = Button("Configuration", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.45), my_font(70), CREAM)
        credits_button = Button("Credits", (SCREEN_HEIGHT/2, SCREEN_HEIGHT*0.6), my_font(70), CREAM)
        # exit_button = Button()


        buttons = [play_button, configure_button, credits_button]

        for button in buttons:
            button.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        
main_menu()
# https://fonts.google.com/specimen/Silkscreen
