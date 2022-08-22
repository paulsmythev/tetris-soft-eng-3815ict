# third version
# buttons can detect if the mouse is clicking them
# any potential ui designs may be altered for preference
# Lastly, configure page needs to be connected to the start-up


# imports pygame module
import pygame, sys

# initialise module
pygame.init()
# initialise clock
clock = pygame.time.Clock()

# Creates the screen
screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption("Configure Page")

# load the icon as an image
# icon = pygame.image.load('tetris.png')


# # Give the window an icon
# pygame.display.set_icon(icon)

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
        self.button_text = self.font.render(text, True, "white")
        self.text_heading = self.font.render(text, True, "black")


    # Method for the headings
    def drawHeading(self, screen):
        self.getPosRect = button_text.get_rect(center=(self.sur.x + self.sur.width/2, self.sur.y + self.sur.height/2))
        pygame.draw.rect(screen, "black", self.sur)
        screen.blit(self.button_text, self.getPosRect)

    # Method for buttons
    def drawButton(self, screen):
        self.getPosRect = button_text.get_rect(center=(self.sur.x + self.sur.width/2, self.sur.y + self.sur.height/2))
        self.rect = pygame.draw.rect(screen, "white", self.sur)
        screen.blit(self.text_heading, self.getPosRect)

    # checks if the mouse collides with button
    # if collision detected print the following
    def mouseClick(self):
        mousePos = pygame.mouse.get_pos()
        collide = self.rect.collidepoint(mousePos)
        if collide:
            print("button is pressed")

# heading objects
heading1 = Button(250, 100, 200, 45, "Size of field")
heading2 = Button(250, 200, 200, 45, "Game level")
heading3 = Button(250, 300, 200, 45, "Game modes")


# buttons objects
button1 = Button(275, 150, 200, 45, "10x40")
button2 = Button(245, 250, 100, 45, "level 1")
button3 = Button(350, 250, 100, 45, "level 2")
button4 = Button(455, 250, 100, 45, "level 3")
button5 = Button(190, 350, 125, 45, "Normal")
button6 = Button(320, 350, 175, 45, "Extended")
button7 = Button(500, 350, 100, 45, "AI")
button8 = Button(600, 500, 100, 45, "Close")


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
