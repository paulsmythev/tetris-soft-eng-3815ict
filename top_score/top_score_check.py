import pygame
from top_score.file_handler import FileHandler
from start_menu.button import Button

NUMBER_IMAGE = (50, 50)
FONT_COLOR = (255, 255, 224)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
BLACK = (0, 0, 0)

pygame.init()

class TopScoreCheck:

    g_score = 0
    g_pos_ach = 0
    g_player_ai = False
    g_input_name = ""

    #checks if the submitted score is in the top 10
    def check(self, score):
        try:
            self.get_file = FileHandler()
            self.top_scores_import = self.get_file.read_json()
        except:
            print("cant load JSON")

        self.array_count = 0

        if self.top_scores_import[len(self.top_scores_import)-1]["score"] <= score:
            for x in self.top_scores_import:
                self.array_count += 1
                if x["score"] == score or x["score"] < score:
                    self.pos_ach = self.array_count
                    self.g_pos_ach = self.array_count
                    return True
        else:
            return False


    def my_font(self, font_size):
        return pygame.font.SysFont("Roboto", font_size)


    def import_images(self):
        self.score1 = pygame.image.load('top_score/images/number-one-round-icon.png')
        self.score2 = pygame.image.load('top_score/images/number-two-round-icon.png')
        self.score3 = pygame.image.load('top_score/images/number-three-round-icon.png')
        self.score4 = pygame.image.load('top_score/images/number-four-round-icon.png')
        self.score5 = pygame.image.load('top_score/images/number-five-round-icon.png')
        self.score6 = pygame.image.load('top_score/images/number-six-round-icon.png')
        self.score7 = pygame.image.load('top_score/images/number-seven-round-icon.png')
        self.score8 = pygame.image.load('top_score/images/number-eight-round-icon.png')
        self.score9 = pygame.image.load('top_score/images/number-nine-round-icon.png')
        self.score10 = pygame.image.load('top_score/images/number-ten-round-icon.png')
        self.header_image = pygame.image.load('top_score/images/1305624857.png')


    #Responsible for displaying everything on the page
    def visual_elements(self):
        self.import_images()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Top Score Achieved")
        self.screen.fill(BLACK)
        pygame.display.update()

        self.header_image = pygame.transform.smoothscale(self.header_image, (225, 175))
        self.screen.blit(self.header_image, (40, 200))

        self.font = pygame.font.Font(None, 100)
        self.text = self.font.render("Top Score Achieved!", 1, FONT_COLOR)
        self.screen.blit(self.text, (270, 275))

        #display number and score
        if self.pos_ach == 1:
            self.position_image = pygame.transform.smoothscale(self.score1, (120, 120))
        elif self.pos_ach == 2:
            self.position_image = pygame.transform.smoothscale(self.score2, (120, 120))
        elif self.pos_ach == 3:
            self.position_image = pygame.transform.smoothscale(self.score3, (120, 120))
        elif self.pos_ach == 4:
            self.position_image = pygame.transform.smoothscale(self.score4, (120, 120))
        elif self.pos_ach == 5:
            self.position_image = pygame.transform.smoothscale(self.score5, (120, 120))
        elif self.pos_ach == 6:
            self.position_image = pygame.transform.smoothscale(self.score6 (120, 120))
        elif self.pos_ach == 7:
            self.position_image = pygame.transform.smoothscale(self.score7, (120, 120))
        elif self.pos_ach == 8:
            self.position_image = pygame.transform.smoothscale(self.score8, (120, 120))
        elif self.pos_ach == 9:
            self.position_image = pygame.transform.smoothscale(self.score9, (120, 120))
        elif self.pos_ach == 10:
            self.position_image = pygame.transform.smoothscale(self.score10, (120, 120))
    
        self.screen.blit(self.position_image, (350, 400))
        font = pygame.font.Font(None, 100)

        strScore = "{:,}".format(self.g_score)
        text = self.font.render(strScore, 1, FONT_COLOR)
        self.screen.blit(text, (490, 430))

        if self.g_player_ai == False:
            #asking user for name
            self.font = pygame.font.Font(None, 50)
            self.text = self.font.render("Enter name to save score", 1, FONT_COLOR)
            self.screen.blit(self.text, (330, 540))

            #textbox
            self.base_font = pygame.font.Font(None, 55)
            self.input_rect = pygame.Rect(340, 600, 400, 50)
            self.text_surface = self.base_font.render(self.g_input_name, True, (0, 0, 0))
            pygame.draw.rect(self.screen, FONT_COLOR, self.input_rect)
            self.screen.blit(self.text_surface, (self.input_rect.x+5, self.input_rect.y+5))


        elif self.g_player_ai == True:
            #changes to AI details

            self.g_input_name = "AI"
            self.font = pygame.font.Font(None, 100)
            self.text = self.font.render("Artificial Intelligence", 1, FONT_COLOR)
            self.screen.blit(self.text, (150, 550))

    #called only from a button to stop continuous loop
    def update_json(self):
        try:
            get_file = FileHandler()
            self.top_scores_import = get_file.read_json()
        except:
            print("cant load JSON")

        #delete last value
        self.top_scores_import.pop(len(self.top_scores_import)-1)

        #inserts name and score
        insert_data = {'name': self.g_input_name, 'score': self.g_score}
        self.top_scores_import.insert(self.g_pos_ach-1, insert_data)

        #passes array back to filehandler
        pass_file = FileHandler()
        pass_file.write_json(self.top_scores_import)


    #Handles the events for running and closing the page 
    def screen(self, score, player_ai):
        sufficient = self.check(score)
        if sufficient == True:
            self.g_score = score
            self.g_player_ai = player_ai

            self.input_rect_act = False

            running = True
            while running:
                mouse_pos = pygame.mouse.get_pos()

                self.visual_elements()

                close_button = Button("Close", (SCREEN_WIDTH/2+30, SCREEN_HEIGHT*0.9), self.my_font(80), FONT_COLOR)
                close_button.update(self.screen)

                if self.g_player_ai == False:
                    save_button = Button("Save", (530, 700), self.my_font(80), FONT_COLOR)
                    save_button.update(self.screen)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        if self.g_player_ai == True:
                            self.update_json()
                            running = False
                        else:
                            running = False

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if close_button.checkInput(mouse_pos):
                            if self.g_player_ai == True:
                                self.update_json()
                                running = False
                            else:
                                running = False

                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if save_button.checkInput(mouse_pos):
                                self.update_json()
                                running = False

                    #sets textbox as active
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.g_player_ai == False:
                            if self.input_rect.collidepoint(event.pos):
                                self.input_rect_act = True
                            else:
                                self.input_rect_act = False

                    #handles text entry
                    elif event.type == pygame.KEYDOWN:
                        if self.input_rect_act == True:
                            if event.key == pygame.K_BACKSPACE:
                                self.g_input_name = self.g_input_name[0:-1]
                            else:
                                self.g_input_name += event.unicode

        else:
            return False 