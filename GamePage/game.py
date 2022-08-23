import pygame
import math
import copy
import random
from GamePage import pieces
from start_menu.button import Button

pygame.init()
#Initialise global variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
WIDTH = 10
HEIGHT = 20
BLOCK_SIZE = 40
SPAWN = math.ceil(WIDTH/2) - 2

GameMode = 0
GameType = 0
score = 0
level = 1
lines = 0
run = True
image = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
board = []
displayBoard = []
tempBoard = []
nextPiece = random.choice(pieces.options)
nextColour = (pieces.colours[pieces.options.index(nextPiece)])
piece = []
colour = ()
rotation = 0
x = 0
y = 0

#Colour presets
WHITE = (235,235,235)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREY = (100, 100, 100)
DARK_GREY = (50, 50, 50)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def generateBoard():
    #Initialise Game Board
    global board, displayBoard
    board = []
    displayBoard = []
    for i in range(0, HEIGHT+2):
        board.append([0]*WIDTH)
    for i in range(2, len(board)):
        top = 100 + (i-2) * BLOCK_SIZE + 0.5
        row = []
        for j in range(0, len(board[0])):
            left = 300 + j * BLOCK_SIZE + 0.5
            row.append(pygame.Rect(left,top,39,39))
        displayBoard.append(row)

def generatePiece():
    #Generate random piece
    global nextPiece, piece, nextColour, colour, rotation
    rotation = 0
    piece = nextPiece
    colour = nextColour
    nextPiece = random.choice(pieces.options)
    nextColour = pieces.colours[pieces.options.index(nextPiece)]

def addPiece(board):
    #Adds a piece to a specified board
    for i in range(0, len(piece[rotation])):
        for j in range(0, len(piece[rotation][i])):
            if i+y < HEIGHT+2 and SPAWN+x+j < WIDTH and SPAWN+x+j >= 0:
                if board[i+y][SPAWN+j+x] == 0 and piece[rotation][i][j] != 0:
                    board[i+y][SPAWN+j+x] = pieces.colours.index(colour)+1

def checkMove(x, y):
    #Find bottom of piece
    bottom = 0
    for i in range(0, len(piece[rotation])):
        if 1 in piece[rotation][i]:
            bottom = i
    #Check bottom boundary
    if y+bottom >= HEIGHT+2:
        return(2)
    #Find left of piece
    left = 0
    done = False
    for i in range(0, len(piece[rotation][0])):
        for j in piece[rotation]:
            if j[i] == 1:
                left = i
                done = True
                break
        if done: break
    #Check left boundary
    if SPAWN+left+x < 0:
        return(1)
     #Find right of piece
    right = 0
    for i in range(0, len(piece[rotation][0])):
        for j in piece[rotation]:
            if j[i] == 1:
                right = i
    #Check right boundary
    if SPAWN+right+x >= WIDTH:
        return(1)
    #Check bottom collision
    for i in range(0, len(piece[rotation][bottom])):
        if SPAWN+x+i < WIDTH and SPAWN+x+i >= 0:
            if board[y+bottom][SPAWN+x+i] != 0 and piece[rotation][bottom][i] != 0:
                return(2)   
    #Check general collision
    for i in range(0, len(piece[rotation])):
        for j in range(0, len(piece[rotation][i])):
            if i+y < HEIGHT+2 and SPAWN+x+j < WIDTH and SPAWN+x+j >= 0:
                if board[i+y][SPAWN+j+x] != 0 and piece[rotation][i][j] != 0:
                    return(1)
    return(0)

