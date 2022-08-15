import pygame
import math
import copy
import os
import random
import pieces

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
WIDTH = 10
HEIGHT = 10
SPAWN = math.ceil(WIDTH/2) - 2

def generateBoard():
    board = []
    for i in range(0, HEIGHT+2):
        board.append([0]*WIDTH)
    displayBoard = []

    for i in range(0, len(board)):
        top = i * 50 + 1
        row = []
        for j in range(0, len(board[0])):
            left = j * 50 + 1
            row.append(pygame.Rect(left,top,48,48))
        displayBoard.append(row)
    return(board, displayBoard)

def generatePiece():
    return(random.choice(pieces.options))

def addPiece(board, piece, x=0, y=0):
    for i in range(0, len(piece[rotation])):
        for j in range(0, len(piece[rotation][i])):
            if i+y < HEIGHT+2 and SPAWN+x+j < WIDTH and SPAWN+x+j >= 0:
                if board[i+y][SPAWN+j+x] == 0:
                    board[i+y][SPAWN+j+x] = piece[rotation][i][j]
    return

def checkMove(board, piece, x, y):
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
            if board[y+bottom][SPAWN+x+i] == 1 and piece[rotation][bottom][i] == 1:
                return(2)   
    #Check general collision
    for i in range(0, len(piece[rotation])):
        for j in range(0, len(piece[rotation][i])):
            if i+y < HEIGHT+2 and SPAWN+x+j < WIDTH and SPAWN+x+j >= 0:
                if board[i+y][SPAWN+j+x] == 1 and piece[rotation][i][j] == 1:
                    return(1)
    return(0)

def updateDisplay(board):
    screen.fill((0,0,0))
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 1:
                pygame.draw.rect(screen, (255, 0, 0), displayBoard[i][j])
            else:
                pygame.draw.rect(screen, (100, 100, 100), displayBoard[i][j])
    myFont = pygame.font.SysFont('Comic Sans MS', 30)
    text = myFont.render("SCORE: %d" %score, False, (255,255,255))
    screen.blit(text, (700,100))
    pygame.display.update()
    return

def moveLeft():
    global x, y
    if checkMove(board, piece, x-1, y) == 0:
        x -= 1
        tempBoard = copy.deepcopy(board)
        addPiece(tempBoard, piece, x, y)
        updateDisplay(tempBoard)
    return

def moveRight():
    global x, y
    if checkMove(board, piece, x+1, y) == 0:
        x += 1
        tempBoard = copy.deepcopy(board)
        addPiece(tempBoard, piece, x, y)
        updateDisplay(tempBoard)
    return

def moveDown():
    global piece, x, y
    if checkMove(board, piece, x, y+1) == 0:
        y += 1
    else:
        addPiece(board, piece, x, y)
        piece = generatePiece()
        x = 0
        y = 0
    checkLines()
    tempBoard = copy.deepcopy(board)
    addPiece(tempBoard, piece, x, y)
    updateDisplay(tempBoard)
    checkLose()
    return

def rotate():
    global piece, rotation, x, y
    if rotation == 3:
        rotation = 0
    else:
        rotation += 1
    if checkMove(board, piece, x, y) != 0:
        if checkMove(board, piece, x+1, y) == 0:
            x += 1
        elif checkMove(board, piece, x-1, y) == 0:
            x -= 1
        elif checkMove(board, piece, x, y-1) == 0:
            y -= 1
        elif checkMove(board, piece, x+2, y) == 0:
            x += 2
        elif checkMove(board, piece, x-2, y) == 0:
            x -= 2
    tempBoard = copy.deepcopy(board)
    addPiece(tempBoard, piece, x, y)
    updateDisplay(tempBoard)
    return

def checkLines():
    global board, score
    fullLines = []
    for i in range(2, len(board)):
        if 0 not in board[i]:
            fullLines.append(i)
            score += 100*len(fullLines)
    for i in fullLines:
        board.pop(i)
        board.insert(2, [0]*WIDTH)
    return

def checkLose():
    if 1 in board[1]:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(200,200,600,600))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(205,205,590,590))
        myFont = pygame.font.SysFont('Comic Sans MS', 100)
    pygame.time.wait(10000)
    pygame.quit()
    exit()

##  MAIN  ##

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TETRIS")

board, displayBoard = generateBoard()

clock = pygame.time.Clock()
prevTime = pygame.time.get_ticks()

piece = generatePiece()
rotation = 0
tempBoard = copy.deepcopy(board)
x = 0
y = 0
score = 0
addPiece(tempBoard, piece, x, y)
updateDisplay(tempBoard)
while True:
    
    clock.tick(12)
    time = pygame.time.get_ticks()
    if time - prevTime >= 1000:
        prevTime = time
        moveDown()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        moveLeft(board, piece)
        
    if keys[pygame.K_RIGHT]:
        moveRight(board, piece)
    
    if keys[pygame.K_DOWN]:
        moveDown()
