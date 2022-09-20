import pygame
import math
import copy
import random
from GamePage import pieces
from start_menu.button import Button

#Colour presets
WHITE = (235,235,235)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREY = (100, 100, 100)
DARK_GREY = (50, 50, 50)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()

class Piece:
    rotation = 0
    def __init__(self, x, y):
        self.type = random.choice(pieces.options)
        self.colour = (pieces.colours[pieces.options.index(self.type)])
        self.x = x
        self.y = y

#MODEL
class Game:
    BLOCK_SIZE = 40
    OFF_SET = 0.5
    board = []
    visual_board = []
    score = 0
    lines = 0

    def __init__(self, size, level, game_type, game_mode):
        self.WIDTH, self.HEIGHT = size
        self.SPAWN = math.ceil(self.WIDTH/2)-2
        self.piece = Piece(self.SPAWN, 0)
        self.next_piece = Piece(self.SPAWN, 0)
        self.level = level
        self.game_type = game_type
        self.game_mode = game_mode
        self.__initialise_boards()
        self.add_piece(self.visual_board)

    def __initialise_boards(self):
        #Initialise game board
        for i in range(0, self.HEIGHT+2):
            self.board.append([0]*self.WIDTH)
        #Initialise visual board
        self.visual_board = copy.deepcopy(self.board)

    def generate_piece(self):
        self.piece = self.next_piece
        self.next_piece = Piece(self.SPAWN, 0)

    def add_piece(self, board):
        for i in range(0, len(self.piece.type[self.piece.rotation])):
            for j in range(0, len(self.piece.type[self.piece.rotation][i])):
                if i+self.piece.y < self.HEIGHT+2 and j+self.piece.x < self.WIDTH and j+self.piece.x >= 0:
                    if board[i+self.piece.y][j+self.piece.x] == 0 and self.piece.type[self.piece.rotation][i][j] != 0:
                        board[i+self.piece.y][j+self.piece.x] = pieces.colours.index(self.piece.colour)+1

    def check_move(self, x, y):
        #Find bottom of piece
        bottom = 0
        for i in range(0, len(self.piece.type[self.piece.rotation])):
            if 1 in self.piece.type[self.piece.rotation][i]:
                bottom = i
        #Check bottom boundary
        if y+bottom >= self.HEIGHT+2:
            return 2
        
        #Find left of piece
        left = 0
        for i in range(len(self.piece.type[self.piece.rotation][0])-1, -1, -1):
            for j in self.piece.type[self.piece.rotation]:
                if j[i] == 1:
                    left = i
        #Check left boundary
        if x+left < 0:
            return 1
        
        #Find right of piece
        right = 0
        for i in range(0, len(self.piece.type[self.piece.rotation][0])):
            for j in self.piece.type[self.piece.rotation]:
                if j[i] == 1:
                    right = i
        #Check right boundary
        if x+right >= self.WIDTH:
            return 1
        
        #Check bottom collision
        for i in range(0, len(self.piece.type[self.piece.rotation][0])):
            if x+i < self.WIDTH and x+i >= 0:
                if self.board[y+bottom][x+i] != 0 and self.piece.type[self.piece.rotation][bottom][i] != 0:
                    return 2
        
        #Check side collision
        for i in range(0, len(self.piece.type[self.piece.rotation])):
            for j in range(0, len(self.piece.type[self.piece.rotation][i])):
                if i+y < self.HEIGHT+2 and x+j < self.WIDTH and x+j >= 0:
                    if self.board[i+y][j+x] != 0 and self.piece.type[self.piece.rotation][i][j] != 0:
                        return 1
        
        #Return 0 if no collisions
        return 0

                

