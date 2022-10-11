import pygame
import time
import copy

from GamePage.game import Game, Piece
from GamePage.display import Display
from top_score.top_score_check import TopScoreCheck

class Controller:
    run = True
    sounds = True
    need_ai = True
    game_pause = False
    game_over_sound = pygame.mixer.Sound("GamePage/assets/Game_Over.wav")
    game_over_sound.set_volume(0.25)
    drop_sound = pygame.mixer.Sound("GamePage/assets/Soft_Drop.wav")
    drop_sound.set_volume(0.5)
    rotate_sound = pygame.mixer.Sound("GamePage/assets/Rotate.wav")
    rotate_sound.set_volume(0.5)
    move_sound = pygame.mixer.Sound("GamePage/assets/Move.wav")
    move_sound.set_volume(0.5)
    single_sound = pygame.mixer.Sound("GamePage/assets/Single.wav")
    single_sound.set_volume(0.5)
    double_sound = pygame.mixer.Sound("GamePage/assets/Double.wav")
    double_sound.set_volume(0.5)
    triple_sound = pygame.mixer.Sound("GamePage/assets/Triple.wav")
    triple_sound.set_volume(0.5)
    tetris_sound = pygame.mixer.Sound("GamePage/assets/Tetris.wav")
    tetris_sound.set_volume(0.5)

    def __init__(self, settings):
        self.game = Game(settings.game_size, settings.start_level, settings.game_type, settings.game_mode)
        self.display = Display(self.game)

    def move_left(self):
        if self.game.check_move(self.game.piece.x-1, self.game.piece.y, self.game.piece.rotation) == 0:
            if self.sounds:
                pygame.mixer.Sound.play(self.move_sound)
            self.game.piece.x -= 1
            self.game.visual_board = copy.deepcopy(self.game.board)
            self.game.add_piece(self.game.visual_board, self.game.piece)
            self.display.update_display()

    def move_right(self):
        if self.game.check_move(self.game.piece.x+1, self.game.piece.y, self.game.piece.rotation) == 0:
            if self.sounds:
                pygame.mixer.Sound.play(self.move_sound)
            self.game.piece.x += 1
            self.game.visual_board = copy.deepcopy(self.game.board)
            self.game.add_piece(self.game.visual_board, self.game.piece)
            self.display.update_display()

    def move_down(self):
        if self.game.check_move(self.game.piece.x, self.game.piece.y+1, self.game.piece.rotation) == 0:
            self.game.piece.y += 1
        else:
            if self.sounds:
                pygame.mixer.Sound.play(self.drop_sound)
            self.need_ai = True
            self.game.add_piece(self.game.board, self.game.piece)
            self.game.generate_piece()
            self.check_lines()
            self.check_lose()
        self.game.visual_board = copy.deepcopy(self.game.board)
        self.game.add_piece(self.game.visual_board, self.game.piece)
        self.display.update_display()
    
    def rotate(self):
        #Rotate the piece
        sound_effect = True
        if self.game.piece.rotation == 3:
            self.game.piece.rotation = 0
        else:
            self.game.piece.rotation += 1
        #Check nearby for valid rotation space
        if self.game.check_move(self.game.piece.x, self.game.piece.y, self.game.piece.rotation) != 0:
            if self.game.check_move(self.game.piece.x+1, self.game.piece.y, self.game.piece.rotation) == 0:
                self.game.piece.x += 1
            elif self.game.check_move(self.game.piece.x-1, self.game.piece.y, self.game.piece.rotation) == 0:
                self.game.piece.x -= 1
            elif self.game.check_move(self.game.piece.x, self.game.piece.y-1, self.game.piece.rotation) == 0:
                self.game.piece.y -= 1
            elif self.game.check_move(self.game.piece.x+2, self.game.piece.y, self.game.piece.rotation) == 0:
                self.game.piece.x += 2
            elif self.game.check_move(self.game.piece.x-2, self.game.piece.y, self.game.piece.rotation) == 0:
                self.game.piece.x -= 2
            else:
                self.game.piece.rotation -= 1
                sound_effect = False
        if self.sounds and sound_effect:
            pygame.mixer.Sound.play(self.rotate_sound)
        self.game.visual_board = copy.deepcopy(self.game.board)
        self.game.add_piece(self.game.visual_board, self.game.piece)
        self.display.update_display()

    def check_lines(self):
        full_lines = []
        for i in range(2, len(self.game.board)):
            if 0 not in self.game.board[i]:
                full_lines.append(i)
                #Increase score
                self.game.score += 100 * len(full_lines)
        if self.sounds:
            if len(full_lines) == 1:
                pygame.mixer.Sound.play(self.single_sound)
            if len(full_lines) == 2:
                pygame.mixer.Sound.play(self.double_sound)
            if len(full_lines) == 3:
                pygame.mixer.Sound.play(self.triple_sound)
            if len(full_lines) == 4:
                pygame.mixer.Sound.play(self.tetris_sound)
        for i in full_lines:
            self.game.visual_board[i] = [-1]*self.game.WIDTH
        if len(full_lines) > 0:
            self.display.update_display()
            time.sleep(0.2)
        for i in full_lines:
            self.game.board.pop(i)
            self.game.board.insert(2, [0]*self.game.WIDTH)
        #Increase lines cleared
        self.game.lines += len(full_lines)
        if self.game.lines-self.game.prev_lines >= (self.game.level+1) * 10:
            #Increase level
            self.game.level += 1
            self.game.prev_lines += self.game.level*10
            if self.sounds:
                if self.game.level >= (self.game.tempo+1)*5:
                    self.game.tempo += 1
                    pygame.mixer.music.stop()
                    print("next song")
                    pygame.mixer.music.load(self.game.songs[self.game.tempo])
                    pygame.mixer.music.play(-1)

    def check_lose(self):
        for i in self.game.board[1]:
            if i != 0:
                #Display Game Over
                if self.sounds:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(self.game_over_sound)
                self.display.game_over()
                start = time.time()
                while self.run:
                    if time.time()-start > 3:
                        self.run = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.run = False
                self.save_score()
                break
                

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
                        self.save_score()
                    if self.display.no_button.check_input(mouse_pos):
                        self.display.update_display()
                        if self.game_pause:
                            self.display.pause()
                        check = False

    def save_score(self):
        top_score = TopScoreCheck()
        if self.game.game_type == 0:
            top_score.screen(self.game.score, False)
        else:
            top_score.screen(self.game.score, True)

    def best_move(self, board, piece):
        total = 0
        test_piece = Piece(0, 0, self.game.game_mode)
        test_piece.type = piece.type
        best_move = [-100,0,0]
        for rotation in range(0, 4):
            test_piece.rotation = rotation
            test_piece.x = 0
            while self.game.check_move(test_piece.x-1, test_piece.y, test_piece.rotation) == 0:
                test_piece.x -= 1
            while self.game.check_move(test_piece.x, test_piece.y, test_piece.rotation) == 0:
                temp_board = copy.deepcopy(board)
                while self.game.check_move(test_piece.x, test_piece.y+1, test_piece.rotation) == 0:
                    test_piece.y += 1
                self.game.add_piece(temp_board, test_piece)
                bottom = 0
                for i in range(0, len(test_piece.type[rotation])):
                    if 1 in test_piece.type[rotation][i]:
                        bottom = i
                score = self.analyse_board(temp_board, test_piece.y+bottom)
                total += 1
                if score > best_move[0]:
                    best_move[0] = score
                    best_move[1] = rotation
                    best_move[2] = test_piece.x
                test_piece.y = 0
                test_piece.x += 1
        return best_move[1], best_move[2]

    def analyse_board(self, board, depth):
        score = depth
        for row in range (0, len(board)):
            for column in range(0, len(board[row])):
                if board[row][column] == 0:
                    above = row
                    while above >= 0:
                        if board[above][column] != 0:
                            score -= 2
                            break
                        above -= 1
        gap_size = 0
        for row in range(len(board)-1, 0, -1):
            if board[row][0] != 0 or board[row][1] == 0:
                gap_size = 0
            if board[row][0] == 0 and board[row][1] != 0:
                gap_size += 1
            if gap_size >= 3:
                score -= 1

        gap_size = 0
        for row in range(len(board)-1, 0, -1):
            if board[row][len(board[row])-1] != 0 or board[row][len(board[row])-2] == 0:
                gap_size = 0
            if board[row][len(board[row])-1] == 0 and board[row][len(board[row])-2] != 0:
                gap_size += 1
            if gap_size >= 3:
                score -= 1
        
        for column in range(1, len(board[0])-1):
            gap_size = 0
            for row in range(len(board)-1, 0, -1):
                if board[row][column] != 0 or board[row][column-1] == 0 or board[row][column+1] == 0:
                    gap_size = 0
                if board[row][column] == 0 and board[row][column-1] != 0 and board[row][column+1] != 0:
                    gap_size += 1
                if gap_size >= 3:
                    score -= 1
        
        return score

    def run_game(self):
        while self.game.level >= (self.game.tempo+1)*6:
            self.game.tempo += 1
        pygame.mixer.music.load(self.game.songs[self.game.tempo])
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play(-1, 0, 5000)

        clock = pygame.time.Clock()
        prev_time = time.time()
        while self.run:
            if not self.game_pause:
                #Move down every second
                clock.tick(12)
                curr_time = time.time()
                if curr_time - prev_time >= self.game.speeds[min(29, self.game.level)]/60:
                    prev_time = curr_time
                    self.move_down()

            # Human Moves
            if self.game.game_type == 0:
                pause = False
                #Check for inputs
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                    if event.type == pygame.KEYDOWN:
                        #Rotate if up key
                        if event.key == pygame.K_UP and not self.game_pause:
                            self.rotate()
                        #Finish game dialog box in escape
                        if event.key == pygame.K_ESCAPE:
                            self.finish_game()
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                            pause = True
                        if event.key == pygame.K_m:
                            if self.sounds == True:
                                self.sounds = False
                                pygame.mixer.music.stop()
                            else:
                                self.sounds = True
                                pygame.mixer.music.play(-1, 0, 5000)
                        if event.key == pygame.K_p:
                            if self.game_pause == False:
                                self.game_pause = True
                                pygame.mixer.music.stop()
                                self.display.pause()
                            else:
                                self.game_pause = False
                                pygame.mixer.music.play(-1, 0, 5000)
                                
                if self.game_pause:
                    continue

                #Check for keys being held down
                keys = pygame.key.get_pressed()
                #Move left if left key
                if keys[pygame.K_LEFT]:
                    self.move_left()
                    if pause:
                        time.sleep(0.1)
                        pause = False
                #Move right if right key
                if keys[pygame.K_RIGHT]:
                    self.move_right()
                    if pause:
                        time.sleep(0.1)
                        pause = False
                #Move down if down key
                if keys[pygame.K_DOWN]:
                    self.move_down()
                    if (not self.run):
                        break
            
            # AI Moves
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                    if event.type == pygame.KEYDOWN:
                        #Finish game dialog box in escape
                        if event.key == pygame.K_ESCAPE:
                            self.finish_game()
                        if event.key == pygame.K_m:
                            if self.sounds == True:
                                self.sounds = False
                                pygame.mixer.music.stop()
                            else:
                                self.sounds = True
                                pygame.mixer.music.play(-1, 0, 5000)
                
                # Function that returns best place to move to
                if self.need_ai:
                    rotation, column = self.best_move(self.game.board, self.game.piece)
                    self.need_ai = False
                if self.game.piece.rotation != rotation:
                    self.rotate()
                elif column < self.game.piece.x:
                    self.move_left()
                elif column > self.game.piece.x:
                    self.move_right()
                else:
                    self.move_down()

        pygame.mixer.music.stop()
