class Button():
    def __init__(self, display_text, coor, font, colour):
        # self.img = img
        self.display_text = display_text
        # rendering text
        self.font = font
        self.x_coor = coor[0]
        self.y_coor = coor[1]
        self.colour = colour
        self.text = self.font.render(self.display_text, True, self.colour)
        self.text_rect = self.text.get_rect(center=(self.x_coor, self.y_coor))
        # change colour on hover --> do it later
        # self.hover_colour = hover_colour

        # if no image is found
        # if self.img is None:
        #     self.img = self.display_text
        
    def update(self, screen):
        # print("update")
        screen.blit(self.text, self.text_rect)

    def checkInput(self, coordinate):
        print("check input")