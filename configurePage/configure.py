# imports pygame module
# imports button class
# imports all functions from main
import pygame, sys
from start_menu.button import Button

# initialise module
pygame.init()

class Configure:
    
    DARK_GREY = (50, 50, 50)
    GREY = (100, 100, 100)
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

    def display_box(self, option, pos, value):
        pygame.draw.rect(self.screen, self.CREAM, pygame.Rect(pos[0]-72,pos[1]-22,144,44))
        if(option == value):
            pygame.draw.rect(self.screen, self.DARK_GREY, pygame.Rect(pos[0]-70,pos[1]-20,140,40))
        else:
            pygame.draw.rect(self.screen, self.GREY, pygame.Rect(pos[0]-70,pos[1]-20,140,40))

    def update_display(self, settings):
        self.screen.fill(self.BLACK)
        self.headings()

        # blits text to screen
        self.screen.blit(self.settings_title, self.title_rect)
        self.screen.blit(self.game_size_heading, self.game_size_rect)
        self.screen.blit(self.start_level_heading, self.start_level_rect)
        self.screen.blit(self.game_mode_heading, self.game_mode_rect)
        self.screen.blit(self.game_type_heading, self.game_type_rect)

        # size buttons
        self.display_box(settings.game_size, (200, 300), (10,20))
        self.fieldsize1_button = Button("10x20", (200, 300), self.my_font(40), self.CREAM)
        self.fieldsize1_button.rect = pygame.Rect(200-70, 300-20, 140, 40)

        self.display_box(settings.game_size, (350, 300), (15,30))
        self.fieldsize2_button = Button("15x30", (350, 300), self.my_font(40), self.CREAM)
        self.fieldsize2_button.rect = pygame.Rect(350-70, 300-20, 140, 40)

        self.display_box(settings.game_size, (500, 300), (20,40))
        self.fieldsize3_button = Button("20x40", (500, 300), self.my_font(40), self.CREAM)
        self.fieldsize3_button.rect = pygame.Rect(500-70, 300-20, 140, 40)

        # start level buttons
        self.display_box(settings.start_level, (200, 450), 0)
        self.level0_button = Button("lvl 0 ", (200, 450), self.my_font(40), self.CREAM)
        self.level0_button.rect = pygame.Rect(200-70, 450-20, 140, 40)

        self.display_box(settings.start_level, (350, 450), 10)
        self.level10_button = Button("lvl 10", (350, 450), self.my_font(40), self.CREAM)
        self.level10_button.rect = pygame.Rect(350-70, 450-20, 140, 40)

        self.display_box(settings.start_level, (500, 450), 20)
        self.level20_button = Button("lvl 20", (500, 450), self.my_font(40), self.CREAM)
        self.level20_button.rect = pygame.Rect(500-70, 450-20, 140, 40)

        self.display_box(settings.start_level, (650, 450), 30)
        self.level30_button = Button("lvl 30", (650, 450), self.my_font(40), self.CREAM)
        self.level30_button.rect = pygame.Rect(650-70, 450-20, 140, 40)

        # game mode buttons
        self.display_box(settings.game_mode, (200, 600), 0)
        self.normal_button = Button("Normal", (200, 600), self.my_font(40), self.CREAM)
        self.normal_button.rect = pygame.Rect(200-70, 600-20, 140, 40)

        self.display_box(settings.game_mode, (350, 600), 1)
        self.extended_button = Button("Extended", (350, 600), self.my_font(40), self.CREAM)
        self.extended_button.rect = pygame.Rect(350-70, 600-20, 140, 40)

        # game type buttons
        self.display_box(settings.game_type, (200, 750), 0)
        self.player_button = Button("Player", (200, 750), self.my_font(40), self.CREAM)
        self.player_button.rect = pygame.Rect(200-70, 750-20, 140, 40)

        self.display_box(settings.game_type, (350, 750), 1)
        self.ai_button = Button("AI", (350, 750), self.my_font(40), self.CREAM)
        self.ai_button.rect = pygame.Rect(350-70, 750-20, 140, 40)

        # close button
        self.close_button = Button("Close", (self.SCREEN_WIDTH*0.85, self.SCREEN_HEIGHT*0.90), self.my_font(50), self.CREAM)


        #blit to the screen
        buttons = [self.fieldsize1_button, self.fieldsize2_button, self.fieldsize3_button,
            self.level0_button, self.level10_button, self.level20_button, self.level30_button,
            self.normal_button, self.extended_button, self.ai_button, self.player_button, self.close_button]

        for button in buttons:
            button.update(self.screen)

    # Runs page
    def config(self, settings):
        self.update_display(settings)
        # game window loops until we press 'exit'
        run = True
        while run:
            
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()   # game quits
                    sys.exit()
                
                # condition
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.fieldsize1_button.check_input(mouse_pos):
                        settings.game_size = (10,20)
                        self.update_display(settings)
                    elif self.fieldsize2_button.check_input(mouse_pos):
                        settings.game_size = (15,30)
                        self.update_display(settings)
                    elif self.fieldsize3_button.check_input(mouse_pos):
                        settings.game_size = (20,40)
                        self.update_display(settings)
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
                    elif self.normal_button.check_input(mouse_pos):
                        settings.game_mode = 0
                        self.update_display(settings)
                    elif self.extended_button.check_input(mouse_pos):
                        settings.game_mode = 1
                        self.update_display(settings)
                    elif self.player_button.check_input(mouse_pos):
                        settings.game_type = 0
                        self.update_display(settings)
                    elif self.ai_button.check_input(mouse_pos):
                        settings.game_type = 1
                        self.update_display(settings)
                    elif self.close_button.check_input(mouse_pos):
                        run = False
                    # lets up update only a portion of whats on the screen
                    pygame.display.flip()
                    # loops 60fps
                self.clock.tick(60)

                # game will update
            pygame.display.update()