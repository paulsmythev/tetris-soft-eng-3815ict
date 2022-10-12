import pygame, sys
from start_menu.button import Button
from assets.colours import Colours

# Initialise pygame modules
pygame.init()

# This class holds the variables and functions of the settings menu
class Configure:

    # Initialise pygame display
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TETRIS - Settings")

    # This class function returns a font type based on the given size and the tetris font boolean
    def my_font(self, font_size, tetris = False):
        # Returns tetris font
        if tetris:
            return pygame.font.Font("assets/fonts/tetris_font.ttf", font_size)
        # Returns roboto font
        else:
            return pygame.font.SysFont("Roboto", font_size)

    # This class function intialises the display headings
    def headings(self):
        # Initialise text
        self.settings_title = self.my_font(150, True).render("Settings", True, Colours.GREEN)
        self.game_size_heading = self.my_font(50, True).render("Game Size", True, Colours.YELLOW)
        self.start_level_heading = self.my_font(50, True).render("Start Level", True, Colours.YELLOW)
        self.game_mode_heading= self.my_font(50, True).render("Game Mode", True, Colours.YELLOW)
        self.game_type_heading= self.my_font(50, True).render("Game Type", True, Colours.YELLOW)
        # Initialise text rect
        self.title_rect = self.settings_title.get_rect(center=(self.SCREEN_WIDTH/2, 125))
        self.game_size_rect = self.game_size_heading.get_rect(midleft=(130, 250))
        self.start_level_rect = self.start_level_heading.get_rect(midleft=(130, 400))
        self.game_mode_rect = self.game_mode_heading.get_rect(midleft=(130, 550))
        self.game_type_rect = self.game_type_heading.get_rect(midleft=(130, 700))

    # This class function changes the colour of the buttons if the settings is active
    def display_box(self, option, pos, value):
        pygame.draw.rect(self.screen, Colours.WHITE, pygame.Rect(pos[0]-72,pos[1]-22,144,44))
        # If active setting make box dark grey
        if(option == value):
            pygame.draw.rect(self.screen, Colours.DARK_GREY, pygame.Rect(pos[0]-70,pos[1]-20,140,40))
        # If inactive setting make box grey
        else:
            pygame.draw.rect(self.screen, Colours.GREY, pygame.Rect(pos[0]-70,pos[1]-20,140,40))

    # This class function updates the display
    def update_display(self, settings):
        self.screen.fill(Colours.BLACK)
        
        # Display settings background image
        wallpaper = pygame.image.load('assets/backgrounds/settings_background.jpg')
        wallpaper = pygame.transform.scale(wallpaper, (1000,1000))
        self.screen.blit(wallpaper, (0, 0))

        # Initialsie headings
        self.headings()

        # Display headings
        self.screen.blit(self.settings_title, self.title_rect)
        self.screen.blit(self.game_size_heading, self.game_size_rect)
        self.screen.blit(self.start_level_heading, self.start_level_rect)
        self.screen.blit(self.game_mode_heading, self.game_mode_rect)
        self.screen.blit(self.game_type_heading, self.game_type_rect)

        # Initialise size buttons
        self.display_box(settings.game_size, (200, 300), (10,20))
        self.fieldsize1_button = Button("10x20", (200, 300), self.my_font(40), Colours.WHITE)
        self.fieldsize1_button.rect = pygame.Rect(200-70, 300-20, 140, 40)

        self.display_box(settings.game_size, (350, 300), (15,30))
        self.fieldsize2_button = Button("15x30", (350, 300), self.my_font(40), Colours.WHITE)
        self.fieldsize2_button.rect = pygame.Rect(350-70, 300-20, 140, 40)

        self.display_box(settings.game_size, (500, 300), (20,40))
        self.fieldsize3_button = Button("20x40", (500, 300), self.my_font(40), Colours.WHITE)
        self.fieldsize3_button.rect = pygame.Rect(500-70, 300-20, 140, 40)

        # Initialise level buttons
        self.display_box(settings.start_level, (200, 450), 0)
        self.level0_button = Button("lvl 0 ", (200, 450), self.my_font(40), Colours.WHITE)
        self.level0_button.rect = pygame.Rect(200-70, 450-20, 140, 40)

        self.display_box(settings.start_level, (350, 450), 10)
        self.level10_button = Button("lvl 10", (350, 450), self.my_font(40), Colours.WHITE)
        self.level10_button.rect = pygame.Rect(350-70, 450-20, 140, 40)

        self.display_box(settings.start_level, (500, 450), 20)
        self.level20_button = Button("lvl 20", (500, 450), self.my_font(40), Colours.WHITE)
        self.level20_button.rect = pygame.Rect(500-70, 450-20, 140, 40)

        self.display_box(settings.start_level, (650, 450), 30)
        self.level30_button = Button("lvl 30", (650, 450), self.my_font(40), Colours.WHITE)
        self.level30_button.rect = pygame.Rect(650-70, 450-20, 140, 40)

        # Initialise game mode buttons
        self.display_box(settings.game_mode, (200, 600), 0)
        self.normal_button = Button("Normal", (200, 600), self.my_font(40), Colours.WHITE)
        self.normal_button.rect = pygame.Rect(200-70, 600-20, 140, 40)

        self.display_box(settings.game_mode, (350, 600), 1)
        self.extended_button = Button("Extended", (350, 600), self.my_font(40), Colours.WHITE)
        self.extended_button.rect = pygame.Rect(350-70, 600-20, 140, 40)

        # Initialise game type buttons
        self.display_box(settings.game_type, (200, 750), 0)
        self.player_button = Button("Player", (200, 750), self.my_font(40), Colours.WHITE)
        self.player_button.rect = pygame.Rect(200-70, 750-20, 140, 40)

        self.display_box(settings.game_type, (350, 750), 1)
        self.ai_button = Button("AI", (350, 750), self.my_font(40), Colours.WHITE)
        self.ai_button.rect = pygame.Rect(350-70, 750-20, 140, 40)

        # Initialise close button
        self.close_button = Button("Close", (490, 900), self.my_font(70, True), Colours.WHITE)

        # Display all buttons
        buttons = [self.fieldsize1_button, self.fieldsize2_button, self.fieldsize3_button,
            self.level0_button, self.level10_button, self.level20_button, self.level30_button,
            self.normal_button, self.extended_button, self.ai_button, self.player_button, self.close_button]
        for button in buttons:
            button.update(self.screen)

        # Update pygame display
        pygame.display.update()

    # This class function runs the control loop for the settings menu
    def run_configure(self, settings):
        # Update display
        self.update_display(settings)
        # Run control loop
        run = True
        while run:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Check all new events
            for event in pygame.event.get():
                # Close window event
                if event.type == pygame.QUIT:
                    run = False
                # Check buttons if mouse is clicked
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Game size buttons
                    if self.fieldsize1_button.check_input(mouse_pos):
                        settings.game_size = (10,20)
                        self.update_display(settings)
                    elif self.fieldsize2_button.check_input(mouse_pos):
                        settings.game_size = (15,30)
                        self.update_display(settings)
                    elif self.fieldsize3_button.check_input(mouse_pos):
                        settings.game_size = (20,40)
                        self.update_display(settings)
                    # Game level buttons
                    elif self.level0_button.check_input(mouse_pos):
                        settings.start_level = 0
                        self.update_display(settings)
                    elif self.level10_button.check_input(mouse_pos):
                        settings.start_level = 10
                        self.update_display(settings)
                    elif self.level20_button.check_input(mouse_pos):
                        settings.start_level = 20
                        self.update_display(settings)
                    elif self.level30_button.check_input(mouse_pos):
                        settings.start_level = 30
                        self.update_display(settings)
                    # Game mode buttons
                    elif self.normal_button.check_input(mouse_pos):
                        settings.game_mode = 0
                        self.update_display(settings)
                    elif self.extended_button.check_input(mouse_pos):
                        settings.game_mode = 1
                        self.update_display(settings)
                    # Game type button
                    elif self.player_button.check_input(mouse_pos):
                        settings.game_type = 0
                        self.update_display(settings)
                    elif self.ai_button.check_input(mouse_pos):
                        settings.game_type = 1
                        self.update_display(settings)
                    # Close button
                    elif self.close_button.check_input(mouse_pos):
                        run = False