import pygame
import time
import copy
from GamePage.game import Game
from GamePage.display import Display

class Controller:
    run = True
    sounds = True
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
        if self.game.check_move(self.game.piece.x-1, self.game.piece.y) == 0:
            if self.sounds:
                pygame.mixer.Sound.play(self.move_sound)
            self.game.piece.x -= 1
            self.game.visual_board = copy.deepcopy(self.game.board)
            self.game.add_piece(self.game.visual_board)
            self.display.update_display()

    def move_right(self):
        if self.game.check_move(self.game.piece.x+1, self.game.piece.y) == 0:
            if self.sounds:
                pygame.mixer.Sound.play(self.move_sound)
            self.game.piece.x += 1
            self.game.visual_board = copy.deepcopy(self.game.board)
            self.game.add_piece(self.game.visual_board)
            self.display.update_display()

    def move_down(self):
        if self.game.check_move(self.game.piece.x, self.game.piece.y+1) == 0:
            self.game.piece.y += 1
        else:
            if self.sounds:
                pygame.mixer.Sound.play(self.drop_sound)
            self.game.add_piece(self.game.board)
            self.game.generate_piece()
            self.check_lines()
            self.check_lose()
        self.game.visual_board = copy.deepcopy(self.game.board)
        self.game.add_piece(self.game.visual_board)
        self.display.update_display()
    
    def rotate(self):
        #Rotate the piece
        sound_effect = True
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
                sound_effect = False
        if self.sounds and sound_effect:
            pygame.mixer.Sound.play(self.rotate_sound)
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
            time.sleep(0.5)
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
        while self.game.level >= (self.game.tempo+1)*6:
            self.game.tempo += 1
        pygame.mixer.music.load(self.game.songs[self.game.tempo])
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play(-1, 0, 5000)

        clock = pygame.time.Clock()
        prev_time = time.time()
        while self.run:
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
                        if event.key == pygame.K_UP:
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
            
            # AI Moves
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
        pygame.mixer.music.stop()
