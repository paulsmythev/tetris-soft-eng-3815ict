from turtle import back, screensize
import pygame
import sys

# Select normal game or extended game - adds 2 extra blocks to the game 
# select field size
# select AI game - the AI will play the game instead 

pygame.init()

window_dimen = (800, 600)

screen = pygame.display.set_mode(window_dimen)
pygame.display.set_caption("Hello World")
background = pygame.Surface(window_dimen)

myFont = pygame.font.SysFont("Roboto", 45)
helloWorld = myFont.render("Hello World", 1, (0, 0, 0), (255, 255, 255))

# draw background
screen.blit(helloWorld, (0, 0))

# game loop
running = True
while running:
    for event in pygame.event.get():
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# https://fonts.google.com/specimen/Silkscreen
