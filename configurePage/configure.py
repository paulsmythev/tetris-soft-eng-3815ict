# imports pygame module
# imports button class
# imports all functions from main
import pygame, sys
from start_menu.button import Button

# initialise module
pygame.init()

class Configure:
    
    CREAM = (255, 255, 224)
    BLACK = (0, 0, 0)
    TURQUOISE = (72, 209, 204)
    ORANGE = (255, 165, 0)

    # window setup
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000

    # initialise clock
    clock = pygame.time.Clock()

    # Creates the screen, includes dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")

    # Title
    pygame.display.set_caption("Configure Page")

    # loads and displays icon
    icon = pygame.image.load('configurePage\images\cogwheel.png')
    pygame.display.set_icon(icon)

        # Font function
    def my_font(self, font_size):
        return pygame.font.SysFont("Roboto", font_size)

        # create headings
    def headings(self):
        self.settings_title = self.my_font(100).render("Settings", True, self.CREAM)
        self.game_size_heading = self.my_font(60).render("Game Size", True, self.CREAM)
        self.start_level_heading = self.my_font(60).render("Start Level", True, self.CREAM)
        self.game_mode_heading= self.my_font(60).render("Game Mode", True, self.CREAM)
        self.game_type_heading= self.my_font(60).render("Game Type", True, self.CREAM)

        self.title_rect = self.settings_title.get_rect(center=(self.SCREEN_WIDTH/2, 100))
        self.game_size_rect = self.game_size_heading.get_rect(midleft=(100, 250))
        self.start_level_rect = self.start_level_heading.get_rect(midleft=(100, 400))
        self.game_mode_rect = self.game_mode_heading.get_rect(midleft=(100, 550))
        self.game_type_rect = self.game_type_heading.get_rect(midleft=(100, 700))

    # Runs page
    def config(self, settings):

        # game window loops until we press 'exit'
        run = True
        while run:
            self.screen.fill(self.BLACK)
            mouse_pos = pygame.mouse.get_pos()
            
            self.headings()

            # blits text to screen
            self.screen.blit(self.settings_title, self.title_rect)
            self.screen.blit(self.game_size_heading, self.game_size_rect)
            self.screen.blit(self.start_level_heading, self.start_level_rect)
            self.screen.blit(self.game_mode_heading, self.game_mode_rect)
            self.screen.blit(self.game_type_heading, self.game_type_rect)

            # create buttons
            fieldsize_button = Button("10x20", (200, 300), self.my_font(40), self.CREAM)

            # start level buttons
            level0_button = Button("lvl 0 ", (200, 450), self.my_font(40), self.CREAM)
            level10_button = Button("lvl 10", (350, 450), self.my_font(40), self.CREAM)
            level20_button = Button("lvl 20", (500, 450), self.my_font(40), self.CREAM)
            level30_button = Button("lvl 30", (650, 450), self.my_font(40), self.CREAM)

            # game mode buttons
            normal_button = Button("Normal", (200, 600), self.my_font(40), self.CREAM)
            extended_button = Button("Extended", (350, 600), self.my_font(40), self.CREAM)

            # game type buttons
            player_button = Button("Player", (200, 750), self.my_font(40), self.CREAM)
            ai_button = Button("AI", (350, 750), self.my_font(40), self.CREAM)
            close_button = Button("Close", (self.SCREEN_WIDTH*0.85, self.SCREEN_HEIGHT*0.90), self.my_font(50), self.CREAM)


            #blit to the screen
            buttons = [fieldsize_button, level0_button, level10_button, level20_button, 
                        level30_button, normal_button, extended_button, ai_button, player_button, close_button]
            for button in buttons:
                button.update(self.screen)

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()   # game quits
                    sys.exit()
                
                # condition
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if fieldsize_button.check_input(mouse_pos):
                        settings.game_size = (10,20)
                    elif level0_button.check_input(mouse_pos):
                        settings.start_level = 0
                    elif level10_button.check_input(mouse_pos):
                        settings.start_level = 10
                    elif level20_button.check_input(mouse_pos):
                        settings.start_level = 20
                    elif level30_button.check_input(mouse_pos):
                        settings.start_level = 30
                    elif normal_button.check_input(mouse_pos):
                        settings.game_mode = 0
                    elif extended_button.check_input(mouse_pos):
                        settings.game_mode = 1
                    elif player_button.check_input(mouse_pos):
                        settings.game_type = 0
                    elif ai_button.check_input(mouse_pos):
                        settings.game_type = 1
                    elif close_button.check_input(mouse_pos):
                        run = False

                    # lets up update only a portion of whats on the screen
                    pygame.display.flip()
                    # loops 60fps
                self.clock.tick(60)

                # game will update
            pygame.display.update()