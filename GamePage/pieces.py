import pygame
pygame.init()

I = [
    [[0,0,0,0],
     [1,1,1,1],
     [0,0,0,0],
     [0,0,0,0]],

    [[0,0,1,0],
     [0,0,1,0],
     [0,0,1,0],
     [0,0,1,0]],

    [[0,0,0,0],
     [0,0,0,0],
     [1,1,1,1],
     [0,0,0,0]],

    [[0,1,0,0],
     [0,1,0,0],
     [0,1,0,0],
     [0,1,0,0]]
]

L = [
    [[0,0,1],
     [1,1,1],
     [0,0,0]],
    
    [[0,1,0],
     [0,1,0],
     [0,1,1]],
    
    [[0,0,0],
     [1,1,1],
     [1,0,0]],
    
    [[1,1,0],
     [0,1,0],
     [0,1,0]]
]

J = [
    [[1,0,0],
     [1,1,1],
     [0,0,0]],
    
    [[0,1,1],
     [0,1,0],
     [0,1,0]],
    
    [[0,0,0],
     [1,1,1],
     [0,0,1]],
    
    [[0,1,0],
     [0,1,0],
     [1,1,0]]
]
O = [
    [[0,1,1,0],
     [0,1,1,0],
     [0,0,0,0],
     [0,0,0,0]],
    
    [[0,1,1,0],
     [0,1,1,0],
     [0,0,0,0],
     [0,0,0,0]],
    
    [[0,1,1,0],
     [0,1,1,0],
     [0,0,0,0],
     [0,0,0,0]],
    
    [[0,1,1,0],
     [0,1,1,0],
     [0,0,0,0],
     [0,0,0,0]]
]

S = [
    [[0,1,1],
     [1,1,0],
     [0,0,0]],
    
    [[0,1,0],
     [0,1,1],
     [0,0,1]],
    
    [[0,0,0],
     [0,1,1],
     [1,1,0]],
    
    [[1,0,0],
     [1,1,0],
     [0,1,0]]
]

Z = [
    [[1,1,0],
     [0,1,1],
     [0,0,0]],
    
    [[0,0,1],
     [0,1,1],
     [0,1,0]],
    
    [[0,0,0],
     [1,1,0],
     [0,1,1]],
    
    [[0,1,0],
     [1,1,0],
     [1,0,0]]
]

T = [
    [[0,1,0],
     [1,1,1],
     [0,0,0]],
    
    [[0,1,0],
     [0,1,1],
     [0,1,0]],
    
    [[0,0,0],
     [1,1,1],
     [0,1,0]],
    
    [[0,1,0],
     [1,1,0],
     [0,1,0]]
]

cyan = (0, 255, 255)
blue = (0, 0, 255)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
purple = (128, 0, 128)
red = (255, 0, 0)

cyanBlock = pygame.transform.scale(pygame.image.load('GamePage/images/cyan.png'), (38, 38))
blueBlock = pygame.transform.scale(pygame.image.load('GamePage/images/blue.png'), (38, 38))
orangeBlock = pygame.transform.scale(pygame.image.load('GamePage/images/orange.png'), (38, 38))
yellowBlock = pygame.transform.scale(pygame.image.load('GamePage/images/yellow.png'), (38, 38))
greenBlock = pygame.transform.scale(pygame.image.load('GamePage/images/green.png'), (38, 38))
purpleBlock = pygame.transform.scale(pygame.image.load('GamePage/images/purple.png'), (38, 38))
redBlock = pygame.transform.scale(pygame.image.load('GamePage/images/red.png'), (38, 38))

options = [I,L,J,O,S,T,Z]
colours = [cyan, blue, orange, yellow, green, purple, red]
images = [cyanBlock, blueBlock, orangeBlock, yellowBlock, greenBlock, purpleBlock, redBlock]