def updateDisplay(board):
    screen.fill(BLACK)

    #Display Group Number
    myFont = pygame.font.SysFont('Roboto', 30)
    Text = myFont.render("GROUP 9", True, YELLOW)
    screen.blit(Text, (850,950))

    #Display Game Settings
    pygame.draw.rect(screen, WHITE, pygame.Rect(50, 150, 200, 100))
    pygame.draw.rect(screen, DARK_GREY, pygame.Rect(54, 154, 192, 92))
    pygame.draw.rect(screen, GREY, pygame.Rect(58, 158, 184, 84))
    myFont = pygame.font.SysFont('Roboto', 30)
        #Game Type
    if GameType == 0:
        Text = myFont.render("Normal Game", True, WHITE)
    else:
        Text = myFont.render("Extended Game", True, WHITE)
    screen.blit(Text, (75,170))
        #Game Mode
    if GameMode == 0:
        Text = myFont.render("Player Mode", True, WHITE)
    else:
        Text = myFont.render("AI Mode", True, WHITE)
    screen.blit(Text, (75,205))

    #Display Game Stats
    pygame.draw.rect(screen, WHITE, pygame.Rect(50, 350, 200, 300))
    pygame.draw.rect(screen, DARK_GREY, pygame.Rect(54, 354, 192, 292))
    pygame.draw.rect(screen, GREY, pygame.Rect(58, 358, 184, 284))
    statFont = pygame.font.SysFont('Roboto', 40)
    numberFont = pygame.font.SysFont('Roboto Thin', 30, False, True)
        #Score
    Text = statFont.render("SCORE", True, WHITE)
    screen.blit(Text, (100, 380))
    pygame.draw.rect(screen, DARK_GREY, pygame.Rect(80, 415, 140, 30))
    Text = numberFont.render("%d" %score, True, WHITE)
    screen.blit(Text, (90, 420))
        #Level
    Text = statFont.render("LEVEL", True, WHITE)
    screen.blit(Text, (100, 470))
    pygame.draw.rect(screen, DARK_GREY, pygame.Rect(80, 505, 140, 30))
    Text = numberFont.render("%d" %level, True, WHITE)
    screen.blit(Text, (90, 510))
        #Lines
    Text = statFont.render("LINES", True, WHITE)
    screen.blit(Text, (100, 560))
    pygame.draw.rect(screen, DARK_GREY, pygame.Rect(80, 595, 140, 30))
    Text = numberFont.render("%d" %lines, True, WHITE)
    screen.blit(Text, (90, 600))

    #Display Next Piece
    pygame.draw.rect(screen, WHITE, pygame.Rect(746, 146, 158, 158))
    pygame.draw.rect(screen, DARK_GREY, pygame.Rect(750, 150, 150, 150))
    pygame.draw.rect(screen, GREY, pygame.Rect(754, 154, 142, 142))
    pygame.draw.rect(screen, DARK_GREY, pygame.Rect(760, 195, 130, 90))
        #Text
    myFont = pygame.font.SysFont('Roboto', 30)
    Text = myFont.render("NEXT", True, WHITE)
    screen.blit(Text, (800,165))
        #Piece
    for i in range(0, len(nextPiece[0])):
        for j in range(0, len(nextPiece[0][i])):
            if nextPiece[0][i][j] == 1:
                if nextPiece == pieces.O:
                    if image:
                        screen.blit(pygame.transform.scale(pieces.images[pieces.colours.index(nextColour)], (28,28)), (765+30*j, 210+30*i))
                    else:
                        pygame.draw.rect(screen, nextColour, pygame.Rect(765+30*j, 210+30*i, 28, 28))
                elif nextPiece == pieces.I:
                    if image:
                        screen.blit(pygame.transform.scale(pieces.images[pieces.colours.index(nextColour)], (28,28)), (765+30*j, 195+30*i))
                    else:
                        pygame.draw.rect(screen, nextColour, pygame.Rect(765+30*j, 195+30*i, 28, 28))
                else:
                    if image:
                        screen.blit(pygame.transform.scale(pieces.images[pieces.colours.index(nextColour)], (28,28)), (780+30*j, 210+30*i))
                    else:
                        pygame.draw.rect(screen, nextColour, pygame.Rect(780+30*j, 210+30*i, 28, 28))

    #Display Current Game Board
    pygame.draw.rect(screen, WHITE, pygame.Rect(284, 84, BLOCK_SIZE*WIDTH+32, BLOCK_SIZE*HEIGHT+32))
    pygame.draw.rect(screen, DARK_GREY, pygame.Rect(288, 88, BLOCK_SIZE*WIDTH+24, BLOCK_SIZE*HEIGHT+24))
    pygame.draw.rect(screen, WHITE, pygame.Rect(296, 96, BLOCK_SIZE*WIDTH+8, BLOCK_SIZE*HEIGHT+8))
    if image:
        pygame.draw.rect(screen, BLACK, pygame.Rect(300, 100, BLOCK_SIZE*WIDTH, BLOCK_SIZE*HEIGHT))
    else:
        pygame.draw.rect(screen, GREY, pygame.Rect(300, 100, BLOCK_SIZE*WIDTH, BLOCK_SIZE*HEIGHT))
        #Game Board
    for i in range(2, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] != 0:
                if image:
                    screen.blit(pieces.images[board[i][j]-1], displayBoard[i-2][j].topleft)
                else:
                    pygame.draw.rect(screen, pieces.colours[board[i][j]-1], displayBoard[i-2][j])
            else:
                pygame.draw.rect(screen, BLACK, displayBoard[i-2][j])
    
    pygame.display.update()
    
def moveLeft():
    #Moves the active piece left
    global x, y
    if checkMove(x-1, y) == 0:
        x -= 1
        tempBoard = copy.deepcopy(board)
        addPiece(tempBoard)
        updateDisplay(tempBoard)

def moveRight():
    #Moves the active piece right
    global x, y
    if checkMove(x+1, y) == 0:
        x += 1
        tempBoard = copy.deepcopy(board)
        addPiece(tempBoard)
        updateDisplay(tempBoard)

