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
        self.settings_title = self.my_font(75).render("Settings", True, self.CREAM)
        self.field_heading = self.my_font(75).render("Field Size", True, self.CREAM)
        self.level_heading = self.my_font(75).render("Level", True, self.CREAM)
        self.mode_heading= self.my_font(75).render("Mode", True, self.CREAM)
        self.title_rect = self.settings_title.get_rect(center=(self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.10))
        self.field_rect = self.field_heading.get_rect(center=(self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.25))
        self.level_rect = self.level_heading.get_rect(center=(self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.40))
        self.mode_rect = self.mode_heading.get_rect(center=(self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.55))

    # Runs page
    def config(self):

        # game window loops until we press 'exit'
        run = True
        while run:
            self.screen.fill(self.BLACK)
            mouse_pos = pygame.mouse.get_pos()
            
            self.headings()

            # blits text to screen
            self.screen.blit(self.settings_title, self.title_rect)
            self.screen.blit(self.field_heading, self.field_rect)
            self.screen.blit(self.level_heading, self.level_rect)
            self.screen.blit(self.mode_heading, self.mode_rect)

            # create buttons
            fieldsize_button = Button("10x40", (self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.30), self.my_font(50), self.CREAM)
            level1_button = Button("Level 1", (self.SCREEN_WIDTH*0.30, self.SCREEN_HEIGHT*0.45), self.my_font(50), self.CREAM)
            level2_button = Button("Level 2", (self.SCREEN_WIDTH*0.45, self.SCREEN_HEIGHT*0.45), self.my_font(50), self.CREAM)
            level3_button = Button("Level 3", (self.SCREEN_WIDTH*0.60, self.SCREEN_HEIGHT*0.45), self.my_font(50), self.CREAM)
            level4_button = Button("Level 4", (self.SCREEN_WIDTH*0.75, self.SCREEN_HEIGHT*0.45), self.my_font(50), self.CREAM)
            easy_button = Button("Easy", (self.SCREEN_WIDTH*0.25, self.SCREEN_HEIGHT*0.60), self.my_font(50), self.CREAM)
            normal_button = Button("Normal", (self.SCREEN_WIDTH*0.40, self.SCREEN_HEIGHT*0.60), self.my_font(50), self.CREAM)
            hard_button = Button("Hard", (self.SCREEN_WIDTH*0.55, self.SCREEN_HEIGHT*0.60), self.my_font(50), self.CREAM)
            extended_button = Button("Extended", (self.SCREEN_WIDTH*0.71, self.SCREEN_HEIGHT*0.60), self.my_font(50), self.CREAM)
            ai_button = Button("AI", (self.SCREEN_WIDTH*0.25, self.SCREEN_HEIGHT*0.67), self.my_font(50), self.CREAM)
            close_button = Button("Close", (self.SCREEN_WIDTH*0.85, self.SCREEN_HEIGHT*0.90), self.my_font(50), self.CREAM)


            #blit to the screen
            buttons = [fieldsize_button, level1_button, level2_button, level3_button, 
                        level4_button, easy_button, normal_button, 
                        hard_button, extended_button, ai_button, close_button]
            for button in buttons:
                button.update(self.screen)

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()   # game quits
                    sys.exit()
                
                # condition
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if fieldsize_button.checkInput(mouse_pos):
                        pass
                    if level1_button.checkInput(mouse_pos):
                        pass
                    elif level2_button.checkInput(mouse_pos):
                        pass
                    elif level3_button.checkInput(mouse_pos):
                        pass
                    elif level4_button.checkInput(mouse_pos):
                        pass
                    elif easy_button.checkInput(mouse_pos):
                        pass
                    elif normal_button.checkInput(mouse_pos):
                        pass
                    elif hard_button.checkInput(mouse_pos):
                        pass
                    elif extended_button.checkInput(mouse_pos):
                        pass
                    elif close_button.checkInput(mouse_pos):
                        run = False

                    # lets up update only a portion of whats on the screen
                    pygame.display.flip()
                    # loops 60fps
                self.clock.tick(60)

                # game will update
            pygame.display.update()