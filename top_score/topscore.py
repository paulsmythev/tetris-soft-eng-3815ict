import json
import pygame

from top_score.fileload import fileLoad, loadJson
from start_menu.button import Button

class topScore():
    def __init__():
        print()

def topScore_displayPage():
    #Handles reading and converting JSON to array
    topScoresArray = []
    concatArray = []

    concatArray = loadJson()

    #import images
    try:
        score1 = pygame.image.load('top_score/images/number-one-round-icon.png')
        score2 = pygame.image.load('top_score/images/number-two-round-icon.png')
        score3 = pygame.image.load('top_score/images/number-three-round-icon.png')
        score4 = pygame.image.load('top_score/images/number-four-round-icon.png')
        score5 = pygame.image.load('top_score/images/number-five-round-icon.png')
        score6 = pygame.image.load('top_score/images/number-six-round-icon.png')
        score7 = pygame.image.load('top_score/images/number-seven-round-icon.png')
        score8 = pygame.image.load('top_score/images/number-eight-round-icon.png')
        score9 = pygame.image.load('top_score/images/number-nine-round-icon.png')
        score10 = pygame.image.load('top_score/images/number-ten-round-icon.png')

        header_image = pygame.image.load('top_score/images/1305624857.png')
    except:
        print("Error loading image files")

    # Initialise the screen
    pygame.init()
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    pygame.display.update()
    pygame.display.set_caption('Tetris - Top Scores')

    #stopped flashing here

    #Fill the background
    background = pygame.Surface(size)
    background = background.convert()
    background.fill((250,250,250))

    #Header text and image
    try: 
        header_image = pygame.transform.smoothscale(header_image, (32, 32))
        screen.blit(header_image, (135, 8))
    except:
        print("Error loading image file")
    font = pygame.font.Font(None, 32)
    text = font.render("Top 10 Scores", 1, (255, 255, 255))
    screen.blit(text, (170, 14))

    #Blit everything to screen
    try:
        score1 = pygame.transform.smoothscale(score1, (32, 32))
        screen.blit(score1, (32, 42))
        score2 = pygame.transform.smoothscale(score2, (32, 32))
        screen.blit(score2, (32, 84))
        score3 = pygame.transform.smoothscale(score3, (32, 32))
        screen.blit(score3, (32, 126))
        score4 = pygame.transform.smoothscale(score4, (32, 32))
        screen.blit(score4, (32, 168))
        score5 = pygame.transform.smoothscale(score5, (32, 32))
        screen.blit(score5, (32, 210))
        score6 = pygame.transform.smoothscale(score6, (32, 32))
        screen.blit(score6, (32, 252))
        score7 = pygame.transform.smoothscale(score7, (32, 32))
        screen.blit(score7, (32, 294))
        score8 = pygame.transform.smoothscale(score8, (32, 32))
        screen.blit(score8, (32, 336))
        score9 = pygame.transform.smoothscale(score9, (32, 32))
        screen.blit(score9, (32, 378))
        score10 = pygame.transform.smoothscale(score10, (32, 32))
        screen.blit(score10, (32, 419))
    except:
        print("Error loading image files")

    #Display some text, 42 spacing
    font = pygame.font.Font(None, 32)
    spacing = 48
    for x in range(len(concatArray)):
        text = font.render(concatArray[x], 1, (255, 255, 255))
        screen.blit(text, (74, spacing))
        spacing += 42

    #close button
    close_button = Button("Close", (185, 485), font, (255, 255, 255))
    close_button.update(screen)

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.checkInput(mouse_pos):
                    running = False

        pygame.display.flip()