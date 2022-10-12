import pygame
import time
import copy
from game_page.game import Game, Piece
from game_page.display import Display
from top_score.top_score_check import TopScoreCheck

# Initialise pygame modules
pygame.init()

# This class holds the variables and functions of the game controller
class Controller:
    # Initialise controller variables
    # Game running boolean
    run = True
    # Game sounds boolean
    sounds = True
    # Need new ai move boolean
    need_ai = True
    # Game pause boolean
    game_pause = False
    # Initialise game sounds and volumes
    game_over_sound = pygame.mixer.Sound("assets/sounds/game_over.wav")
    game_over_sound.set_volume(0.25)
    drop_sound = pygame.mixer.Sound("assets/sounds/soft_drop.wav")
    drop_sound.set_volume(0.5)
    rotate_sound = pygame.mixer.Sound("assets/sounds/rotate.wav")
    rotate_sound.set_volume(0.5)
    move_sound = pygame.mixer.Sound("assets/sounds/move.wav")
    move_sound.set_volume(0.5)
    single_sound = pygame.mixer.Sound("assets/sounds/single.wav")
    single_sound.set_volume(0.5)
    double_sound = pygame.mixer.Sound("assets/sounds/double.wav")
    double_sound.set_volume(0.5)
    triple_sound = pygame.mixer.Sound("assets/sounds/triple.wav")
    triple_sound.set_volume(0.5)
    tetris_sound = pygame.mixer.Sound("assets/sounds/tetris.wav")
    tetris_sound.set_volume(0.5)

    # This is the class contructor
    def __init__(self, settings):
        # Initialise game class that stores the game data
        self.game = Game(settings.game_size, settings.start_level, settings.game_type, settings.game_mode)
        # Initialise display class that handles the game display
        self.display = Display(self.game)

    # This class function tries to move the current piece to the left
    def move_left(self):
        # If move is possible
        if self.game.check_move(self.game.piece.x-1, self.game.piece.y, self.game.piece.rotation) == 0:
            # Play move sound if game sound is on
            if self.sounds:
                pygame.mixer.Sound.play(self.move_sound)
            # Move piece left
            self.game.piece.x -= 1
            # Update display
            self.game.visual_board = copy.deepcopy(self.game.board)
            self.game.add_piece(self.game.visual_board, self.game.piece)
            self.display.update_display()
    
    # This class function tries to move the current piece to the right
    def move_right(self):
        # If move is possible
        if self.game.check_move(self.game.piece.x+1, self.game.piece.y, self.game.piece.rotation) == 0:
            # Play move sound if game sound is on
            if self.sounds:
                pygame.mixer.Sound.play(self.move_sound)
            # Move piece right
            self.game.piece.x += 1
            # Update display
            self.game.visual_board = copy.deepcopy(self.game.board)
            self.game.add_piece(self.game.visual_board, self.game.piece)
            self.display.update_display()

    # This class function tries to move the current piece down and checks if it has collided with the stack
    def move_down(self):
        # If move is possible
        if self.game.check_move(self.game.piece.x, self.game.piece.y+1, self.game.piece.rotation) == 0:
            # Move piece down
            self.game.piece.y += 1
        # If move is not possible
        else:
            # Play drop sound if game sound is on
            if self.sounds:
                pygame.mixer.Sound.play(self.drop_sound)
            # Set ai move boolean to true
            self.need_ai = True
            # Add piece to bottom stack
            self.game.add_piece(self.game.board, self.game.piece)
            # Generate a new piece
            self.game.generate_piece()
            # Check for lines that need clearing
            self.check_lines()
            # Check if the user has lost
            if self.check_lose():
                return
        # Update display
        self.game.visual_board = copy.deepcopy(self.game.board)
        self.game.add_piece(self.game.visual_board, self.game.piece)
        self.display.update_display()
    
    # This class function tries to rotate the current piece clockwise 90 degrees
    def rotate(self):
        # Change to next rotation state (0-3)
        if self.game.piece.rotation == 3:
            self.game.piece.rotation = 0
        else:
            self.game.piece.rotation += 1
        # If the rotation is not possible check for adjacent spaces that it can fit in
        if self.game.check_move(self.game.piece.x, self.game.piece.y, self.game.piece.rotation) != 0:
            # Try different adjacent spaces
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
            # If no spaces then undo the rotation
            else:
                if self.game.piece.rotation == 0:
                    self.game.piece.rotation = 3
                else:
                    self.game.piece.rotation -= 1
                return
        # Play rotation sound if game sound is on
        if self.sounds:
            pygame.mixer.Sound.play(self.rotate_sound)
        # Update display
        self.game.visual_board = copy.deepcopy(self.game.board)
        self.game.add_piece(self.game.visual_board, self.game.piece)
        self.display.update_display()

    # This class fuction checks the board for lines that need to be cleared
    def check_lines(self):
        # List for full lines
        full_lines = []
        # Check the board for full rows
        for i in range(2, len(self.game.board)):
            # If full add row to list of full rows and increase the score
            if 0 not in self.game.board[i]:
                full_lines.append(i)
                self.game.score += 100 * len(full_lines)
        # Play line clear sounds if game sound is on
        if self.sounds:
            # Single clear sound
            if len(full_lines) == 1:
                pygame.mixer.Sound.play(self.single_sound)
            # Double clear sound
            if len(full_lines) == 2:
                pygame.mixer.Sound.play(self.double_sound)
            # Tripple clear sound
            if len(full_lines) == 3:
                pygame.mixer.Sound.play(self.triple_sound)
            # Tetris clear sound
            if len(full_lines) == 4:
                pygame.mixer.Sound.play(self.tetris_sound)
        # Change full lines to ghost lines
        for i in full_lines:
            self.game.visual_board[i] = [-1]*self.game.WIDTH
        # Update display and delay to show ghost lines
        if len(full_lines) > 0:
            self.display.update_display()
            time.sleep(0.2)
        # Pop rows from board and add empty rows to top
        for i in full_lines:
            self.game.board.pop(i)
            self.game.board.insert(2, [0]*self.game.WIDTH)
        # Increase lines cleared
        self.game.lines += len(full_lines)
        if self.game.lines-self.game.prev_lines >= (self.game.level+1) * 10:
            # Increase level is needed
            self.game.level += 1
            self.game.prev_lines += self.game.level*10
            # Change tetris theme tempo if needed
            if self.sounds:
                if self.game.level >= (self.game.tempo+1)*5:
                    self.game.tempo += 1
                    pygame.mixer.music.stop()
                    print("next song")
                    pygame.mixer.music.load(self.game.songs[self.game.tempo])
                    pygame.mixer.music.play(-1)

    # This class function checks if the user has lost
    def check_lose(self):
        # Check the row above the displayed board for blocks
        for i in self.game.board[1]:
            # If there is a block out of bounds
            if i != 0:
                # Play game over sound if game sound is on
                if self.sounds:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(self.game_over_sound)
                # Display game over
                self.display.game_over()
                # Wait 3 seconds then exit game or exit on demand
                start = time.time()
                while self.run:
                    if time.time()-start > 3:
                        self.run = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.run = False
                # Check if the score is a new high score
                self.save_score()
                return True
        return False
                
    # This class function controls the pop up menu to leave the game
    def finish_game(self):
        # Display finish game menu
        self.display.finish()
        # Wait for input from user
        check = True
        while self.run and check:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Check for new events
            for event in pygame.event.get():
                # Close window event
                if event.type == pygame.QUIT:
                    self.run = False
                # Check buttons if mouse is clicked
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Yes button
                    if self.display.yes_button.check_input(mouse_pos):
                        # Leave game
                        self.run = False
                        self.save_score()
                    # No button
                    if self.display.no_button.check_input(mouse_pos):
                        # Return to score
                        self.display.update_display()
                        if self.game_pause:
                            self.display.pause()
                        check = False
                        break

    # This class funtion uses the top score check class to check if the score is a new high score
    def save_score(self):
        top_score = TopScoreCheck()
        # Send score and human boolean if human playing
        if self.game.game_type == 0:
            top_score.run_new_score(self.game.score, False)
        # Send score and ai boolean if ai playing
        else:
            top_score.run_new_score(self.game.score, True)

    # This class function finds the best move based on the current game state
    def best_move(self, board, piece):
        # Initialise a duplicate piece for testing positions
        test_piece = Piece(0, 0, self.game.game_mode)
        test_piece.type = piece.type
        # Initialise a list that holds the score, column and rotation of the best move
        best_move = [-100,0,0]
        # For every possible rotation
        for rotation in range(0, 4):
            test_piece.rotation = rotation
            test_piece.x = 0
            # Move piece as far left as possible
            while self.game.check_move(test_piece.x-1, test_piece.y, test_piece.rotation) == 0:
                test_piece.x -= 1
            # Move piece as far right as possible
            while self.game.check_move(test_piece.x, test_piece.y, test_piece.rotation) == 0:
                # Make a duplicate of the board for testing
                temp_board = copy.deepcopy(board)
                # Move down until it collides
                while self.game.check_move(test_piece.x, test_piece.y+1, test_piece.rotation) == 0:
                    test_piece.y += 1
                # Add the test piece to the test board
                self.game.add_piece(temp_board, test_piece)
                # Find the bottom level of the piece
                bottom = 0
                for i in range(0, len(test_piece.type[rotation])):
                    if 1 in test_piece.type[rotation][i]:
                        bottom = i
                # Calculate the score of this possible moves using the new board state and the pieces final depth
                score = self.analyse_board(temp_board, test_piece.y+bottom)
                # If this move is better than make it the new best move
                if score > best_move[0]:
                    best_move[0] = score
                    best_move[1] = rotation
                    best_move[2] = test_piece.x
                # Reset piece depth and move right to the next column
                test_piece.y = 0
                test_piece.x += 1
        # Return the column and rotation of the best move
        return best_move[1], best_move[2]

    # This class function produces and returns a score based on how desirable a game board state is
    def analyse_board(self, board, depth):
        # Add the piece depth to the score
        score = depth
        # Reduce the score by 2 for each empty slot with a full slot somewhere ebove it
        for row in range (0, len(board)):
            for column in range(0, len(board[row])):
                if board[row][column] == 0:
                    above = row
                    while above >= 0:
                        if board[above][column] != 0:
                            score -= 2
                            break
                        above -= 1
        # Reduce the score by 1 for every 3 or more deep cavern on the far left
        gap_size = 0
        for row in range(len(board)-1, 0, -1):
            if board[row][0] != 0 or board[row][1] == 0:
                gap_size = 0
            if board[row][0] == 0 and board[row][1] != 0:
                gap_size += 1
            if gap_size >= 3:
                score -= 1

        # Reduce the score by 1 for every 3 or more deep cavern on the far right
        gap_size = 0
        for row in range(len(board)-1, 0, -1):
            if board[row][len(board[row])-1] != 0 or board[row][len(board[row])-2] == 0:
                gap_size = 0
            if board[row][len(board[row])-1] == 0 and board[row][len(board[row])-2] != 0:
                gap_size += 1
            if gap_size >= 3:
                score -= 1
        
        # Reduce the score by 1 for every 3 or more deep cavern in all othe columns
        for column in range(1, len(board[0])-1):
            gap_size = 0
            for row in range(len(board)-1, 0, -1):
                if board[row][column] != 0 or board[row][column-1] == 0 or board[row][column+1] == 0:
                    gap_size = 0
                if board[row][column] == 0 and board[row][column-1] != 0 and board[row][column+1] != 0:
                    gap_size += 1
                if gap_size >= 3:
                    score -= 1
        
        # Return the calculated score
        return score

    # This class function runs the control loop for the game
    def run_game(self):
        # Set the game theme tempo to the correct level
        while self.game.level >= (self.game.tempo+1)*6:
            self.game.tempo += 1
        # Load and initialise game sounds
        pygame.mixer.music.load(self.game.songs[self.game.tempo])
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play(-1, 0, 5000)
        # Initialise the game clock
        clock = pygame.time.Clock()
        prev_time = time.time()
        while self.run:
            # Drop the block based on the speed algorithm if the game is not paused
            if not self.game_pause:
                #Move down every second
                clock.tick(12)
                curr_time = time.time()
                if curr_time - prev_time >= self.game.speeds[min(29, self.game.level)]/60:
                    prev_time = curr_time
                    self.move_down()

            # If game is in human player mode
            if self.game.game_type == 0:
                # Boolean for a brief pause after first move when holding input arrows
                pause = False
                # Check for new events
                for event in pygame.event.get():
                    # Close window event
                    if event.type == pygame.QUIT:
                        self.run = False
                    # If a key has been pressed
                    if event.type == pygame.KEYDOWN:
                        # Rotate piece if up key
                        if event.key == pygame.K_UP and not self.game_pause:
                            self.rotate()
                        # Display finish pop up menu if escape key
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.stop()
                            self.finish_game()
                            if not self.game_pause and self.sounds:
                                pygame.mixer.music.play(-1, 0, 5000)
                        # Activate input pause if moving right or left
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                            pause = True
                        # Toggle game sounds if m key
                        if event.key == pygame.K_m:
                            if self.sounds == True:
                                self.sounds = False
                                pygame.mixer.music.stop()
                            else:
                                self.sounds = True
                                pygame.mixer.music.play(-1, 0, 5000)
                        # Toggle game pause if p key
                        if event.key == pygame.K_p:
                            if self.game_pause == False:
                                self.game_pause = True
                                pygame.mixer.music.stop()
                                self.display.pause()
                            else:
                                self.game_pause = False
                                if self.sounds:
                                    pygame.mixer.music.play(-1, 0, 5000)
                # Skip the following code if game is paused
                if self.game_pause:
                    continue
                # Check for keys being held down
                keys = pygame.key.get_pressed()
                # Move left if left key
                if keys[pygame.K_LEFT]:
                    self.move_left()
                    if pause:
                        time.sleep(0.1)
                        pause = False
                # Move right if right key
                if keys[pygame.K_RIGHT]:
                    self.move_right()
                    if pause:
                        time.sleep(0.1)
                        pause = False
                # Move down if down key
                if keys[pygame.K_DOWN]:
                    self.move_down()
            
            # If game is in AI player mode
            else:
                # Check for new human input events
                for event in pygame.event.get():
                    # Close window event
                    if event.type == pygame.QUIT:
                        self.run = False
                    # If a key has been pressed 
                    if event.type == pygame.KEYDOWN:
                        # Display finish pop up menu if escape key
                        if event.key == pygame.K_ESCAPE:
                            pygame.mixer.music.stop()
                            self.finish_game()
                            if not self.game_pause and self.sounds:
                                pygame.mixer.music.play(-1, 0, 5000)
                        # Toggle game sounds if m key
                        if event.key == pygame.K_m:
                            if self.sounds == True:
                                self.sounds = False
                                pygame.mixer.music.stop()
                            else:
                                self.sounds = True
                                pygame.mixer.music.play(-1, 0, 5000)
                        # Toggle game pause if p key
                        if event.key == pygame.K_p:
                            if self.game_pause == False:
                                self.game_pause = True
                                pygame.mixer.music.stop()
                                self.display.pause()
                            else:
                                self.game_pause = False
                                if self.sounds:
                                    pygame.mixer.music.play(-1, 0, 5000)
                # If not paused then make AI moves
                if not self.game_pause:
                    # If an AI move is needed find the best move
                    if self.need_ai:
                        rotation, column = self.best_move(self.game.board, self.game.piece)
                        self.need_ai = False
                    # Rotate piece until in wanted position
                    if self.game.piece.rotation != rotation:
                        self.rotate()
                    # Move left if piece is right of wanted position
                    elif column < self.game.piece.x:
                        self.move_left()
                    # Move right if piece is left of wanted position
                    elif column > self.game.piece.x:
                        self.move_right()
                    # If piece is in wanted position then move down
                    else:
                        self.move_down()

        # Stop music when terminating game
        pygame.mixer.music.stop()
