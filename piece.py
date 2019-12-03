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

    def move(self, pos, board):
        m = 1
        if self.colour == 'W':
            m = -1
        if pos+8*m <= 63 and board[pos+8*m] == None:
            self.legal_moves.append(pos+8*m)
        if pos+9*m <= 63 and pos % 8 != 7 and board[pos+9*m] != None and self.colour != board[pos+9*m].colour:
            self.legal_moves.append(pos+9*m)
        if pos+7*m <= 63 and pos % 8 != 0 and board[pos+7*m] != None and self.colour != board[pos+7*m].colour:
            self.legal_moves.append(pos+7*m)
        if self.FirstMove and pos+16*m <= 63 and board[pos+8*m] == None and board[pos+16*m] == None:
            self.legal_moves.append(pos+16*m)

class King(Piece):

    def __init__(self,colour):
        super().__init__(colour)
        if (colour == 'W'):
            self.image = pg.transform.scale(pg.image.load("imgs/white_king.png"), (60,60))
        else:
            self.image = pg.transform.scale(pg.image.load("imgs/black_king.png"), (60,60))

    def move(self, pos, board):
        x = pos % 8
        y = pos // 8

        arr = [(x, y-1),(x+1, y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1)]
        for pos in arr:
            if 0 <= pos[0] < 8 and 0 <= pos[1] < 8 and (board[pos[1]*8+pos[0]] == None or self.colour != board[pos[1]*8+pos[0]].colour):
                self.legal_moves.append(pos[1]*8+pos[0])

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
