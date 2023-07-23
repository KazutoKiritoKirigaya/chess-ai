"""
The provided code defines a Board class, which represents a chessboard. 
The chessboard is represented as a 2D list of squares, where each square can potentially hold a chess piece. 
The _create() method initializes the board with empty squares, 
and the _add_pieces() method places the pieces (pawns, knights, bishops, rooks, queens, and kings) on the board for both white and black players.
"""

from const import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLS)] # Creating a 2D list of eight 0s for each column. 
        self.last_move = None
        self._create() # Filling the board with square objects
        self._add_pieces("white")
        self._add_pieces("black")

    def move(self, piece, move):
        initial = move.initial
        final = move.final

        # Console board move updates
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        # Pawn promotion 
        if isinstance(piece, Pawn): 
            """
            To the world, you are invisible - it never stops to notice you.
            So you stand up, you leap, twirl, and show them, through a most-exquisite transition.
            """
            self.check_promotion(piece, final)

        # King castling
        if isinstance(piece, King):
            if self.castling(initial, final):
                diff = final.col - initial.col
                rook = piece.left_rook if (diff < 0) else piece.right_rook
                self.move(rook, rook.moves[-1])

        # Move
        piece.moved = True

        # Clear valid moves.
        piece.clear_moves()

        # Set last move
        self.last_move = move

    # Is the move even real? Or is it just a fantasy?
    def valid_move(self, piece, move): 
        return move in piece.moves

    def check_promotion(self, piece, final):
        if final.row == 0 or final.row == 7:
            self.squares[final.row][final.col].piece = Queen(piece.colour)

    def castling(self, initial, final):
        return abs(initial.col - final.col) == 2# If the king has moved two squares, we have castled.

    def calc_moves(self, piece, row, col):
        """
        Calculates all of the possible (valid) moves a piece at a specific position can make.
        """

        def pawn_moves():
            steps = 1 if piece.moved else 2 # Pawns can move 2 squares if this is their first move in the game.

            # Vertical movement
            start = row + piece.dir
            end = row + (piece.dir * (1 + steps))
            for move_row in range(start, end, piece.dir):
                if Square.in_range(move_row):
                    if self.squares[move_row][col].isempty():
                        # Create initial and final move squares.
                        initial = Square(row, col)
                        final = Square(move_row, col)
                        # Create a new move
                        move = Move(initial, final)
                        piece.add_move(move) # Append new move
                    else: # The Pawn's path is blocked. 
                        break
                else: break
            # Diagonal movement
            possible_move_row = row + piece.dir
            possible_move_cols = [col -1, col +1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.colour):
                        # Create initial and final move squares.
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Create a new move 
                        move = Move(initial, final)
                        # Append new move
                        piece.add_move(move)

        def knight_moves():
            # A maximum of 8 moves are possible
            possible_moves = [
                (row -2, col +1),
                (row -1, col +2),
                (row +1, col +2),
                (row +2, col +1),
                (row +2, col -1),
                (row +1, col -2),
                (row -1, col -2),
                (row -2, col -1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col): # Checks whether the move is actually on the board or not with regards to the Knight's current position.
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.colour):
                        # Creates the squares of the new moves.
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # Piece = piece
                        # Creates a new move
                        move = Move(initial, final)
                        # Append new valid move
                        piece.add_move(move)
        
        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        initial = Square(row, col)
                        final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col, final_piece)
                        move = Move(initial, final)

                        if self.squares[possible_move_row][possible_move_col].isempty():
                            if bool:
                                piece.add_move(move)
                            else:
                                piece.add_move(move)

                        # Has enemy piece = add move + break
                        elif self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.colour):
                            if bool:
                                piece.add_move(move)
                                pass
                            else:
                                piece.add_move(move)
                            break

                        elif self.squares[possible_move_row][possible_move_col].has_team_piece(piece.colour):
                            break
                    
                    else: break

                    # Incrementing the increments
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr

        def king_moves():
            adjs = [
                (row -1, col +0), # Upwards
                (row -1, col +1), # Upper right
                (row +0, col +1), # Right
                (row +1, col +1), # Down right
                (row +1, col +0), # Downwards
                (row +1, col -1), # Down left
                (row +0, col -1), # Left
                (row -1, col -1), # Upper left  
            ]

            # Standard king moves
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.colour):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)

            # Castling moves
            if not piece.moved:
                # Queen castling
                left_rook = self.squares[row][0].piece
                if isinstance(left_rook, Rook):
                    if not left_rook.moved:
                        for c in range(1, 4):
                            if self.squares[row][c].has_piece(): # Castling is not possible as there are pieces in between.
                                break
                            
                            if c == 3:
                                piece.left_rook = left_rook # Links the leftward rook to the king.

                                # The rook's movement
                                initial = Square(row, 0)
                                final = Square(row, 3)
                                move = Move(initial, final)
                                left_rook.add_move(move)
                                
                                # The king's movement
                                
                                initial = Square(row, col)
                                final = Square(row, 2)
                                move = Move(initial, final)
                                piece.add_move(move)

                right_rook = self.squares[row][7].piece
                if isinstance(right_rook, Rook):
                    if not right_rook.moved:
                        for c in range(5, 7):
                            if self.squares[row][c].has_piece(): # Castling is not possible as there are pieces in between.
                                break
                            
                            if c == 6:
                                piece.right_rook = right_rook # Links the rightward rook to the king.

                                # The rook's movement
                                initial = Square(row, 7)
                                final = Square(row, 5)
                                move = Move(initial, final)
                                right_rook.add_move(move)
                                
                                # The king's movement
                                initial = Square(row, col)
                                final = Square(row, 6)
                                move = Move(initial, final)
                                right_rook.add_move(move)

        if isinstance(piece, Pawn): # Basically checks if the piece is an instance of the Pawn class.
            pawn_moves()

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            straightline_moves([
                (-1, 1), # Upper right 
                (-1, -1), # Upper left
                (1, 1), # Down right 
                (1, -1) # Down left
            ])

        elif isinstance(piece, Rook):
            straightline_moves([
                (-1, 0), # Upward
                (0, 1), # Leftward
                (1, 0), # Downwards
                (0, -1) # Rightwards

            ])

        elif isinstance(piece, Queen):
            straightline_moves([
                (-1, 1),  
                (-1, -1),
                (1, 1), 
                (1, -1), 
                (-1, 0), 
                (0, 1), 
                (1, 0), 
                (0, -1)
            ])

        elif isinstance(piece, King):
            king_moves()

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