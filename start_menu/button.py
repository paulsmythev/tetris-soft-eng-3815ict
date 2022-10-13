# This class holds the variables and functions of buttons used to take input
class Button():
    # This is the class constructor
    def __init__(self, display_text, coor, font, colour):
        # Initialise button variables with given arguments
        # Coordinates
        self.x_coor = coor[0]
        self.y_coor = coor[1]
        # Text
        self.display_text = display_text
        # Colour
        self.colour = colour
        # Font
        self.font = font
        self.text = self.font.render(self.display_text, True, self.colour)
        self.text_rect = self.text.get_rect(center=(self.x_coor, self.y_coor))
        self.rect = self.text.get_rect(center=(self.x_coor, self.y_coor))
        
    # This class function updates the screen with the button
    def update(self, screen):
        screen.blit(self.text, self.text_rect)

    # This class function checks if mouse cursor is in the buttons bounds
    def check_input(self, coor):
        if coor[0] in range(self.rect.left, self.rect.right) and coor[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False