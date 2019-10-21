import pygame as pg
class Piece:


    def __init__(self):
        self.image = None
        self.FirstMove = True
        self.legal_moves = []

class Legal(Piece):

    def __init__(self):
        self.image = pg.transform.scale(pg.image.load("imgs/legal.png"), (60,60))
        self.image.set_colorkey((0,0,0))

class WPiece(Piece):

    def __init__(self):
        super().__init__()

class BPiece(Piece):

    def __init__(self):
        super().__init__()

class WPawn(WPiece):

    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/white_pawn.png"), (60,60))


class BPawn(BPiece):

    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/black_pawn.png"), (60,60))

class BKing(BPiece):

    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/black_king.png"), (60,60))


class WKing(WPiece):

    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/white_king.png"), (60,60))

class BQueen(BPiece):

    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/black_queen.png"), (60,60))

class WQueen(WPiece):

    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/white_queen.png"), (60,60))

class BBishop(BPiece):

    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/black_bishop.png"), (60,60))

class WBishop(WPiece):

    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/white_bishop.png"), (60,60))

class WKnight(WPiece):

    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/white_knight.png"), (60,60))

class BKnight(BPiece):

    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/black_knight.png"), (60,60))

class BRook(BPiece):

    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/black_rook.png"), (60,60))

class WRook(WPiece):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imgs/white_rook.png"), (60,60))


