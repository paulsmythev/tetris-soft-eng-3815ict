
import pygame
import json
from start_menu.button import Button
from top_score.file_handler import FileHandler

NUMBER_IMAGE = (50, 50)
FONT_COLOR = (255, 255, 0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()

class TopScoreScreen:
    
    def __init__(self):
        self.concat_array = []
        self.top_scores_array = []
        self.concat_array.clear()

        self.file_issue = False

        #calls file_handler to loading json data ? happens when the start menu opens
        try:
            self.get_file = FileHandler()
            self.top_scores_import = []
            self.top_scores_import = self.get_file.read_json()
        except:
            print("cant load JSON")

        #writes each line to array
        for x in self.top_scores_import:
            self.top_scores_array.append(x)


        #Formats the names and scores to be displayed 
        for x in range(len(self.top_scores_array)):
            brk = json.dumps(self.top_scores_array[x])
            test = json.loads(brk)
            str_name = test["name"]
            str_score = "{:,}".format(test["score"])
            self.concat_array.append(str_name + " - " + str_score)

    
    def my_font(self, font_size):
        return pygame.font.SysFont("Roboto", font_size)


    #imports all the images
    def import_images(self):
        try:
            self.score1 = pygame.image.load('top_score/images/number-one-round-icon.png')
            self.score2 = pygame.image.load('top_score/images/number-two-round-icon.png')
            self.score3 = pygame.image.load('top_score/images/number-three-round-icon.png')
            self.score4 = pygame.image.load('top_score/images/number-four-round-icon.png')
            self.score5 = pygame.image.load('top_score/images/number-five-round-icon.png')
            self.score6 = pygame.image.load('top_score/images/number-six-round-icon.png')
            self.score7 = pygame.image.load('top_score/images/number-seven-round-icon.png')
            self.score8 = pygame.image.load('top_score/images/number-eight-round-icon.png')
            self.score9 = pygame.image.load('top_score/images/number-nine-round-icon.png')
            self.score10 = pygame.image.load('top_score/images/number-ten-round-icon.png')
            self.header_image = pygame.image.load('top_score/images/1305624857.png')
            self.wallpaper = pygame.image.load('GamePage/assets/Score_Wallpaper.jpg')
        except:
            self.file_issue = True

    #Responsible for displaying everything on the page
    def visual_elements(self):
        self.import_images()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris - Top Scores')
        self.screen.fill(BLACK)

        if self.file_issue == False:
            self.wallpaper = pygame.transform.scale(self.wallpaper, (1000,1000))
            self.screen.blit(self.wallpaper, (0, 0))

            self.header_image = pygame.transform.smoothscale(self.header_image, (225, 175))
            self.screen.blit(self.header_image, (35, 8))

            #Displays the images for 1 - 10
            self.score1 = pygame.transform.smoothscale(self.score1, NUMBER_IMAGE)
            self.screen.blit(self.score1, (150, 200))
            self.score2 = pygame.transform.smoothscale(self.score2, NUMBER_IMAGE)
            self.screen.blit(self.score2, (150, 270))
            self.score3 = pygame.transform.smoothscale(self.score3, NUMBER_IMAGE)
            self.screen.blit(self.score3, (150, 340))
            self.score4 = pygame.transform.smoothscale(self.score4, NUMBER_IMAGE)
            self.screen.blit(self.score4, (150, 410))
            self.score5 = pygame.transform.smoothscale(self.score5, NUMBER_IMAGE)
            self.screen.blit(self.score5, (150, 480))
            self.score6 = pygame.transform.smoothscale(self.score6, NUMBER_IMAGE)
            self.screen.blit(self.score6, (150, 550))
            self.score7 = pygame.transform.smoothscale(self.score7, NUMBER_IMAGE)
            self.screen.blit(self.score7, (150, 620))
            self.score8 = pygame.transform.smoothscale(self.score8, NUMBER_IMAGE)
            self.screen.blit(self.score8, (150, 690))
            self.score9 = pygame.transform.smoothscale(self.score9, NUMBER_IMAGE)
            self.screen.blit(self.score9, (150, 760))
            self.score10 = pygame.transform.smoothscale(self.score10, NUMBER_IMAGE)
            self.screen.blit(self.score10, (150, 830))

        self.font = pygame.font.Font(None, 100)
        self.text = self.font.render("Top 10 Scores", 1, FONT_COLOR)
        self.screen.blit(self.text, (290, 80))

        #Display names and scores on the page, 42 spacing
        font = pygame.font.Font(None, 50)
        spacing = 210
        for x in range(len(self.concat_array)):
            text = font.render(self.concat_array[x], 1, FONT_COLOR)
            self.screen.blit(text, (225, spacing))
            spacing += 70

    #Handles the events for running and closing the page 
    def screen(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()

            self.visual_elements()

            close_button = Button("Close", (490, 925), self.my_font(80), RED)
            close_button.update(self.screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if close_button.check_input(mouse_pos):
                        running = False
