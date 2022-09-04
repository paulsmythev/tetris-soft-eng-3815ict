import pygame
import json
from start_menu.button import Button
from top_score.file_handler import readJson

class topScoreScreen():
    def __init__(self):

        topScoresArray = []
        concatArray = []

        try:
            topScoresImport = readJson()
        except:
            print("cant load JSON")

        #writes each line to array
        for x in topScoresImport:
            topScoresArray.append(x)

        for x in range(len(topScoresArray)):
            brk = json.dumps(topScoresArray[x])
            test = json.loads(brk)
            strName = test["name"]
            strScore = "{:,}".format(test["score"])
            concatArray.append(strName + " - " + strScore)

        number_image = (50, 50)
        font_color = (255, 255, 224)

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

        #Fill the background
        background = pygame.Surface(size)
        background = background.convert()
        background.fill((250,250,250))

        #Header text and image
        try: 
            header_image = pygame.transform.smoothscale(header_image, (225, 175))
            screen.blit(header_image, (135, 8))
        except:
            print("Error loading image file")
        font = pygame.font.Font(None, 100)
        text = font.render("Top 10 Scores", 1, font_color)
        screen.blit(text, (390, 80))

        #Blit everything to screen
        try:
            score1 = pygame.transform.smoothscale(score1, number_image)
            screen.blit(score1, (200, 200))
            score2 = pygame.transform.smoothscale(score2, number_image)
            screen.blit(score2, (200, 270))
            score3 = pygame.transform.smoothscale(score3, number_image)
            screen.blit(score3, (200, 340))
            score4 = pygame.transform.smoothscale(score4, number_image)
            screen.blit(score4, (200, 410))
            score5 = pygame.transform.smoothscale(score5, number_image)
            screen.blit(score5, (200, 480))
            score6 = pygame.transform.smoothscale(score6, number_image)
            screen.blit(score6, (200, 550))
            score7 = pygame.transform.smoothscale(score7, number_image)
            screen.blit(score7, (200, 620))
            score8 = pygame.transform.smoothscale(score8, number_image)
            screen.blit(score8, (200, 690))
            score9 = pygame.transform.smoothscale(score9, number_image)
            screen.blit(score9, (200, 760))
            score10 = pygame.transform.smoothscale(score10, number_image)
            screen.blit(score10, (200, 830))
        except:
            print("Error loading image files")

        #Display some text, 42 spacing
        font = pygame.font.Font(None, 50)
        spacing = 210
        for x in range(len(concatArray)):
            text = font.render(concatArray[x], 1, font_color)
            screen.blit(text, (275, spacing))
            spacing += 70

        #close button
        font_button = pygame.font.Font(None, 80)
        close_button = Button("Close", (490, 925), font_button, font_color)
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