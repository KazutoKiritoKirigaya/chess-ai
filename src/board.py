"""
The provided code defines a Board class, which represents a chessboard. 
The chessboard is represented as a 2D list of squares, where each square can potentially hold a chess piece. 
The _create() method initializes the board with empty squares, 
and the _add_pieces() method places the pieces (pawns, knights, bishops, rooks, queens, and kings) on the board for both white and black players.
"""

from const import *
from square import Square
from piece import *

class Board:
    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLS)] # Creating a 2D list of eight 0s for each column. 
        self._create() # Filling the board with square objects
        self._add_pieces("white")
        self._add_pieces("black")

    # The _ shows that these are "private" methods.
    def _create(self):
        for row in range(ROWS):
            for col in range (COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, colour):
        row_pawn, row_other = (6, 7) if colour == "white" else (1, 0)

        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(colour))

        # Knights 
        self.squares[row_other][1] = Square(row_other, 1, Knight(colour))
        self.squares[row_other][6] = Square(row_other, 6, Knight(colour))

        # Bishops 
        self.squares[row_other][2] = Square(row_other, 2, Bishop(colour))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(colour))

        # Rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(colour))
        self.squares[row_other][7] = Square(row_other, 7, Rook(colour))

        # Queen 
        self.squares[row_other][3] = Square(row_other, 3, Queen(colour))

        # King 
        self.squares[row_other][4] = Square(row_other, 4, King(colour))