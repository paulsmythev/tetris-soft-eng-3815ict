import math
import copy
import random
from GamePage import pieces

class Piece:
    rotation = 0
    def __init__(self, x, y):
        self.type = random.choice(pieces.options)
        self.colour = pieces.colours[pieces.options.index(self.type)]
        self.second_colour = pieces.second_colours[pieces.options.index(self.type)]
        self.x = x
        self.y = y

#MODEL
class Game:
    OFF_SET = 2
    score = 0
    lines = 0
    prev_lines = 0
    speeds = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    tempo = 0
    songs = ["GamePage/assets/Tetris_Theme_1.mp3", "GamePage/assets/Tetris_Theme_1.2.mp3"
            ,"GamePage/assets/Tetris_Theme_1.4.mp3", "GamePage/assets/Tetris_Theme_1.6.mp3"
            ,"GamePage/assets/Tetris_Theme_1.8.mp3", "GamePage/assets/Tetris_Theme_2.mp3"]

    def __init__(self, size, level, game_type, game_mode):
        self.board = []
        self.visual_board = []
        self.WIDTH, self.HEIGHT = size
        self.BLOCK_SIZE = 40/(self.WIDTH/10)
        self.SPAWN = math.ceil(self.WIDTH/2)-2
        self.piece = Piece(self.SPAWN, 0)
        self.next_piece = Piece(self.SPAWN, 0)
        self.level = level
        self.game_type = game_type
        self.game_mode = game_mode
        self.__initialise_boards()
        self.add_piece(self.visual_board, self.piece)

    def __initialise_boards(self):
        #Initialise game board
        for i in range(0, self.HEIGHT+2):
            self.board.append([0]*self.WIDTH)
        #Initialise visual board
        self.visual_board = copy.deepcopy(self.board)

    def generate_piece(self):
        self.piece = self.next_piece
        self.next_piece = Piece(self.SPAWN, 0)

    def add_piece(self, board, piece):
        for i in range(0, len(piece.type[piece.rotation])):
            for j in range(0, len(piece.type[piece.rotation][i])):
                if i+piece.y < self.HEIGHT+2 and j+piece.x < self.WIDTH and j+piece.x >= 0:
                    if board[i+piece.y][j+piece.x] == 0 and piece.type[piece.rotation][i][j] != 0:
                        board[i+piece.y][j+piece.x] = pieces.colours.index(piece.colour)+1

    def check_move(self, x, y, rotation):
        #Find bottom of piece
        bottom = 0
        for i in range(0, len(self.piece.type[rotation])):
            if 1 in self.piece.type[rotation][i]:
                bottom = i
        #Check bottom boundary
        if y+bottom >= self.HEIGHT+2:
            return 2
        
        #Find left of piece
        left = 0
        for i in range(len(self.piece.type[rotation][0])-1, -1, -1):
            for j in self.piece.type[rotation]:
                if j[i] == 1:
                    left = i
        #Check left boundary
        if x+left < 0:
            return 1
        
        #Find right of piece
        right = 0
        for i in range(0, len(self.piece.type[rotation][0])):
            for j in self.piece.type[rotation]:
                if j[i] == 1:
                    right = i
        #Check right boundary
        if x+right >= self.WIDTH:
            return 1
        
        #Check bottom collision
        for i in range(0, len(self.piece.type[rotation][0])):
            if x+i < self.WIDTH and x+i >= 0:
                if self.board[y+bottom][x+i] != 0 and self.piece.type[rotation][bottom][i] != 0:
                    return 2
        
        #Check side collision
        for i in range(0, len(self.piece.type[rotation])):
            for j in range(0, len(self.piece.type[rotation][i])):
                if i+y < self.HEIGHT+2 and x+j < self.WIDTH and x+j >= 0:
                    if self.board[i+y][j+x] != 0 and self.piece.type[rotation][i][j] != 0:
                        return 1
        
        #Return 0 if no collisions
        return 0
