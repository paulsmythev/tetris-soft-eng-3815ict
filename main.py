import pygame
from assets.colours import Colours
from start_menu.button import Button
from game_page.controller import Controller
from configurePage.configure import Configure
from top_score.top_score_screen import TopScoreScreen

# Initialise pygame modules
pygame.init()

# This is a class for the settings of the game
class GameSettings:
    # Initialise settings with default values
    game_size = (10,20)
    start_level = 0
    game_type = 0
    game_mode = 0

# This class holds the variables and functions of the tetris main menu
class MainMenu:
    # Initialise settings class
    settings = GameSettings()

    # Initialise pygame display
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TETRIS - Main Menu")

    # This class function returns a font type based on the given size and the tetris font boolean
    def my_font(self, font_size, tetris = False):
        # Returns tetris font
        if tetris:
            return pygame.font.Font("assets/fonts/tetris_font.ttf", font_size)
        # Returns roboto font
        else:
            return pygame.font.SysFont("Roboto", font_size)

    # This class function creates and runs the game controller class
    def play(self):
        controller = Controller(self.settings)
        controller.run_game()

    # This class function creates and runs the configure class
    def options(self):
        configure = Configure()
        configure.run_configure(self.settings)

    # This class function creates and runs the top score class
    def high_scores(self):
        top_score = TopScoreScreen()
        top_score.run_high_scores()

    # This class function updates the display
    def main_menu_display(self):
        self.screen.fill(Colours.BLACK)

        # Display main menu background image
        background = pygame.image.load('assets/backgrounds/main_menu_background.jpg')
        background = pygame.transform.smoothscale(background, (1000,1000))
        self.screen.blit(background, (0, 0))

        # Display tetris title
        tetris_title = self.my_font(250, True).render("TETRIS", True, Colours.YELLOW)
        title_rect = tetris_title.get_rect(center=(self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.15))
        self.screen.blit(tetris_title, title_rect)

        # Initialise menu buttons
        self.play_button = Button("PLAY", (500, 400), self.my_font(180, True), Colours.GREEN)
        self.options_button = Button("Settings", (500, 550), self.my_font(80, True), Colours.WHITE)
        self.score_button = Button("High Scores", (500, 700), self.my_font(80, True), Colours.WHITE)
        self.exit_button = Button("Exit", (500, 850), self.my_font(80, True), Colours.WHITE)

        # Display menu buttons
        buttons = [self.play_button, self.options_button, self.exit_button, self.score_button]
        for button in buttons:
            button.update(self.screen)

        # Display project information
        course_info = self.my_font(35).render("3815ICT Software Engineering - Timester 2 2022", True, Colours.WHITE)
        self.screen.blit(course_info, (20, 940))
        student_info = self.my_font(35).render("By: Paul Smyth - Kevin Pho - Robert Newcombe - Emanuel Worku", True, Colours.WHITE)
        self.screen.blit(student_info, (20, 970))
        
        #Update the pygame display
        pygame.display.update()

    # This class function runs the control loop for the main menu
    def main_menu(self):
        # Update display
        self.main_menu_display()
        # Run control loop
        running = True
        while running:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Check all new events
            for event in pygame.event.get():
                # Close window event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Check buttons if mouse is clicked
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Play button
                    if self.play_button.check_input(mouse_pos):
                        self.play()
                        # Update display
                        self.main_menu_display()
                    # Settings button
                    elif self.options_button.check_input(mouse_pos):
                        self.options()
                        # Update display
                        self.main_menu_display()
                    # High-Scores button
                    elif self.score_button.check_input(mouse_pos):
                        self.high_scores()
                        # Update display
                        self.main_menu_display()
                    # Exit button
                    elif self.exit_button.check_input(mouse_pos):
                        # Quit pygame and exit program
                        pygame.quit()
                        exit()

# Create main menu class and call its control loop
main_menu = MainMenu()
main_menu.main_menu()