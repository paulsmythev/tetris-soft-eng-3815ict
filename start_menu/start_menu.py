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
window_dimen = (1000, 1000)
screen = pygame.display.set_mode(window_dimen)
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
        title_rect = tetris_title.get_rect(center=(500, 150))
        screen.blit(tetris_title, title_rect)

        # play_button = Button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        
main_menu()
# https://fonts.google.com/specimen/Silkscreen
