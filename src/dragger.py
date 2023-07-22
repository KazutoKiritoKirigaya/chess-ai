import pygame 
from const import *

class Dragger:
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    # Blit method

    def update_blit(self, surface):
        # Increase the size of the piece being moved (from 80px to 128px)
        self.piece.set_texture(size=128) # Just changes the image retrieval path from 80px to 128px
        texture = self.piece.texture
        img = pygame.image.load(texture)
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        # Blit
        surface.blit(img, self.piece.texture_rect)

    # Other methods
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # Pos will be a tuple representing a Cartesian co-ordinate [(xcoor, ycoor)].

    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
    
    def undrag_piece(self):
        self.piece = None
        self.dragging = False