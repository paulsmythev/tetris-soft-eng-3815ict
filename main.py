from turtle import back, left, screensize


import pygame
import sys
from start_menu.button import Button

from GamePage.controller import Controller
from configurePage.configure import Configure

from top_score.top_score_screen import TopScoreScreen

pygame.init()
class MainMenu:
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

    def my_font(self, font_size):
        return pygame.font.SysFont("Roboto", font_size)

    def write_lines(self, surface, text, font, colour, x_coor, y_coor):
        height = font.get_height()
        lines = text.split("\n")
        for i, line in enumerate(lines):
            text_rect = font.render(line, True, colour)
            surface.blit(text_rect, (x_coor, y_coor+(i*height))) 

    def play(self):
        controller = Controller((10,20),0,0,0)
        controller.run_game()

    def options(self):
        configure = Configure()
        configure.config()

    def high_scores(self):
        top_score = TopScoreScreen()
        top_score.screen()

    def main_menu_view(self):
        self.screen.fill(self.BLACK)        
        # main title
        tetris_title = self.my_font(300).render("Tetris", True, self.CREAM)
        title_rect = tetris_title.get_rect(center=(self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.15))
        self.screen.blit(tetris_title, title_rect)

        # year + course code
        course_info = "Made for:\n3815ICT\nSoftware Engineering\nYear: 2022"
        self.write_lines(self.screen, course_info, self.my_font(35), self.ORANGE, self.SCREEN_WIDTH*0.01, self.SCREEN_HEIGHT*0.5)
        # student names
        student_names = "Students:\nPaul Smyth\nKevin Pho\nRobert Newcombe\nEmanuel Worku"
        self.write_lines(self.screen, student_names, self.my_font(35), self.ORANGE, self.SCREEN_WIDTH*0.01, self.SCREEN_HEIGHT*0.65)

    # menu loop
    def main_menu(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            # getting view
            self.main_menu_view()
            # instantiating buttons
            play_button = Button("PLAY!", (self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.40), self.my_font(200), self.CREAM)
            options_button = Button("Settings", (self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.6), self.my_font(100), self.CREAM)
            # credits_button = Button("Credits", (SCREEN_HEIGHT/2, SCREEN_HEIGHT*0.6), my_font(70), CREAM)
            score_button = Button("High Scores", (self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.75), self.my_font(100), self.CREAM)
            exit_button = Button("Exit", (self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT*0.9), self.my_font(80), self.CREAM)
            # for blitting buttons to screen
            buttons = [play_button, options_button, exit_button, score_button]
            for button in buttons:
                button.update(self.screen)

            # event check
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkInput(mouse_pos):
                        self.play()
                    elif options_button.checkInput(mouse_pos):
                        self.options()
                    elif score_button.checkInput(mouse_pos):
                        self.high_scores()
                    elif exit_button.checkInput(mouse_pos):
                        pygame.quit()
                        exit()

            pygame.display.update()
        
main_menu = MainMenu()
main_menu.main_menu()
# https://fonts.google.com/specimen/Silkscreen
