import pygame
import copy
from GamePage.game import Game
from GamePage.display import Display

class Controller:
    run = True

    def __init__(self, size, level, game_type, game_mode):
        self.game = Game(size, level, game_type, game_mode)
        self.display = Display(self.game)

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
        #Check nearby for valid rotation space
        if self.game.check_move(self.game.piece.x, self.game.piece.y) != 0:
            if self.game.check_move(self.game.piece.x+1, self.game.piece.y) == 0:
                self.game.piece.x += 1
            elif self.game.check_move(self.game.piece.x-1, self.game.piece.y) == 0:
                self.game.piece.x -= 1
            elif self.game.check_move(self.game.piece.x, self.game.piece.y-1) == 0:
                self.game.piece.y -= 1
            elif self.game.check_move(self.game.piece.x+2, self.game.piece.y) == 0:
                self.game.piece.x += 2
            elif self.game.check_move(self.game.piece.x-2, self.game.piece.y) == 0:
                self.game.piece.x -= 2
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
        for i in self.game.board[1]:
            if i != 0:
                #Display Game Over
                self.display.game_over()
                while self.run:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.run = False

    def finish_game(self):
        #Display finish game menu
        self.display.finish()
        #Wait for input
        check = True
        while self.run and check:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.display.yes_button.check_input(mouse_pos):
                        self.run = False
                    if self.display.no_button.check_input(mouse_pos):
                        check = False

    def run_game(self):
        clock = pygame.time.Clock()
        prev_time = pygame.time.get_ticks()
        while self.run:
            #Move down every second
            clock.tick(12)
            time = pygame.time.get_ticks()
            if time - prev_time >= 1000:
                prev_time = time
                self.move_down()
            #Check for inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    #Rotate if up key
                    if event.key == pygame.K_UP:
                        self.rotate()
                    #Finish game dialog box in escape
                    if event.key == pygame.K_ESCAPE:
                        self.finish_game()
                
            #Check for keys being held down
            keys = pygame.key.get_pressed()
            #Move left if left key
            if keys[pygame.K_LEFT]:
                self.move_left()
            #Move right if right key
            if keys[pygame.K_RIGHT]:
                self.move_right()
            #Move down if down key
            if keys[pygame.K_DOWN]:
                self.move_down()
