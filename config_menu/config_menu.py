from turtle import back, screensize
import pygame
import sys

pygame.init()

window_dimen = (1000, 1000)

screen = pygame.display.set_mode(window_dimen)
pygame.display.set_caption("Hello World")
background = pygame.Surface(window_dimen)

myFont = pygame.font.SysFont("Roboto", 45)
helloWorld = myFont.render("Hello World", 1, (0, 0, 0), (255, 255, 255))

# draw background
screen.blit(helloWorld, (0, 0))

# colours
cream = (255, 255, 224)
black = (0, 0, 0)
turquoise = (72, 209, 204)
orange = (255, 165, 0)

# game loop
running = True
while running:
    for event in pygame.event.get():
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# https://fonts.google.com/specimen/Silkscreen
