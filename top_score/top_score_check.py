import pygame
from assets.colours import Colours
from top_score.file_handler import FileHandler
from start_menu.button import Button

# Initialise pygame modules
pygame.init()

# This class hold the variables and functions of the new high score page
class TopScoreCheck:
    # Initialise the display
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Top Score Achieved")

    # Initialise new high score variables
    g_score = 0
    g_pos_ach = 0
    g_player_ai = False
    g_input_name = ""

    # This class function checks if the submitted score is in the top 10
    def check(self, score):
        # Read JSON file using file handler class and error handling
        try:
            self.get_file = FileHandler()
            self.top_scores_import = self.get_file.read_json()
        except:
            print("cant load JSON")
        # Check if new score is in the top 10
        self.array_count = 0
        try:
            if self.top_scores_import[len(self.top_scores_import)-1]["score"] <= score:
                for x in self.top_scores_import:
                    self.array_count += 1
                    if x["score"] == score or x["score"] < score:
                        self.pos_ach = self.array_count
                        self.g_pos_ach = self.array_count
                        # Return true if in the top 10
                        return True
            else:
                # If not in the top 10 return false
                return False
        except:
            return False

    # This class function returns a font type based on the given size and the tetris font boolean
    def my_font(self, font_size, tetris = False):
        # Returns tetris font
        if tetris:
            return pygame.font.Font("assets/fonts/tetris_font.ttf", font_size)
        # Returns roboto font
        else:
            return pygame.font.SysFont("Roboto", font_size)

    # This class function updates the display
    def update_display(self):
        self.screen.fill(Colours.BLACK)
        
        # Display new high score background image
        background = pygame.image.load('assets/backgrounds/new_high_score_background.jpg')
        background = pygame.transform.smoothscale(background, (1000,1000))
        self.screen.blit(background, (0, 0))
        # Display title
        self.font = pygame.font.Font("assets/fonts/tetris_font.ttf", 70)
        self.text = self.font.render("Top Score Achieved", 1, Colours.YELLOW)
        self.screen.blit(self.text, (160, 300))

        # Load and display new position image
        path = "assets/images/high_score_{0}.png".format(self.pos_ach)
        score_image = pygame.image.load(path)
        score_image = pygame.transform.smoothscale(score_image, (80, 80))
        self.screen.blit(score_image, (370, 420))

        # Display new score
        self.font = pygame.font.SysFont("Roboto", 100)
        strScore = "{:,}".format(self.g_score)
        text = self.font.render(strScore, 1, Colours.YELLOW)
        self.screen.blit(text, (490, 430))

        # Human type display
        if self.g_player_ai == False:
            # Asking user for name
            self.font = pygame.font.Font(None, 50)
            self.text = self.font.render("Enter name to save score", 1, Colours.WHITE)
            self.screen.blit(self.text, (300, 540))

            # Display textbox
            self.base_font = pygame.font.SysFont("Roboto", 55)
            self.input_rect = pygame.Rect(310, 600, 400, 50)
            self.text_surface = self.base_font.render(self.g_input_name, True, (0, 0, 0))
            pygame.draw.rect(self.screen, Colours.WHITE, self.input_rect)
            self.screen.blit(self.text_surface, (self.input_rect.x+5, self.input_rect.y+5))

        # Ai type display
        elif self.g_player_ai == True:
            # Display AI name
            self.g_input_name = "AI"
            self.font = pygame.font.SysFont("Roboto", 100)
            self.text = self.font.render("Artificial Intelligence", 1, Colours.WHITE)
            self.screen.blit(self.text, (150, 550))

        # Display close button
        self.close_button = Button("Close", (500, 820), self.my_font(60, True), Colours.RED)
        self.close_button.update(self.screen)

        # Display save button
        self.save_button = Button("Save", (500, 720), self.my_font(60, True), Colours.GREEN)
        self.save_button.update(self.screen)
        
        # Update pygame display
        pygame.display.update()

    #This class funtion updates the json file
    def update_json(self):
        # Update the json file using file handler class and error handling
        try:
            get_file = FileHandler()
            self.top_scores_import = get_file.read_json()
        except:
            print("cant load JSON")

        # If name empty set to Undisclosed
        if self.g_input_name == "":
            self.g_input_name = "Undisclosed"

        # Delete last value
        self.top_scores_import.pop(len(self.top_scores_import)-1)

        # Inserts name and score
        insert_data = {'name': self.g_input_name, 'score': self.g_score}
        self.top_scores_import.insert(self.g_pos_ach-1, insert_data)

        # Pass array back to filehandler
        pass_file = FileHandler()
        pass_file.write_json(self.top_scores_import)

    # This class function handles the events for running and closing the page 
    def run_new_score(self, score, player_ai):
        # Only ask for name and update the json if the new score is in the top 10
        if self.check(score):
            # Initialise new score variables
            self.g_score = score
            self.g_player_ai = player_ai
            self.input_rect_act = False
            # Update display
            self.update_display()
            # Run control loop
            running = True
            while running:
                # Get mouse position
                mouse_pos = pygame.mouse.get_pos()
                # Check all new evenets
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        if self.g_player_ai == True:
                            self.update_json()
                            running = False
                        else:
                            running = False
                    # Check buttons if mouse is clicked
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        # Close button
                        if self.close_button.check_input(mouse_pos):
                            running = False
                        # Save button
                        if self.save_button.check_input(mouse_pos):
                            self.update_json()
                            running = False
                    # Sets textbox as active
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.g_player_ai == False:
                            if self.input_rect.collidepoint(event.pos):
                                self.input_rect_act = True
                            else:
                                self.input_rect_act = False
                    # Handles text entry
                    elif event.type == pygame.KEYDOWN:
                        if self.input_rect_act == True:
                            if event.key == pygame.K_BACKSPACE:
                                self.g_input_name = self.g_input_name[0:-1]
                            else:
                                self.g_input_name += event.unicode
                            self.update_display()

        else:
            return False 