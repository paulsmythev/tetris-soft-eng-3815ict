# Software Engineering (2805ICT & 3815ICT) Tetris Assignment

The following README will detail information on the Python files contained in the Tetris game project. It will provide the:

 - Names of each file
 - Purpose of the file (overview of its functionality)
 - Number of lines of code for the file
 - Total number of lines of code in the project
 - Naming conventions for classes, objects, functions and variables.

## Source Code Information

This Tetris game consisted of a total of **1170** lines of code

A list of files and information used in this project are shown below.

### `main.py`
**Length**: 109 lines
#### Description
This is the main entry point into the application and all classes and modules are accessed through this file's MainMenu class. It contains all the code for running, displaying and storing data relating to the main menu. It contains buttons that direct the user to other parts of the program.

### `__init__.py`
**Length**: 0 lines
#### Description
A file that Python uses to indicate that the .py files in the folder are to be treated as a module for importing into other files.

### ***start_menu------------------***
### `button.py`
**Length**: 26 lines
#### Description
Contains the class for a Button, the variables that are required to pass in to create a button, as well as methods to update the button (if needed in the future) and for checking user input using the mouse position.

### ***configure_page--------------***
### `configure.py`
**Length**: 124 lines
#### Description
This file has all the code that is relating to the configuration menu that is accessed from the main menu. The file contains code for blitting object to screen, handling user input and initialising variables. 
WIP - There is an interface set up for other functionality such as changing field size, difficulty and the game type (Extended, AI or Player).

### ***GamePage------------------***
### `controller.py`
**Length**: 137 lines
#### Description
This file contains the code for the controller component of the MVC Game architecture. The code is responsible for processing user input (movement of the block, quitting the game), checking scoring and lose conditions, as well as running the main game loop.

### `display.py`
**Length**: 140 lines
#### Description
This file contains code for displaying the graphical user interface (GUI) to the user and inititialising the playing board (game field). This code also has a method for updating the display, this method gets called when the controller updates the model and redraws the screen with the updated information from the model. It also contains methods for drawing a game over screen and drawing a finish screen where the user chooses whether to continue or return back to main menu

### `game.py`
**Length**: 96 lines
#### Description
This file is used for storing and checking information about the game, instantiating tetris blocks from the Pieces class and manipulating the board's state. This class has methods for generating and adding Tetris blocks to the game field, finding the position of the current block and checking for collision.

### `pieces.py`
**Length**: 147 lines
#### Description
This file contains the "shapes" and rotation configurations of each playing block shown in a bit array. 

### ***top_score--------------------***
### `file_handler.py`
**Length**: 28 lines
#### Description
This class is used for handling reading and writing to the top scores file

### `top_score_check.py`
**Length**: 193 lines
#### Description
This page reads top-scores.json and checks to see if your score is within the top 10. If it is it will prompt you to enter your name and write your score back to the file.

### `top_score_screen.py`
**Length**: 127 lines
#### Description
This file contains the code for drawing the top score screen, as well as loading the top 10 scores from top-scores.json

### `top-scores.json`
**Length**: 43 lines
#### Description
This file holds the seeded top scores for the application. The scores are stored in key-value pairs with JSON formatting.

## Naming Conventions
Naming conventions were a reflection of standard Python naming conventions and the project team adhered to these conventions to the best of their ability. The naming conventions were taken from the [Python documentation](https://peps.python.org/pep-0008/).

### Classes
Classes were named with the `CapitilisedWords` convention.
An example from the code would be the Button class, as follows:
```
	class Button():
		def __init__(self, display_text, coor, font, colour):
			...
```

### Objects
An object, such as an instance of a class was assigned using the `lower_case_with_underscores` convention. An example from the code would be the assigning of a button using the Button class, as follows:
```
	play_button = Button("PLAY!", (SCREEN_WIDTH/2, SCREEN_HEIGHT*0.40), my_font(200), CREAM)
```

### Functions
Functions were declared using the`lower_case_with_underscores` convention. An example for the code would be the `write_lines()` function, as follows:
```
	def write_lines(surface, text, font, colour, x_coor, y_coor):
		...
```

### Variables
Variables were declared using the`lower_case_with_underscores` convention. An example of this would be getting the mouse position (coordinates) on screen, as follows:
```
	mouse_pos = pygame.mouse.get_pos()
```

#### Constants
Constants were declared using the`UPPER_CASE_WITH_UNDERSCORES` convention. An example of this would be the screen dimensions for the game window, as follows:
```
	SCREEN_WIDTH = 1000
```
