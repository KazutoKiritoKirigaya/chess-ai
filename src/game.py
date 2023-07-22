import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:
    def __init__(self) :
        self.board = Board()
        self.dragger = Dragger()

    # Show methods
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    colour = (234, 235, 200) # Light green
                else:
                    colour = (119, 154, 88) # Dark green

                rect = ((col * SQSIZE), (row * SQSIZE), SQSIZE, SQSIZE )
                pygame.draw.rect(surface, colour, rect)
    
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
        if self.dragger.dragging:
            piece = self.dragger.piece

            # Loop through all of the valid moves and blit them to the screen.
            for move in piece.moves:
                # Blit colour
                colour = "#C86464" if (move.final.row + move.final.col ) % 2 == 0 else "#C84646"
                # Blit rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                # Blit it
                pygame.draw.rect(surface, colour, rect)
