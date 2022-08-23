# last adjustment
# rescaled the ui to match larger window
# added a "settings" heading
# gave the window an icon
# font can be changed to match main.py in main branch 
# top score page can be closed in the configure.py


# imports pygame module
# imports start menu function
import pygame, sys
# from main import start_menu

# initialise module
pygame.init()
# initialise clock
clock = pygame.time.Clock()

# Creates the screen, includes dimensions
screen = pygame.display.set_mode((1000, 1000))

# Title
pygame.display.set_caption("Configure Page")

# loads an icon of a cog wheel
icon = pygame.image.load('cogwheel.png')


# # Give the window an icon
pygame.display.set_icon(icon)

font = pygame.font.SysFont("arialblack", 20)
button_text = font.render("Start", True, "white")

# button class
class Button:
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.sur = pygame.Rect(x, y, w, h)
        self.font = pygame.font.SysFont("arialblack", 20)
        self.titleFont = pygame.font.SysFont("arialblack", 40)
        self.title_font = self.titleFont.render(text, True, "white")
        self.text_heading = self.font.render(text, True, "white")
        self.button_text = self.font.render(text, True, "black")

    # Method for the headings
    def drawHeading(self, screen):
        self.getPosRect = button_text.get_rect(center=(self.sur.x + self.sur.width/2, self.sur.y + self.sur.height/2))
        pygame.draw.rect(screen, "black", self.sur)
        screen.blit(self.text_heading, self.getPosRect)

    # Method for Title
    def drawTitle(self, screen):
        self.getPosRect = button_text.get_rect(center=(self.sur.x + self.sur.width/2, self.sur.y + self.sur.height/2))
        pygame.draw.rect(screen, "black", self.sur)
        screen.blit(self.title_font, self.getPosRect)

    # Method for buttons
    def drawButton(self, screen):
        self.getPosRect = button_text.get_rect(center=(self.sur.x + self.sur.width/2, self.sur.y + self.sur.height/2))
        self.rect = pygame.draw.rect(screen, "white", self.sur)
        screen.blit(self.button_text, self.getPosRect)

    # checks if the mouse collides with button
    # if mouse collision detected print the following
    def mouseClick(self):
        mousePos = pygame.mouse.get_pos()
        collide = self.rect.collidepoint(mousePos)
        if collide:
            print("button is pressed")

    # function to go back to main_menu through close "button"
    # def backToMenu(self):
    #     if button8.mouseClick():
    #         start_menu()

    # need to give each button individual functionality in the assignment, and its own clicking message

# heading objects
heading1 = Button(450, 250, 0, 0, "Size of field")
heading2 = Button(450, 400, 0, 0, "Game level")
heading3 = Button(450, 550, 0, 0, "Game modes")
heading_title = Button(425, 100, 0, 0, "Settings")

# buttons objects
button1 = Button(390, 300, 200, 45, "10x40")
button2 = Button(300, 450, 100, 45, "level 1")
button3 = Button(425, 450, 100, 45, "level 2")
button4 = Button(550, 450, 100, 45, "level 3")
button5 = Button(225, 600, 125, 45, "Normal")
button6 = Button(400, 600, 175, 45, "Extended")
button7 = Button(625, 600, 100, 45, "AI")
button8 = Button(850, 900, 100, 45, "Close")

# function
def config():

    # game window loops until we press 'exit'
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()   # game quits
                sys.exit()
            
            # condition
            if event.type == pygame.MOUSEBUTTONDOWN:
                # button calls mouse click method
                button1.mouseClick()
                button2.mouseClick()
                button3.mouseClick()
                button4.mouseClick()
                button5.mouseClick()
                button6.mouseClick()
                button7.mouseClick()
                button8.mouseClick()

        screen.fill("black")

        # Draws headings onto the screen
        heading1.drawHeading(screen)
        heading2.drawHeading(screen)
        heading3.drawHeading(screen)
        heading_title.drawTitle(screen)
       
        # Draws button
        button1.drawButton(screen)
        button2.drawButton(screen)
        button3.drawButton(screen)
        button4.drawButton(screen)
        button5.drawButton(screen)
        button6.drawButton(screen)
        button7.drawButton(screen)
        button8.drawButton(screen)

        # lets up update only a portion of whats on the screen
        pygame.display.flip()
        # loops 60fps
        clock.tick(60)

        # game will update
        pygame.display.update()

config()
