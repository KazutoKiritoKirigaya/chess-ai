
class Square:
    def __init__(self, row, col, piece=None): # Optional parameter piece - Not all squares are going to have a chess piece on it.
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece != None