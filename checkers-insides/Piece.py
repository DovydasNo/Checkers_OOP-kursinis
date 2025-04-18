class Piece:
    def __init__(self, x, y, color):
        self.x = x   #columbs
        self.y = y   #rows
        self.color = color
        self.queen = False

    def make_queen(self):
        self.queen = True
