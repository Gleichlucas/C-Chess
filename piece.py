import pygame as pg

class Piece:

    def __init__(self, colour):
        self.colour = colour
        self.image = None
        self.FirstMove = True
        self.legal_moves = []

class Legal(Piece):

    def __init__(self):
        super().__init__('L')
        self.image = pg.transform.scale(pg.image.load("imgs/legal.png"), (60,60))
        self.image.set_colorkey((0,0,0))

class Pawn(Piece):

    def __init__(self,colour):
        super().__init__(colour)
        if (colour == 'W'):
            self.image = pg.transform.scale(pg.image.load("imgs/white_pawn.png"), (60,60))
        else:
            self.image = pg.transform.scale(pg.image.load("imgs/black_pawn.png"), (60,60))

class King(Piece):

    def __init__(self,colour):
        super().__init__(colour)
        if (colour == 'W'):
            self.image = pg.transform.scale(pg.image.load("imgs/white_king.png"), (60,60))
        else:
            self.image = pg.transform.scale(pg.image.load("imgs/black_king.png"), (60,60))

class Queen(Piece):

    def __init__(self,colour):
        super().__init__(colour)
        if (colour == 'W'):
            self.image = pg.transform.scale(pg.image.load("imgs/white_queen.png"), (60,60))
        else:
            self.image = pg.transform.scale(pg.image.load("imgs/black_queen.png"), (60,60))

class Bishop(Piece):

    def __init__(self,colour):
        super().__init__(colour)
        if (colour == 'W'):
            self.image = pg.transform.scale(pg.image.load("imgs/white_bishop.png"), (60,60))
        else:
            self.image = pg.transform.scale(pg.image.load("imgs/black_bishop.png"), (60,60))

class Knight(Piece):

    def __init__(self,colour):
        super().__init__(colour)
        if (colour == 'W'):
            self.image = pg.transform.scale(pg.image.load("imgs/white_knight.png"), (60,60))
        else:
            self.image = pg.transform.scale(pg.image.load("imgs/black_knight.png"), (60,60))


class Rook(Piece):

    def __init__(self,colour):
        super().__init__(colour)
        if (colour == 'W'):
            self.image = pg.transform.scale(pg.image.load("imgs/white_rook.png"), (60,60))
        else:
            self.image = pg.transform.scale(pg.image.load("imgs/black_rook.png"), (60,60))
