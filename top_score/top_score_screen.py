#Class is responsible for showing the top 10 scores list printed to the screen and with images
import pygame
import json
from start_menu.button import Button
from top_score.file_handler import FileHandler

NUMBER_IMAGE = (50, 50)
FONT_COLOR = (255, 255, 224)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

class TopScoreScreen:
    def screen(self):

        top_scores_array = []
        concat_array = []

        #calls file_handler to loading json data
        try:
            get_file = FileHandler()
            top_scores_import = get_file.read_json()
        except:
            print("cant load JSON")

        #writes each line to array
        for x in top_scores_import:
            top_scores_array.append(x)

        #Formats the names and scores to be displayed 
        for x in range(len(top_scores_array)):
            brk = json.dumps(top_scores_array[x])
            test = json.loads(brk)
            str_name = test["name"]
            str_score = "{:,}".format(test["score"])
            concat_array.append(str_name + " - " + str_score)

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
        size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
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
        text = font.render("Top 10 Scores", 1, FONT_COLOR)
        screen.blit(text, (390, 80))

        #Blit everything to screen
        try:
            score1 = pygame.transform.smoothscale(score1, NUMBER_IMAGE)
            screen.blit(score1, (250, 200))
            score2 = pygame.transform.smoothscale(score2, NUMBER_IMAGE)
            screen.blit(score2, (250, 270))
            score3 = pygame.transform.smoothscale(score3, NUMBER_IMAGE)
            screen.blit(score3, (250, 340))
            score4 = pygame.transform.smoothscale(score4, NUMBER_IMAGE)
            screen.blit(score4, (250, 410))
            score5 = pygame.transform.smoothscale(score5, NUMBER_IMAGE)
            screen.blit(score5, (250, 480))
            score6 = pygame.transform.smoothscale(score6, NUMBER_IMAGE)
            screen.blit(score6, (250, 550))
            score7 = pygame.transform.smoothscale(score7, NUMBER_IMAGE)
            screen.blit(score7, (250, 620))
            score8 = pygame.transform.smoothscale(score8, NUMBER_IMAGE)
            screen.blit(score8, (250, 690))
            score9 = pygame.transform.smoothscale(score9, NUMBER_IMAGE)
            screen.blit(score9, (250, 760))
            score10 = pygame.transform.smoothscale(score10, NUMBER_IMAGE)
            screen.blit(score10, (250, 830))
        except:
            print("Error loading image files")

        #Display some text, 42 spacing
        font = pygame.font.Font(None, 50)
        spacing = 210
        for x in range(len(concat_array)):
            text = font.render(concat_array[x], 1, FONT_COLOR)
            screen.blit(text, (325, spacing))
            spacing += 70

        #close button
        font_button = pygame.font.Font(None, 80)
        close_button = Button("Close", (490, 925), font_button, FONT_COLOR)
        close_button.update(screen)

        #Handles the events for closing the page 
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if close_button.check_input(mouse_pos):
                        running = False

            pygame.display.flip()