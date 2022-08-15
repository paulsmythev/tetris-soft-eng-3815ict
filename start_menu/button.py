class Button():
    def __init__(self, img, coor, font, display_text, colour):
        self.img = img
        self.x_coor = coor[0]
        self.y_coor = coor[1]
        self.font = font
        self.colour = colour
        # change colour on hover --> do it later
        # self.hover_colour = hover_colour
        self.display_text = display_text
        # rendering text
        self.text = self.font.render(self.display_text, True, self.colour)
        # if no image is found
        if self.img is None:
            self.img = self.display_text
        
        def update(self, screen):
            print("update")

        def checkInput(self, coordinate):
            print("check input")