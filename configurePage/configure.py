# imports pygame module
# imports button class
# imports all functions from main
import pygame, sys
from start_menu.button import Button

# initialise module
pygame.init()

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

# loads an icon of a cog wheel
icon = pygame.image.load('cogwheel.png')

# # Give the window an icon
pygame.display.set_icon(icon)

# function
def my_font(font_size):
    return pygame.font.SysFont("Roboto", font_size)

# function
def config():

    # game window loops until we press 'exit'
    run = True
    while run:
        screen.fill(BLACK)
        mouse_pos = pygame.mouse.get_pos()

        # create headings
        settings_title = my_font(75).render("Settings", True, CREAM)
        field_heading = my_font(75).render("Field Size", True, CREAM)
        level_heading = my_font(75).render("Level", True, CREAM)
        mode_heading= my_font(75).render("Mode", True, CREAM)
        title_rect = settings_title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT*0.10))
        field_rect = field_heading.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT*0.25))
        level_rect = level_heading.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT*0.40))
        mode_rect = mode_heading.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT*0.55))

        # blits text to screen
        screen.blit(settings_title, title_rect)
        screen.blit(field_heading, field_rect)
        screen.blit(level_heading, level_rect)
        screen.blit(mode_heading, mode_rect)

                # create buttons
        fieldsize_button = Button("10x40", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.30), my_font(50), CREAM)
        level1_button = Button("Level 1", (SCREEN_WIDTH*0.30, SCREEN_HEIGHT*0.45), my_font(50), CREAM)
        level2_button = Button("Level 2", (SCREEN_WIDTH*0.45, SCREEN_HEIGHT*0.45), my_font(50), CREAM)
        level3_button = Button("Level 3", (SCREEN_WIDTH*0.60, SCREEN_HEIGHT*0.45), my_font(50), CREAM)
        level4_button = Button("Level 4", (SCREEN_WIDTH*0.75, SCREEN_HEIGHT*0.45), my_font(50), CREAM)
        easy_button = Button("Easy", (SCREEN_WIDTH*0.25, SCREEN_HEIGHT*0.60), my_font(50), CREAM)
        normal_button = Button("Normal", (SCREEN_WIDTH*0.40, SCREEN_HEIGHT*0.60), my_font(50), CREAM)
        hard_button = Button("Hard", (SCREEN_WIDTH*0.55, SCREEN_HEIGHT*0.60), my_font(50), CREAM)
        extended_button = Button("Extended", (SCREEN_WIDTH*0.71, SCREEN_HEIGHT*0.60), my_font(50), CREAM)
        ai_button = Button("AI", (SCREEN_WIDTH*0.25, SCREEN_HEIGHT*0.67), my_font(50), CREAM)
        close_button = Button("Close", (SCREEN_WIDTH*0.85, SCREEN_HEIGHT*0.90), my_font(50), CREAM)


        #blit to the screen
        buttons = [fieldsize_button, level1_button, level2_button, level3_button, 
                    level4_button, easy_button, normal_button, 
                    hard_button, extended_button, ai_button, close_button]
        for button in buttons:
            button.update(screen)

        
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
            clock.tick(60)

            # game will update
        pygame.display.update()

