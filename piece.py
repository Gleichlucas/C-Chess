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


class Mover():

        def horizontal_move(self, pos, board):
            y = pos + 1 # looking at all positions to the right of pos
            while (y % 8 != 0):
                if board[y] == None:
                    self.legal_moves.append(y)
                elif self.colour != board[y].colour:
                    self.legal_moves.append(y)
                    break
                else:
                    break
                y += 1

            y = pos - 1 # looking at all the positions to left of pos
            while (y % 8 != 7):
                if board[y] == None:
                    self.legal_moves.append(y)
                elif self.colour != board[y].colour:
                    self.legal_moves.append(y)
                    break
                else:
                    break
                y -= 1

        def vertical_move(self, pos, board):
            y = pos + 8
            while (y <= 63):
                if board[y] == None:
                    self.legal_moves.append(y)
                elif self.colour != board[y].colour:
                    self.legal_moves.append(y)
                    break
                else:
                    break
                y += 8
            y = pos - 8
            while (y >= 0):
                if board[y] == None:
                    self.legal_moves.append(y)
                elif self.colour != board[y].colour:
                    self.legal_moves.append(y)
                    break
                else:
                    break
                y -= 8

        def check_direction(self, pos, board, dir_x, dir_y):
            x = pos % 8
            y = pos // 8
            m = 1
            if dir_y < 0:
                m = -1
            tmp = pos + (dir_y * 8 + dir_x)
            x += dir_x
            y += dir_y
            while (tmp <= 63 and tmp >= 0 and x >= 0 and x <= 7 and y >= 0 and y <= 7):
                if board[tmp] == None:
                    self.legal_moves.append(tmp)
                elif self.colour != board[tmp].colour:
                    self.legal_moves.append(tmp)
                    break
                else:
                    break
                x += dir_x
                y += dir_y

                tmp += (dir_y * 8 + dir_x)

        def diagonal_moves(self, pos, board):
            self.check_direction(pos, board, 1,1)
            self.check_direction(pos, board, -1,-1)
            self.check_direction(pos, board, -1,1)
            self.check_direction(pos, board, 1,-1)

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
        for z in arr:
            if 0 <= z[0] < 8 and 0 <= z[1] < 8 and (board[z[1]*8+z[0]] == None or self.colour != board[z[1]*8+z[0]].colour):
                self.legal_moves.append(z[1]*8+z[0])

class Queen(Piece, Mover):

    def __init__(self,colour):
        super().__init__(colour)
        if (colour == 'W'):
            self.image = pg.transform.scale(pg.image.load("imgs/white_queen.png"), (60,60))
        else:
            self.image = pg.transform.scale(pg.image.load("imgs/black_queen.png"), (60,60))
    def move(self, pos, board):
        self.horizontal_move(pos, board)
        self.vertical_move(pos, board)
        self.diagonal_moves(pos, board)

class Bishop(Piece, Mover):

    def __init__(self,colour):
        super().__init__(colour)
        if (colour == 'W'):
            self.image = pg.transform.scale(pg.image.load("imgs/white_bishop.png"), (60,60))
        else:
            self.image = pg.transform.scale(pg.image.load("imgs/black_bishop.png"), (60,60))

    def move(self, pos, board):
        self.diagonal_moves(pos, board)

class Knight(Piece):

    def __init__(self,colour):
        super().__init__(colour)
        if (colour == 'W'):
            self.image = pg.transform.scale(pg.image.load("imgs/white_knight.png"), (60,60))
        else:
            self.image = pg.transform.scale(pg.image.load("imgs/black_knight.png"), (60,60))

    def move(self, pos, board):
        x = pos % 8
        y = pos // 8

        arr = [(x+1, y-2),(x+2, y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2),(x-2,y+1),(x-2,y-1),(x-1,y-2)]
        for z in arr:
            if 0 <= z[0] < 8 and 0 <= z[1] < 8 and (board[z[1]*8+z[0]] == None or self.colour != board[z[1]*8+z[0]].colour):
                self.legal_moves.append(z[1]*8+z[0])

class Rook(Piece, Mover):

    def __init__(self,colour):
        super().__init__(colour)
        if (colour == 'W'):
            self.image = pg.transform.scale(pg.image.load("imgs/white_rook.png"), (60,60))
        else:
            self.image = pg.transform.scale(pg.image.load("imgs/black_rook.png"), (60,60))
    def move(self, pos, board):
        self.horizontal_move(pos, board)
        self.vertical_move(pos, board)
