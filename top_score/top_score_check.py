#This class does to things. 
#One checks to see if the end of game score is high enough to be added to top scores list
#Two if the score is big enough to added, a screen will be displayed showing the score and asking for a name and once submitted the top-scores.json will be updated 

#from top_score.top_score_check import TopScoreCheck
#TopScoreCheck(1000, True)

import pygame
from top_score.file_handler import FileHandler
from start_menu.button import Button

FONT_COLOUR = (255, 255, 224)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

#Checks to see if the score being checked is bigger or lower than the number 10 score 
class TopScoreCheck:
    def check(self, score, player_ai):

        try:
            get_file = FileHandler()
            top_scores_import = get_file.read_json()
        except:
            print("cant load JSON")

        array_count = 0

        if top_scores_import[len(top_scores_import)-1]["score"] <= score:
            for x in top_scores_import:
                array_count += 1
                if x["score"] == score or x["score"] < score:
                    prompt_name(score, player_ai, array_count)
                    break
        else:
            print("not high enough")

#If the score is high enough a screen is displayed congratulating them and asking for a name to save their score 
def prompt_name(score, player_ai, pos):

    #temp name get from textbox
    input_name = "Fred Smith"

    #game played by AI will skip ask for name 
    if player_ai == True:
        update_json(score, "AI", pos)
        input_name = "Artificial Intelligence"
    
    # Initialise the screen
    pygame.init()
    size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.update()
    pygame.display.set_caption("Top Score Achieved")

    #Fill the background
    background = pygame.Surface(size)
    background = background.convert()
    background.fill((250,250,250))

    #import images
    try:
        score1 = pygame.image.load('top_score/images/number-one-round-icon.png')
        score2 = pygame.image.load('top_score/images/number-two-round-icon.png')
        score3 = pygame.image.load('top_score/images/number-three-round-icon.png')
        score4 = pygame.image.load('top_score/images/number-four-round-icon.png')
        score5 = pygame.image.load('top_score/images/number-five-round-icon.png')
        score6 = pygame.image.load('top_score/images/number-six-round-icon.png')
        score7 = pygame.image.load('top_score/images/number-seven-round-icon.png')
        score8 = pygame.image.load('top_score/images/number-eight-round-icon.png')
        score9 = pygame.image.load('top_score/images/number-nine-round-icon.png')
        score10 = pygame.image.load('top_score/images/number-ten-round-icon.png')

        header_image = pygame.image.load('top_score/images/1305624857.png')
    except:
        print("Error loading image files")

    #Header text and image
    try: 
        header_image = pygame.transform.smoothscale(header_image, (225, 175))
        screen.blit(header_image, (40, 200))
    except:
        print("Error loading image file")

    font = pygame.font.Font(None, 100)
    text = font.render("Top Score Achieved!", 1, FONT_COLOUR)
    screen.blit(text, (270, 275))

    #display number and score
    if pos == 1:
        position_image = pygame.transform.smoothscale(score1, (120, 120))
    elif pos == 2:
        position_image = pygame.transform.smoothscale(score2, (120, 120))
    elif pos == 3:
        position_image = pygame.transform.smoothscale(score3, (120, 120))
    elif pos == 4:
        position_image = pygame.transform.smoothscale(score4, (120, 120))
    elif pos == 5:
        position_image = pygame.transform.smoothscale(score5, (120, 120))
    elif pos == 6:
        position_image = pygame.transform.smoothscale(score6 (120, 120))
    elif pos == 7:
        position_image = pygame.transform.smoothscale(score7, (120, 120))
    elif pos == 8:
        position_image = pygame.transform.smoothscale(score8, (120, 120))
    elif pos == 9:
        position_image = pygame.transform.smoothscale(score9, (120, 120))
    elif pos == 10:
        position_image = pygame.transform.smoothscale(score10, (120, 120))
    
    screen.blit(position_image, (350, 400))
    font = pygame.font.Font(None, 100)

    strScore = "{:,}".format(score)
    text = font.render(strScore, 1, FONT_COLOUR)
    screen.blit(text, (490, 430))

    if player_ai == False:
        #asking user for name
        font = pygame.font.Font(None, 50)
        text = font.render("Enter name to save score", 1, FONT_COLOUR)
        screen.blit(text, (330, 540))

        #textbox
        base_font = pygame.font.Font(None, 55)
        input_rect = pygame.Rect(340, 600, 400, 50)
        text_surface = base_font.render(input_name, True, (0, 0, 0))
        pygame.draw.rect(screen, FONT_COLOUR, input_rect)
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        font_button = pygame.font.Font(None, 80)
        save_button = Button("Save", (530, 700), font_button, FONT_COLOUR)
        save_button.update(screen)

    elif player_ai == True:
        font = pygame.font.Font(None, 100)
        text = font.render(input_name, 1, FONT_COLOUR)
        screen.blit(text, (150, 550))

    #close button
    font_button = pygame.font.Font(None, 80)
    close_button = Button("Close", (SCREEN_WIDTH/2+30, SCREEN_HEIGHT*0.9), font_button, FONT_COLOUR)
    close_button.update(screen)

    #Handles the events for closing the page 
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.check_input(mouse_pos):
                    running = False
                elif save_button.check_input(mouse_pos):
                    if input_name != "":
                        update_json(score, input_name, pos)
                        running = False
                    else:
                        print("Enter Name!")
                elif input_rect.collidepoint(event.pos):
                    print("Hit")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                        input_name = input_name[:-1]

                elif len(input_name) >= 20:
                    print(len(input_name))
                
                else:
                    input_name += event.unicode

        pygame.display.flip()

#Handles the updateJson procedure by deleting las entry then inserting into the array at desired position 
def update_json(score, name, pos):

    try:
        get_file = FileHandler()
        top_scores_import = get_file.read_json()
    except:
        print("cant load JSON")

    #delete last value
    top_scores_import.pop(len(top_scores_import)-1)

    insert_data = {'name': name, 'score': score}
    top_scores_import.insert(pos-1, insert_data)

    pass_file = FileHandler()
    pass_file.write_json(top_scores_import)