from turtle import back, screensize
import pygame
import sys


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

myFont = pygame.font.SysFont("Roboto", 45)
helloWorld = myFont.render("Hello World", 1, (0, 0, 0), (255, 255, 255))

# draw a test to screen
screen.blit(helloWorld, (0, 0))

# menu loop
def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

main_menu()
# https://fonts.google.com/specimen/Silkscreen
