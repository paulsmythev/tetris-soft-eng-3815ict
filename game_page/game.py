import math
import copy
import random
from game_page import pieces

# This class holds and initialises game pieces
class Piece:
    # Piece rotation variables
    rotation = 0
    # Piece constructor
    def __init__(self, x, y, game_mode):
        # Randomly assign a new piece from the game mode selection
        if game_mode == 0:
            self.type = random.choice(pieces.options)
            self.colour = pieces.colours[pieces.options.index(self.type)]
            self.second_colour = pieces.second_colours[pieces.options.index(self.type)]
        else:
            self.type = random.choice(pieces.extended_options)
            self.colour = pieces.colours[pieces.extended_options.index(self.type)]
            self.second_colour = pieces.second_colours[pieces.extended_options.index(self.type)]
        # Set piece coordinates based on given arguments
        self.x = x
        self.y = y

# This class holds the variables and functions of the game data
class Game:
    # Initialise game varaibles
    OFF_SET = 2
    score = 0
    lines = 0
    prev_lines = 0
    # List of game level speeds
    speeds = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    # Initialise theme tempo and theme songs list
    tempo = 0
    songs = ["assets/sounds/theme_1_0.mp3", "assets/sounds/theme_1_2.mp3"
            ,"assets/sounds/theme_1_4.mp3", "assets/sounds/theme_1_6.mp3"
            ,"assets/sounds/theme_1_8.mp3", "assets/sounds/theme_2_0.mp3"]

    # This is the class constructor
    def __init__(self, size, level, game_type, game_mode):
        # Initialise game with given settings
        self.level = level
        self.game_type = game_type
        self.game_mode = game_mode
        self.WIDTH, self.HEIGHT = size
        # Initialise block size and spawn coordinates
        self.BLOCK_SIZE = 40/(self.WIDTH/10)
        self.SPAWN = math.ceil(self.WIDTH/2)-2
        # Initialise the current and next piece
        self.piece = Piece(self.SPAWN, 0, self.game_mode)
        self.next_piece = Piece(self.SPAWN, 0, self.game_mode)
        # Initialise the game board and visual board
        self.board = []
        self.visual_board = []
        self.__initialise_boards()
        # Add piece to visual board
        self.add_piece(self.visual_board, self.piece)

    # This private class function initialises the game board and visual board
    def __initialise_boards(self):
        #Initialise game board
        for i in range(0, self.HEIGHT+2):
            self.board.append([0]*self.WIDTH)
        #Initialise visual board
        self.visual_board = copy.deepcopy(self.board)

    # This class function generates a new piece
    def generate_piece(self):
        # Make current piece equal to next piece
        self.piece = self.next_piece
        # Create and construct new next piece
        self.next_piece = Piece(self.SPAWN, 0, self.game_mode)

    # This class function adds a given piece to a given board
    def add_piece(self, board, piece):
        # For each slot in the board
        for i in range(0, len(piece.type[piece.rotation])):
            for j in range(0, len(piece.type[piece.rotation][i])):
                # If the piece slot is with in the board bounds add it to the board
                if i+piece.y < self.HEIGHT+2 and j+piece.x < self.WIDTH and j+piece.x >= 0:
                    if board[i+piece.y][j+piece.x] == 0 and piece.type[piece.rotation][i][j] != 0:
                        board[i+piece.y][j+piece.x] = pieces.colours.index(piece.colour)+1

    # This class function checks if a move is possible
    def check_move(self, x, y, rotation):
        # Find bottom of piece
        bottom = 0
        for i in range(0, len(self.piece.type[rotation])):
            if 1 in self.piece.type[rotation][i]:
                bottom = i
        # Check bottom boundary
        if y+bottom >= self.HEIGHT+2:
            return 2
        
        # Find left of piece
        left = 0
        for i in range(len(self.piece.type[rotation][0])-1, -1, -1):
            for j in self.piece.type[rotation]:
                if j[i] == 1:
                    left = i
        # Check left boundary
        if x+left < 0:
            return 1
        
        # Find right of piece
        right = 0
        for i in range(0, len(self.piece.type[rotation][0])):
            for j in self.piece.type[rotation]:
                if j[i] == 1:
                    right = i
        # Check right boundary
        if x+right >= self.WIDTH:
            return 1
        
        # Check bottom collision
        for i in range(0, len(self.piece.type[rotation][0])):
            if x+i < self.WIDTH and x+i >= 0:
                if self.board[y+bottom][x+i] != 0 and self.piece.type[rotation][bottom][i] != 0:
                    return 2
        
        # Check side collision
        for i in range(0, len(self.piece.type[rotation])):
            for j in range(0, len(self.piece.type[rotation][i])):
                if i+y < self.HEIGHT+2 and x+j < self.WIDTH and x+j >= 0:
                    if self.board[i+y][j+x] != 0 and self.piece.type[rotation][i][j] != 0:
                        return 1
        
        # Return 0 if no collisions
        return 0