#VIEW
class Display:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display_board = []

    def __init__(self, game):
        self.game = game
        self.__initialise_board()
        pygame.display.set_caption("TETRIS")
        self.update_display()

    def __initialise_board(self):
        #Initialise display board
        for i in range(0, self.game.HEIGHT):
            top = 100 + i * self.game.BLOCK_SIZE + self.game.OFF_SET
            row = []
            for j in range(0, self.game.WIDTH):
                left = 300 + j * self.game.BLOCK_SIZE + self.game.OFF_SET
                row.append(pygame.Rect(left, top, self.game.BLOCK_SIZE-2*self.game.OFF_SET, self.game.BLOCK_SIZE-2*self.game.OFF_SET))
            self.display_board.append(row)
        
    def update_display(self):
        self.screen.fill(BLACK)

        #Display Group Number
        my_font = pygame.font.SysFont('Roboto', 30)
        text = my_font.render("GROUP 9", True, YELLOW)
        self.screen.blit(text, (850,950))

        #Display Game Settings
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(50, 150, 200, 100))
        pygame.draw.rect(self.screen, DARK_GREY, pygame.Rect(54, 154, 192, 92))
        pygame.draw.rect(self.screen, GREY, pygame.Rect(58, 158, 184, 84))
        my_font = pygame.font.SysFont('Roboto', 30)
            #game type
        if self.game.game_type == 0:
            text = my_font.render("Normal Game", True, WHITE)
        else:
            text = my_font.render("Extended Game", True, WHITE)
        self.screen.blit(text, (75, 170))
            #game mode
        if self.game.game_mode == 0:
            text = my_font.render("Player Mode", True, WHITE)
        else:
            text = my_font.render("AI Mode", True, WHITE)
        self.screen.blit(text, (75,205))

        #Display Game Stats
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(50, 350, 200, 300))
        pygame.draw.rect(self.screen, DARK_GREY, pygame.Rect(54, 354, 192, 292))
        pygame.draw.rect(self.screen, GREY, pygame.Rect(58, 358, 184, 284))
        stat_font = pygame.font.SysFont('Roboto', 40)
        number_font = pygame.font.SysFont('Roboto Thin', 30, False, True)
            #score
        text = stat_font.render("SCORE", True, WHITE)
        self.screen.blit(text, (100, 380))
        pygame.draw.rect(self.screen, DARK_GREY, pygame.Rect(80, 415, 140, 30))
        text = number_font.render("%d" %self.game.score, True, WHITE)
        self.screen.blit(text, (90, 420))
            #level
        text = stat_font.render("LEVEL", True, WHITE)
        self.screen.blit(text, (100, 470))
        pygame.draw.rect(self.screen, DARK_GREY, pygame.Rect(80, 505, 140, 30))
        text = number_font.render("%d" %self.game.level, True, WHITE)
        self.screen.blit(text, (90, 510))
            #lines
        text = stat_font.render("LINES", True, WHITE)
        self.screen.blit(text, (100, 560))
        pygame.draw.rect(self.screen, DARK_GREY, pygame.Rect(80, 595, 140, 30))
        text = number_font.render("%d" %self.game.lines, True, WHITE)
        self.screen.blit(text, (90, 600))
        
        #Display Next Piece
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(746, 146, 158, 158))
        pygame.draw.rect(self.screen, DARK_GREY, pygame.Rect(750, 150, 150, 150))
        pygame.draw.rect(self.screen, GREY, pygame.Rect(754, 154, 142, 142))
        pygame.draw.rect(self.screen, DARK_GREY, pygame.Rect(760, 195, 130, 90))
            #text
        my_font = pygame.font.SysFont('Roboto', 30)
        text = my_font.render("NEXT", True, WHITE)
        self.screen.blit(text, (800,165))
            #piece
        for i in range(0, len(self.game.next_piece[0])):
            for j in range(0, len(self.game.next_piece[0][i])):
                if self.game.next_piece[0][i][j] == 1:
                    if self.game.next_piece == pieces.O:
                        pygame.draw.rect(self.screen, self.game.next_piece.colour, pygame.Rect(765+30*j, 210+30*i, 28, 28))
                    elif self.game.next_piece == pieces.I:
                        pygame.draw.rect(self.screen, self.game.next_piece.colour, pygame.Rect(765+30*j, 195+30*i, 28, 28))
                    else:
                        pygame.draw.rect(self.screen, self.game.next_piece.colour, pygame.Rect(780+30*j, 210+30*i, 28, 28))

        #Display Game Board
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(284, 84, self.game.BLOCK_SIZE*self.game.WIDTH+32, self.game.BLOCK_SIZE*self.game.HEIGHT+32))
        pygame.draw.rect(self.screen, DARK_GREY, pygame.Rect(288, 88, self.game.BLOCK_SIZE*self.game.WIDTH+24, self.game.BLOCK_SIZE*self.game.HEIGHT+24))
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(296, 96, self.game.BLOCK_SIZE*self.game.WIDTH+8, self.game.BLOCK_SIZE*self.game.HEIGHT+8))
        pygame.draw.rect(self.screen, GREY, pygame.Rect(300, 100,self.game. BLOCK_SIZE*self.game.WIDTH, self.game.BLOCK_SIZE*self.game.HEIGHT))
        for i in range(2, len(self.game.visual_board)):
            for j in range(0, len(self.game.visual_board[i])):
                pygame.draw.rect(self.screen, pieces.colours[self.game.visual_board[i][j]], self.display_board[i-2][j])

        pygame.display.update()

