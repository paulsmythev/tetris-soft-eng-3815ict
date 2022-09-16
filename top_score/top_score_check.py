#This class does to things. 
#One checks to see if the end of game score is high enough to be added to top scores list
#Two if the score is big enough to added, a screen will be displayed showing the score and asking for a name and once submitted the top-scores.json will be updated 
import pygame
from top_score.file_handler import readJson, writeJson
from start_menu.button import Button

#Checks to see if the score being checked is bigger or lower than the number 10 score 
class topScoreCheck():
    def __init__(selft, score, playerAI):

        try:
            topScoresImport = readJson()
        except:
            print("cant load JSON")

        arrayCount = 0

        if topScoresImport[len(topScoresImport)-1]["score"] <= score:
            for x in topScoresImport:
                arrayCount += 1
                if x["score"] == score or x["score"] < score:
                    promptName(score, playerAI, arrayCount)
                    break
        else:
            print("not high enough")

#If the score is high enough a screen is displayed congratulating them and asking for a name to save their score 
def promptName(score, playerAI, pos):
    font_color = (255, 255, 224)
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000

    #temp name get from textbox
    name = "git add ."

    #game played by AI will skip ask for name 
    if playerAI == True:
        updateJson(pos, "AI", score)
    
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
    text = font.render("Top Score Achieved!", 1, font_color)
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
    text = font.render(strScore, 1, font_color)
    screen.blit(text, (490, 430))

    #textbox and button to save
    font = pygame.font.Font(None, 50)
    text = font.render("Enter name to save score", 1, font_color)
    screen.blit(text, (330, 540))

    font_button = pygame.font.Font(None, 80)
    save_button = Button("Save", (530, 700), font_button, font_color)
    save_button.update(screen)

    #close button
    font_button = pygame.font.Font(None, 80)
    close_button = Button("Close", (SCREEN_WIDTH/2+30, SCREEN_HEIGHT*0.9), font_button, font_color)
    close_button.update(screen)

    #Handles the events for closing the page 
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.checkInput(mouse_pos):
                    running = False
                elif save_button.checkInput(mouse_pos):
                    if name != "":
                        updateJson(score, name, pos)
                        running = False
                    else:
                        print("Enter Name!")

        pygame.display.flip()

#Handles the updateJson procedure 
def updateJson(score, name, pos):

    try:
        topScoresImport = readJson()
    except:
        print("cant load JSON")

    #delete last value
    topScoresImport.pop(len(topScoresImport)-1)

    insertData = {'name': name, 'score': score}
    topScoresImport.insert(pos-1, insertData)

    writeJson(topScoresImport)