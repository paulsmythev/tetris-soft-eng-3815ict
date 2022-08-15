class Button():
    def __init__(self, img, coor, font, display_text, colour, hover_colour):
        self.img = img
        self.x_coor = coor[0]
        self.y_coor = coor[1]
        self.font = font
        self.colour = colour
        self.hover_colour = hover_colour
        self.display_text = display_text
        # rendering text
        self.text = self.font.render(self.display_text, True, self.colour)