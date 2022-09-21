import pygame
from start_menu.button import Button
from GamePage import pieces

class Display:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display_board = []
    
    WHITE = (235,235,235)
    BLACK = (0,0,0)
    BLUE = (0,0,255)
    GREY = (100, 100, 100)
    DARK_GREY = (50, 50, 50)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    def __init__(self, game):
        self.game = game
        self.__initialise_board()
        pygame.display.set_caption("TETRIS")
        self.update_display()

    def __initialise_board(self):
        #Initialise display board
        for i in range(0, self.game.HEIGHT):
            top = 100 + i * self.game.BLOCK_SIZE
            row = []
            for j in range(0, self.game.WIDTH):
                left = 300 + j * self.game.BLOCK_SIZE
                row.append([pygame.Rect(left-2, top-2, self.game.BLOCK_SIZE+4, self.game.BLOCK_SIZE+4)
                            ,pygame.Rect(left+self.game.OFF_SET, top+self.game.OFF_SET, self.game.BLOCK_SIZE-2*self.game.OFF_SET, self.game.BLOCK_SIZE-2*self.game.OFF_SET)
                            ,pygame.Rect(left+3*self.game.OFF_SET, top+3*self.game.OFF_SET, self.game.BLOCK_SIZE-6*self.game.OFF_SET, self.game.BLOCK_SIZE-6*self.game.OFF_SET)])
            self.display_board.append(row)
        
    def generate_projection(self):
        depth = 0
        while (self.game.check_move(self.game.piece.x, self.game.piece.y+depth) == 0):
            depth += 1
        depth -= 1
        for i in range(0, len(self.game.piece.type[self.game.piece.rotation])):
            for j in range(0, len(self.game.piece.type[self.game.piece.rotation][i])):
                if i+self.game.piece.y+depth < self.game.HEIGHT+2 and j+self.game.piece.x < self.game.WIDTH and j+self.game.piece.x >= 0:
                    if self.game.visual_board[i+self.game.piece.y+depth][j+self.game.piece.x] == 0 and self.game.piece.type[self.game.piece.rotation][i][j] != 0:
                        self.game.visual_board[i+self.game.piece.y+depth][j+self.game.piece.x] = -1

    def update_display(self):
        self.screen.fill(self.BLACK)

        #Display Group Number
        my_font = pygame.font.SysFont('Roboto', 30)
        text = my_font.render("GROUP 9", True, self.YELLOW)
        self.screen.blit(text, (850,950))

        #Display Game Settings
        pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(50, 150, 200, 100))
        pygame.draw.rect(self.screen, self.DARK_GREY, pygame.Rect(54, 154, 192, 92))
        pygame.draw.rect(self.screen, self.GREY, pygame.Rect(58, 158, 184, 84))
        my_font = pygame.font.SysFont('Roboto', 30)
            #game type
        if self.game.game_type == 0:
            text = my_font.render("Normal Game", True, self.WHITE)
        else:
            text = my_font.render("Extended Game", True, self.WHITE)
        self.screen.blit(text, (75, 170))
            #game mode
        if self.game.game_mode == 0:
            text = my_font.render("Player Mode", True, self.WHITE)
        else:
            text = my_font.render("AI Mode", True, self.WHITE)
        self.screen.blit(text, (75,205))

        #Display Game Stats
        pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(50, 350, 200, 300))
        pygame.draw.rect(self.screen, self.DARK_GREY, pygame.Rect(54, 354, 192, 292))
        pygame.draw.rect(self.screen, self.GREY, pygame.Rect(58, 358, 184, 284))
        stat_font = pygame.font.SysFont('Roboto', 40)
        number_font = pygame.font.SysFont('Roboto Thin', 30, False, True)
            #score
        text = stat_font.render("SCORE", True, self.WHITE)
        self.screen.blit(text, (100, 380))
        pygame.draw.rect(self.screen, self.DARK_GREY, pygame.Rect(80, 415, 140, 30))
        text = number_font.render("%d" %self.game.score, True, self.WHITE)
        self.screen.blit(text, (90, 420))
            #level
        text = stat_font.render("LEVEL", True, self.WHITE)
        self.screen.blit(text, (100, 470))
        pygame.draw.rect(self.screen, self.DARK_GREY, pygame.Rect(80, 505, 140, 30))
        text = number_font.render("%d" %self.game.level, True, self.WHITE)
        self.screen.blit(text, (90, 510))
            #lines
        text = stat_font.render("LINES", True, self.WHITE)
        self.screen.blit(text, (100, 560))
        pygame.draw.rect(self.screen, self.DARK_GREY, pygame.Rect(80, 595, 140, 30))
        text = number_font.render("%d" %self.game.lines, True, self.WHITE)
        self.screen.blit(text, (90, 600))
        
        #Display Next Piece
        pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(746, 146, 158, 158))
        pygame.draw.rect(self.screen, self.DARK_GREY, pygame.Rect(750, 150, 150, 150))
        pygame.draw.rect(self.screen, self.GREY, pygame.Rect(754, 154, 142, 142))
        pygame.draw.rect(self.screen, self.DARK_GREY, pygame.Rect(760, 195, 130, 90))
            #text
        my_font = pygame.font.SysFont('Roboto', 30)
        text = my_font.render("NEXT", True, self.WHITE)
        self.screen.blit(text, (800,165))
            #piece
        for i in range(0, len(self.game.next_piece.type[0])):
            for j in range(0, len(self.game.next_piece.type[0][i])):
                if self.game.next_piece.type[0][i][j] == 1:
                    if self.game.next_piece.type == pieces.O:
                        pygame.draw.rect(self.screen, self.game.next_piece.colour, pygame.Rect(765+30*j, 210+30*i, 28, 28))
                        pygame.draw.rect(self.screen, self.game.next_piece.second_colour, pygame.Rect(765+30*j+1, 210+30*i+1, 26, 26))
                    elif self.game.next_piece.type == pieces.I:
                        pygame.draw.rect(self.screen, self.game.next_piece.colour, pygame.Rect(765+30*j, 195+30*i, 28, 28))
                        pygame.draw.rect(self.screen, self.game.next_piece.second_colour, pygame.Rect(765+30*j+1, 195+30*i+1, 26, 26))
                    else:
                        pygame.draw.rect(self.screen, self.game.next_piece.colour, pygame.Rect(780+30*j, 210+30*i, 28, 28))
                        pygame.draw.rect(self.screen, self.game.next_piece.second_colour, pygame.Rect(780+30*j+1, 210+30*i+1, 26, 26))

        #Display Game Board
        pygame.draw.rect(self.screen, self.GREY, pygame.Rect(284, 84, self.game.BLOCK_SIZE*self.game.WIDTH+32, self.game.BLOCK_SIZE*self.game.HEIGHT+32))
        pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(288, 88, self.game.BLOCK_SIZE*self.game.WIDTH+24, self.game.BLOCK_SIZE*self.game.HEIGHT+24))
        pygame.draw.rect(self.screen, self.DARK_GREY, pygame.Rect(296, 96, self.game.BLOCK_SIZE*self.game.WIDTH+8, self.game.BLOCK_SIZE*self.game.HEIGHT+8))
        pygame.draw.rect(self.screen, self.GREY, pygame.Rect(300, 100,self.game. BLOCK_SIZE*self.game.WIDTH, self.game.BLOCK_SIZE*self.game.HEIGHT))
        self.generate_projection()
        for i in range(2, self.game.HEIGHT+2):
            for j in range(0, self.game.WIDTH):
                if self.game.visual_board[i][j] == -1:
                    pygame.draw.rect(self.screen, self.WHITE, self.display_board[i-2][j][1])
                    pygame.draw.rect(self.screen, self.GREY, self.display_board[i-2][j][2])
                elif self.game.visual_board[i][j] != 0:
                    pygame.draw.rect(self.screen, self.BLACK, self.display_board[i-2][j][0])
                    pygame.draw.rect(self.screen, pieces.colours[self.game.visual_board[i][j]-1], self.display_board[i-2][j][1])
                    pygame.draw.rect(self.screen, pieces.second_colours[self.game.visual_board[i][j]-1], self.display_board[i-2][j][2])

        pygame.display.update()

    def game_over(self):
        game_over = pygame.image.load('GamePage/assets/Game-Over.png')
        game_over = pygame.transform.scale(game_over, (400,250))
        self.screen.blit(game_over, (300, 200))
        pygame.display.update()

    def finish(self):
        #Display finish game dialog box
        pygame.draw.rect(self.screen, self.RED, pygame.Rect(245, 195, 510, 210))
        pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(250, 200, 500, 200))
        pygame.draw.rect(self.screen, self.DARK_GREY, pygame.Rect(254, 204, 492, 192))
        pygame.draw.rect(self.screen, self.GREY, pygame.Rect(258, 208, 484, 184))
        pygame.draw.rect(self.screen, self.RED, pygame.Rect(300, 280, 400, 10))
        #Display text
        my_font = pygame.font.SysFont('Roboto', 80)
        text = my_font.render("FINISH GAME?", True, self.RED)
        self.screen.blit(text, (300,230))
        #Display buttons
        my_font = pygame.font.SysFont('Roboto', 50)
        self.yes_button = Button("YES", (400, 340), my_font, self.WHITE)
        self.yes_button.update(self.screen)
        self.no_button = Button("NO", (600, 340), my_font, self.WHITE)
        self.no_button.update(self.screen)
        pygame.display.update()
