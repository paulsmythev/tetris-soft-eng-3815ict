import pygame
import json
from assets.colours import Colours
from start_menu.button import Button
from top_score.file_handler import FileHandler

# Initialise pygame modules
pygame.init()

# This class holds the variables and functions of the tetris topscores page
class TopScoreScreen:
    # Initialise pygame display
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TETRIS - High Scores")
    
    # This is the class contructor
    def __init__(self):
        # Initialise empty lists for holding and formatting top scores
        self.concat_array = []
        self.top_scores_array = []

        # Initialise file handler class and call its read json function
        try:
            self.get_file = FileHandler()
            self.top_scores_array = self.get_file.read_json()
        except:
            print("cant load JSON")

        # Formats the names and scores to be displayed 
        for x in range(len(self.top_scores_array)):
            brk = json.dumps(self.top_scores_array[x])
            test = json.loads(brk)
            str_name = test["name"]
            str_score = "{:,}".format(test["score"])
            self.concat_array.append(str_score + " - " + str_name)

    #This class function updates the display
    def update_display(self):
        self.screen.fill(Colours.BLACK)
        
        # Display high score background image
        background = pygame.image.load('assets/backgrounds/high_score_background.jpg')
        background = pygame.transform.smoothscale(background, (1000,1000))
        self.screen.blit(background, (0, 0))

        # Display high scores title
        font = pygame.font.Font("Assets/Fonts/Tetris_Font.ttf", 120)
        text = font.render("HIGH SCORES", 1, Colours.GREEN)
        self.screen.blit(text, (120, 60))

        # Initialise number images
        score1 = pygame.image.load('assets/images/high_score_1.png')
        score2 = pygame.image.load('assets/images/high_score_2.png')
        score3 = pygame.image.load('assets/images/high_score_3.png')
        score4 = pygame.image.load('assets/images/high_score_4.png')
        score5 = pygame.image.load('assets/images/high_score_5.png')
        score6 = pygame.image.load('assets/images/high_score_6.png')
        score7 = pygame.image.load('assets/images/high_score_7.png')
        score8 = pygame.image.load('assets/images/high_score_8.png')
        score9 = pygame.image.load('assets/images/high_score_9.png')
        score10 = pygame.image.load('assets/images/high_score_10.png')

        #Displays number images
        score1 = pygame.transform.smoothscale(score1, (50, 50))
        self.screen.blit(score1, (150, 200))
        score2 = pygame.transform.smoothscale(score2, (50, 50))
        self.screen.blit(score2, (150, 270))
        score3 = pygame.transform.smoothscale(score3, (50, 50))
        self.screen.blit(score3, (150, 340))
        score4 = pygame.transform.smoothscale(score4, (50, 50))
        self.screen.blit(score4, (150, 410))
        score5 = pygame.transform.smoothscale(score5, (50, 50))
        self.screen.blit(score5, (150, 480))
        score6 = pygame.transform.smoothscale(score6, (50, 50))
        self.screen.blit(score6, (150, 550))
        score7 = pygame.transform.smoothscale(score7, (50, 50))
        self.screen.blit(score7, (150, 620))
        score8 = pygame.transform.smoothscale(score8, (50, 50))
        self.screen.blit(score8, (150, 690))
        score9 = pygame.transform.smoothscale(score9, (50, 50))
        self.screen.blit(score9, (150, 760))
        score10 = pygame.transform.smoothscale(score10, (50, 50))
        self.screen.blit(score10, (150, 830))

        # Display names and scores
        font = pygame.font.SysFont("Roboto", 50)
        spacing = 205
        for x in range(len(self.concat_array)):
            # Print black outline text
            text = font.render(self.concat_array[x], 1, Colours.BLACK)
            self.screen.blit(text, (223, spacing))
            text = font.render(self.concat_array[x], 1, Colours.BLACK)
            self.screen.blit(text, (227, spacing))
            text = font.render(self.concat_array[x], 1, Colours.BLACK)
            self.screen.blit(text, (225, spacing+2))
            text = font.render(self.concat_array[x], 1, Colours.BLACK)
            self.screen.blit(text, (225, spacing-2))
            # Print inner yellow text
            text = font.render(self.concat_array[x], 1, Colours.YELLOW)
            self.screen.blit(text, (225, spacing))
            # Increase spacing between lines
            spacing += 70

        # Display close button
        self.close_button = Button("Close", (490, 935), pygame.font.Font("Assets/Fonts/Tetris_Font.ttf", 70), Colours.WHITE)
        self.close_button.update(self.screen)

        # Update the pygame display
        pygame.display.update()

    #This class function runs the control loop for the high score page
    def run_high_scores(self):
        # Update display
        self.update_display()
        # Run control loop
        running = True
        while running:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Check all new events
            for event in pygame.event.get():
                # Close window event
                if event.type == pygame.QUIT:
                    running = False
                # Check close button if mouse is clicked
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.close_button.check_input(mouse_pos):
                        running = False