# self.image = pg.transform.scale(pg.image.load("imgs/legal.png"), (60,60))
# self.image.set_colorkey((0,0,0))
#
class Board:

    def __init__(self):
        self.image = pg.transform.scale(pg.image.load("imgs/board.png"), (640,640))
        self.testp = pg.image.load("imgs/pieces.png")
        self.squares = []
        self.legal = []

        for i in range(64):
            self.legal.append(None)

        #add pieces
        self.squares.append(BRook())
        self.squares.append(BKnight())
        self.squares.append(BBishop())
        self.squares.append(BQueen())
        self.squares.append(BKing())
        self.squares.append(BBishop())
        self.squares.append(BKnight())
        self.squares.append(BRook())
        for i in range(8):
            self.squares.append(BPawn())
        for i in range(4 * 8):
            self.squares.append(None)
        for i in range(8):
            self.squares.append(WPawn())
        self.squares.append(WRook())
        self.squares.append(WKnight())
        self.squares.append(WBishop())
        self.squares.append(WQueen())
        self.squares.append(WKing())
        self.squares.append(WBishop())
        self.squares.append(WKnight())
        self.squares.append(WRook())

        self.WTurn = True
        self.time = 0

    def horizontal_move(self, p, x):
        y = x + 1
        if isinstance(p, WPiece):
            test = BPiece
        else:
            test = WPiece
        while (y % 8 != 0):
            if self.squares[y] == None:
                p.legal_moves.append(y)
            elif isinstance(self.squares[y], test):
                p.legal_moves.append(y)
                break
            else:
                break
            y += 1
        y = x - 1
        while (y % 8 != 7):
            if self.squares[y] == None:
                p.legal_moves.append(y)
            elif isinstance(self.squares[y], test):
                p.legal_moves.append(y)
                break
            else:
                break
            y -= 1





    def vertical_move(self, p, x):
        y = x + 8
        if isinstance(p, WPiece):
            test = BPiece
        else:
            test = WPiece
        while (y <= 63):
            if self.squares[y] == None:
                p.legal_moves.append(y)
            elif isinstance(self.squares[y], test):
                p.legal_moves.append(y)
                break
            else:
                break
            y += 8
        y = x - 8
        while (y >= 0):
            if self.squares[y] == None:
                p.legal_moves.append(y)
            elif isinstance(self.squares[y], test):
                p.legal_moves.append(y)
                break
            else:
                break
            y -= 8

    def pawn_moves(self, p, x):
        m = 1
        if isinstance(p, WPiece):
            test = BPiece
            m = -1
        else:
            test = WPiece
        if x+8*m <= 63 and self.squares[x+8*m] == None:
            p.legal_moves.append(x+8*m)
        if x+9*m <= 63 and x % 8 != 7 and isinstance(self.squares[x+9*m], test):
            p.legal_moves.append(x+9*m)
        if x+7*m <= 63 and x % 8 != 0 and isinstance(self.squares[x+7*m], test):
            p.legal_moves.append(x+7*m)
        if p.FirstMove and x+16*m <= 63 and self.squares[x+16*m] == None:
            p.legal_moves.append(x+16*m)


    def jump_moves(self, p, pos):
        if isinstance(p, WPiece):
            test = BPiece
        else:
            test = WPiece
        x = pos % 8
        y = pos // 8

        arr = [(x+1, y-2),(x+2, y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2),(x-2,y+1),(x-2,y-1),(x-1,y-2)]
        for pos in arr:
            if 0 <= pos[0] < 8 and 0 <= pos[1] < 8 and (isinstance(self.squares[pos[1]*8+pos[0]],test) or self.squares[pos[1]*8+pos[0]] == None):
                p.legal_moves.append(pos[1]*8+pos[0])

    def check_direction(self, p, test, pos, dir):
        x = pos % 8
        y = pos // 8
        m = 1
        if dir < 0:
            m = -1
        tmp = pos + dir
        if dir == 9:
            x += 1
            y += 1
        elif dir == -9:
            y -= 1
            x -= 1
        elif dir == 7:
            x -= 1
            y += 1
        elif dir == -7:
            x += 1
            y -= 1
        while (tmp <= 63 and tmp >= 0 and x >= 0 and x <= 7 and y >= 0 and y <= 7):
            if self.squares[tmp] == None:
                p.legal_moves.append(tmp)
            elif isinstance(self.squares[tmp], test):
                p.legal_moves.append(tmp)
                break
            else:
                break
            if dir == 9:
                x += 1
                y += 1
            elif dir == -9:
                y -= 1
                x -= 1
            elif dir == 7:
                x -= 1
                y += 1
            elif dir == -7:
                x += 1
                y -= 1

            tmp += dir


            
    def diagonal_moves(self, p, pos):
        if isinstance(p, WPiece):
            test = BPiece
        else:
            test = WPiece
        self.check_direction(p, test, pos, 9)
        self.check_direction(p, test, pos, -9)
        self.check_direction(p, test, pos, 7)
        self.check_direction(p, test, pos, -7)

    def king_moves(self, p , pos):
        if isinstance(p, WPiece):
            test = BPiece
        else:
            test = WPiece


    def legal_moves(self):
        x = 0  #x is the postion in the list squares
        for p in self.squares:
            if isinstance(p, WPawn) or isinstance(p, BPawn):
                self.pawn_moves(p, x)
            if isinstance(p, BKnight) or isinstance(p, WKnight):
                self.jump_moves(p, x)
            if isinstance(p, WBishop) or isinstance(p, BBishop):
                self.diagonal_moves(p,x)
            if isinstance(p, WRook) or isinstance(p, BRook):
                self.horizontal_move(p, x)
                self.vertical_move(p,x)
            if isinstance(p, WQueen) or isinstance(p, BQueen):
                self.horizontal_move(p, x)
                self.vertical_move(p,x)
                self.diagonal_moves(p,x)
            if isinstance(p, WRook) or isinstance(p, BRook):
                self.horizontal_move(p, x)
                self.vertical_move(p,x)
            if isinstance(p, WKing) or isinstance(p, BKing):
                pass
                #self.king_moves(p,x)
            x += 1

    def free_moves(self):
        for x in range(64):
            if isinstance(self.squares[x], Piece):
                self.squares[x].legal_moves = []
        self.legal = []
        for i in range(64):
            self.legal.append(None)