def moveDown():
    #Moves the active down
    global piece, x, y
    if checkMove(x, y+1) == 0:
        y += 1
    else:
        addPiece(board)
        generatePiece()
        x = 0
        y = 0
        #Check for filled lines
        checkLines()
        #Check for losing conditions
        checkLose()
    tempBoard = copy.deepcopy(board)
    addPiece(tempBoard)
    updateDisplay(tempBoard)

def rotate():
    #Rotates the active piece
    global rotation, x, y
    if rotation == 3:
        rotation = 0
    else:
        rotation += 1
    #Check nearby for valid rotation space
    if checkMove(x, y) != 0:
        if checkMove(x+1, y) == 0:
            x += 1
        elif checkMove(x-1, y) == 0:
            x -= 1
        elif checkMove(x, y-1) == 0:
            y -= 1
        elif checkMove(x+2, y) == 0:
            x += 2
        elif checkMove(x-2, y) == 0:
            x -= 2
        else:
            rotation -= 1
    tempBoard = copy.deepcopy(board)
    addPiece(tempBoard)
    updateDisplay(tempBoard)

def checkLines():
    #Check for and remove full lines
    global board, score, lines, level
    fullLines = []
    for i in range(2, len(board)):
        if 0 not in board[i]:
            fullLines.append(i)
            #Increse current score
            score += 100*len(fullLines)
    for i in fullLines:
        board.pop(i)
        board.insert(2, [0]*WIDTH)
    #Increase lines cleared
    lines += len(fullLines)
    if lines >= level*10:
        #Increase level
        level += 1

def checkLose():
    #Check for losing conditions
    global run
    for i in board[1]:
        if i != 0:
            #Display Game Over
            GameOver = pygame.image.load('GamePage/images/Game-Over.png')
            GameOver = pygame.transform.scale(GameOver, (400,250))
            screen.blit(GameOver, (300,200))
            pygame.display.update()
                #Wait for input
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

def finishGame():
    global run
    #Display finish game dialog box
    pygame.draw.rect(screen, RED, pygame.Rect(245, 195, 510, 210))
    pygame.draw.rect(screen, WHITE, pygame.Rect(250, 200, 500, 200))
    pygame.draw.rect(screen, DARK_GREY, pygame.Rect(254, 204, 492, 192))
    pygame.draw.rect(screen, GREY, pygame.Rect(258, 208, 484, 184))
    pygame.draw.rect(screen, RED, pygame.Rect(300, 280, 400, 10))
    #Display text
    myFont = pygame.font.SysFont('Roboto', 80)
    Text = myFont.render("FINISH GAME?", True, RED)
    screen.blit(Text, (300,230))
    #Display buttons
    myFont = pygame.font.SysFont('Roboto', 50)
    yesButton = Button("YES", (400, 340), myFont, WHITE)
    yesButton.update(screen)
    noButton = Button("NO", (600, 340), myFont, WHITE)
    noButton.update(screen)
    pygame.display.update()
    #Wait for input
    check = True
    while run and check:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if yesButton.checkInput(mouse_pos):
                    run = False
                if noButton.checkInput(mouse_pos):
                    check = False

def runGame(inputSize = (10,20), inputLevel = 0, inputGameType = 0, inputGameMode = 0):
    global WIDTH, HEIGHT, GameType, GameMode, board, displayBoard, tempBoard, run, x, y, score, level, lines, image
    #Adjust game base on given inputs parameters
    WIDTH, HEIGHT = inputSize
    level = inputLevel
    GameType = inputGameType
    GameMode = inputGameMode
    #Reset and initialise game varaibles
    image = False
    run = True
    x = 0
    y = 0
    score = 0
    lines = 0

    generateBoard()
    tempBoard = copy.deepcopy(board)
    generatePiece()
    addPiece(tempBoard)
    updateDisplay(tempBoard)

    pygame.display.set_caption("TETRIS")
    clock = pygame.time.Clock()
    prevTime = pygame.time.get_ticks()

    #Main loop
    while run:
        #Move down every second
        clock.tick(12)
        time = pygame.time.get_ticks()
        if time - prevTime >= 1000:
            prevTime = time
            moveDown()
        #Check for inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                #Rotate if up key
                if event.key == pygame.K_UP:
                    rotate()
                #Finish game dialog box in escape
                if event.key == pygame.K_ESCAPE:
                    finishGame()
                #Activate Image Mode
                if event.key == pygame.K_p:
                    if image == True:
                        image = False
                    else:
                        image = True
                    tempBoard = copy.deepcopy(board)
                    addPiece(tempBoard)
                    updateDisplay(tempBoard)
        #Check for keys being held down
        keys = pygame.key.get_pressed()
        #Move left if left key
        if keys[pygame.K_LEFT]:
            moveLeft()
        #Move right if right key
        if keys[pygame.K_RIGHT]:
            moveRight()
        #Move down if down key
        if keys[pygame.K_DOWN]:
            moveDown()