#CONTROLLER
class Controller:

    def __init__(self, game, display):
        self.game = game
        self.display = display

    def move_left(self):
        if self.game.check_move(self.game.piece.x-1, self.game.piece.y) == 0:
            self.game.piece.x -= 1
            self.game.visual_board = copy.deepcopy(self.game.board)
            self.game.add_piece(self.game.visual_board)
            self.display.update_display()

    def move_right(self):
        if self.game.check_move(self.game.piece.x+1, self.game.piece.y) == 0:
            self.game.piece.x += 1
            self.game.visual_board = copy.deepcopy(self.game.board)
            self.game.add_piece(self.game.visual_board)
            self.display.update_display()

    def move_down(self):
        if self.game.check_move(self.game.piece.x, self.game.piece.y+1) == 0:
            self.game.piece.y += 1
        else:
            self.game.add_piece(self.game.board)
            self.game.generate_piece()
            self.check_lines()
            self.check_lose()
        self.game.visual_board = copy.deepcopy(self.game.board)
        self.game.add_piece(self.game.visual_board)
        self.display.update_display()
    
    def rotate(self):
        #Rotate the piece
        if self.game.piece.rotation == 3:
            self.game.piece.rotation = 0
        else:
            self.game.piece.rotation += 1
        #Check nearby for void rotation space
        if self.game.check_move(self.game.piece.x, self.game.piece.y) != 0:
            if self.game.check_move(self.game.piece.x+1, self.game.piece.y) == 0:
                x += 1
            elif self.game.check_move(self.game.piece.x-1, self.game.piece.y) == 0:
                x -= 1
            elif self.game.check_move(self.game.piece.x, self.game.piece.y-1) == 0:
                y -= 1
            elif self.game.check_move(self.game.piece.x+2, self.game.piece.y) == 0:
                x += 2
            elif self.game.check_move(self.game.piece.x-2, self.game.piece.y) == 0:
                x -= 2
            else:
                self.game.piece.rotation -= 1
            self.game.visual_board = copy.deepcopy(self.game.board)
            self.game.add_piece(self.game.visual_board)
            self.display.update_display()

    def check_lines(self):
        full_lines = []
        for i in range(2, len(self.game.board)):
            if 0 not in self.game.board[i]:
                full_lines.append(i)
                #Increase score
                self.game.score += 100 * len(full_lines)
        for i in full_lines:
            self.game.board.pop(i)
            self.game.board.insert(2, [0]*self.game.WIDTH)
        #Increase lines cleared
        self.game.lines += len(full_lines)
        if self.game.lines >= self.game.level * 10:
            #Increase level
            self.game.level += 1

    def check_lose(self):
        
