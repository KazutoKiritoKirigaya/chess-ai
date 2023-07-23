import pygame
from config import Config
from const import *
from board import Board
from dragger import Dragger
from square import Square
class Game:
    def __init__(self):
        self.next_player = "white"
        self.hovered_sqr = None
        self.board = Board()
        self.dragger = Dragger()
        self.config = Config()

    # Show methods
    def show_bg(self, surface):
        theme = self.config.theme
        
        for row in range(ROWS):
            for col in range(COLS):
                colour = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                rect = ((col * SQSIZE), (row * SQSIZE), SQSIZE, SQSIZE ) # Rect
                pygame.draw.rect(surface, colour, rect) # Blits it
                # Row co-ordinates
                if col == 0:
                    # Colour
                    colour = theme.bg.dark if row % 2 == 0 else theme.bg.light
                    # Label 
                    lbl = self.config.font.render(str(ROWS-row), 1, colour)
                    lbl_pos = (5, 5 + row * SQSIZE)
                    # Blit it
                    surface.blit(lbl, lbl_pos)

                # Column co-ordinates
                if row == 7:
                    # Colour
                    colour = theme.bg.dark if (row + col) % 2 == 0 else theme.bg.light
                    # Label 
                    lbl = self.config.font.render(Square.get_alphacol(col), 1, colour)
                    lbl_pos = (col * SQSIZE + SQSIZE - 20, HEIGHT - 20)
                    # Blit it
                    surface.blit(lbl, lbl_pos)

    
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # Is there a piece on this specific square?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    # Blits all pieces except the one being dragged.
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80) # The default size is already 80px, but we're still sending it in as an argument.
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface): # Shows the possible valid moves a selected piece can make.
        theme = self.config.theme

        if self.dragger.dragging:
            piece = self.dragger.piece

            # Loop through all of the valid moves and blit them to the screen.
            for move in piece.moves:
                # Blit colour
                colour = theme.moves.light if (move.final.row + move.final.col ) % 2 == 0 else theme.moves.dark
                # Blit rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                # Blit it
                pygame.draw.rect(surface, colour, rect)

    def show_last_move(self, surface):
        theme = self.config.theme
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            for pos in [initial, final]:
                # Blit Colour
                colour = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                # Blit rect
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                # Blit it
                pygame.draw.rect(surface, colour, rect)
    
    def show_hover(self, surface):
        if self.hovered_sqr:
            # Blit Colour
            colour = (180, 180, 180)
            # Blit rect
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            # Blit it
            pygame.draw.rect(surface, colour, rect, width=3)


    def next_turn(self):
        self.next_player = "white" if self.next_player == "black" else "black"

    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]

    def change_theme(self):
        self.config.change_theme()

    def sound_effect(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()

    def reset(self): # That which thou seeketh hath now been bestowed unto thee, for my promise stands as solid as stone.
        self.__init__()