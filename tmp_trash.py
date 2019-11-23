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



    def horizontal_move(self, p, x):
        y = x + 1
        if isinstance(p, WPiece): #if p.colour == 'W':
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
