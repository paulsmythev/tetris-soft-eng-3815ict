# 3815ICT Software Engineering - Group Assignment - Trimester 2 2022

The purpose of this assignment is to construct and document a Requirements
Specification, Design, and Development Process for a classic computer game Tetris. You
should apply, as far as possible, the software engineering techniques introduced in this
course. You should employ an OO design and demonstrate capability to use advanced
design patterns and tactics in your project. The following problem statement is provided.
The assignment is to be conducted in groups with no more than four students in one
group

## Milestones
First Stage – Week 5 - 26/08/2022 (Midnight)

Second Stage – Week 9 - 23/09/2022 (Midnight)

Third Stage – Week 12 -  14/10/2022 (Midnight)

## Git
git clone https://github.com/paulsmythev/tetris-soft-eng-3815ict.git

git checkout -b ＜new-branch＞

## OG branches
RobertGame

configPage

hello_world

pauls-top-score

# Software Engineering (2805ICT & 3815ICT) Tetris Assignment

The following README will detail information on the Python files contained in the Tetris game project. It will provide the:

 - Names of each file
 - Purpose of the file (overview of its functionality)
 - Number of lines of code for the file
 - Total number of lines of code in the project
 - Naming conventions for classes, objects, functions and variables.

## Source Code Information
This Tetris game consisted of a total of **#** lines of code

A list of files and information used in this project are shown below.

### [File name]
**Length**: # lines
#### Description

### \_\_init__.py
**Length**: 0 lines
#### Description
A file that Python uses to indicate that the .py files in the folder are to be treated as a module for importing into other files.

### configure.py
**Length**: # lines
#### Description


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


