from turtle import back, left, screensize
import pygame
import sys
from start_menu.button import Button
from GamePage.game import runGame

pygame.init()

# colours
CREAM = (255, 255, 224)
BLACK = (0, 0, 0)
TURQUOISE = (72, 209, 204)
ORANGE = (255, 165, 0)

# window setup
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)
pygame.display.set_caption("Start menu")

def my_font(font_size):
    return pygame.font.SysFont("Roboto", font_size)

def write_lines(surface, text, font, colour, x_coor, y_coor):
    height = font.get_height()
    lines = text.split("\n")
    for i, line in enumerate(lines):
        text_rect = font.render(line, True, colour)
        surface.blit(text_rect, (x_coor, y_coor+(i*height))) 

def play():
    runGame()
    print("@ play screen")

def options():
    print("@ options screen")

def high_scores():
    print("@ high score")

# menu loop
def main_menu():
    running = True
    while running:
        screen.fill(BLACK)
        mouse_pos = pygame.mouse.get_pos()

        # main title
        tetris_title = my_font(300).render("Tetris", True, CREAM)
        title_rect = tetris_title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT*0.15))
        screen.blit(tetris_title, title_rect)

        # year + course code
        course_info = "Made for:\n3815ICT\nSoftware Engineering\nYear: 2022"
        write_lines(screen, course_info, my_font(35), ORANGE, SCREEN_WIDTH*0.01, SCREEN_HEIGHT*0.5)
        # student names
        student_names = "Students:\nPaul Smyth\nKevin Pho\nRobert Newcombe\nEmanuel Worku"
        write_lines(screen, student_names, my_font(35), ORANGE, SCREEN_WIDTH*0.01, SCREEN_HEIGHT*0.65)

        # instantiating buttons
        play_button = Button("PLAY!", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.40), my_font(200), CREAM)
        options_button = Button("Settings", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.6), my_font(100), CREAM)
        # credits_button = Button("Credits", (SCREEN_HEIGHT/2, SCREEN_HEIGHT*0.6), my_font(70), CREAM)
        score_button = Button("High Scores", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.75), my_font(100), CREAM)
        exit_button = Button("Exit", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.9), my_font(80), CREAM)

        # for blitting buttons to screen
        buttons = [play_button, options_button, exit_button, score_button]
        for button in buttons:
            button.update(screen)

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkInput(mouse_pos):
                    play()
                elif options_button.checkInput(mouse_pos):
                    options()
                elif score_button.checkInput(mouse_pos):
                    high_scores()
                elif exit_button.checkInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()
        
main_menu()
# https://fonts.google.com/specimen/Silkscreen
