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
        if p.FirstMove and x+16*m <= 63 and self.squares[x+8*m] == None and self.squares[x+16*m] == None:
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

    def check_for_pinning_piece_h(self, killer, pos, dir):
        if killer == 1:
            test = BRook
            test2 = BQueen
        else:
            test = WRook
            test2 = WQueen
        pinned = False
        tmp = pos
        tmp += dir
        while(tmp % 8 <= 7 and tmp % 8 >= 0):

            if self.squares[tmp] == None:
                tmp += dir
                continue
            if isinstance(self.squares[tmp], test) or isinstance(self.squares[tmp], test2):
                pinned = True
                break
            else:
                break
        if not pinned:
            return
        print(str(self.squares[pos]) + " is horizontal pinned")
        self.squares[pos].legal_moves[:] = [x for x in self.squares[pos].legal_moves if x // 8 == pos // 8]

    def check_for_pinning_piece_v(self, killer, pos, dir):
        if killer == 1:
            test = BRook
            test2 = BQueen
        else:
            test = WRook
            test2 = WQueen
        pinned = False
        tmp = pos
        tmp += dir
        while(tmp // 8 <= 7 and tmp // 8 >= 0):

            if self.squares[tmp] == None:
                tmp += dir
                continue
            if isinstance(self.squares[tmp], test) or isinstance(self.squares[tmp], test2):
                pinned = True
                break
            else:
                break
        if not pinned:
            return
        print(str(self.squares[pos]) + " is vertical pinned")
        self.squares[pos].legal_moves[:] = [x for x in self.squares[pos].legal_moves if x % 8 == pos % 8]


    def check_horizontal_pin(self,p, pos):
        if isinstance(p, WKing):
            test = WPiece
            killer = 1
        else:
            test = BPiece
            killer = -1

        tmp = pos + 1
        while(tmp % 8 <= 7):
            if self.squares[tmp] == None:
                tmp +=1
                continue
            if isinstance(self.squares[tmp], test):
                self.check_for_pinning_piece_h(killer, tmp, 1)
                break
            else:
                break
        tmp = pos - 1
        while(tmp % 8 >= 0):

            if self.squares[tmp] == None:
                tmp -=1
                continue
            if isinstance(self.squares[tmp], test):
                self.check_for_pinning_piece_h(killer,tmp, -1)
                break
            else:
                break

    def check_vertical_pin(self,p, pos):
        if isinstance(p, WKing):
            test = WPiece
            killer = 1
        else:
            test = BPiece
            killer = -1

        tmp = pos + 8
        while(tmp // 8 <= 7):
            if self.squares[tmp] == None:
                tmp +=8
                continue
            if isinstance(self.squares[tmp], test):
                self.check_for_pinning_piece_v(killer, tmp, 8)
                break
            else:
                break
        tmp = pos - 8
        while(tmp // 8 >= 0):

            if self.squares[tmp] == None:
                tmp -= 8
                continue
            if isinstance(self.squares[tmp], test):
                self.check_for_pinning_piece_v(killer,tmp, -8)
                break
            else:
                break
        '''
        if isinstance(p, WPiece):
            test = BKing
            test2 = BPiece
        else:
            test = WKing
            test2 = WPiece
        tmp = pos + 1
        hasKing = 0
        while(tmp % 8 <= 7):

            if self.squares[tmp] == None:
                tmp +=1
                continue
            if isinstance(self.squares[tmp], test):
                hasKing = 1
                break
            else:
                break
        if not hasKing:
            tmp = pos -1
            while(tmp % 8 >= 0):

                if self.squares[tmp] == None:
                    tmp -=1
                    continue;
                if isinstance(self.squares[tmp], test):
                    hasKing = -1
                    break
                else:
                    break
        if hasKing == 0:
            return
        tmp = pos + hasKing

        while(tmp % 8 >= 0 and tmp % 8 <= 7):
            if self.squares[tmp] == None:
                tmp += hasKing
                continue;
            if isinstance(self.squares[tmp], test2):
                self.squares[tmp].horizontal_pinned()
                break
            else:
                break
        '''





    def is_pinned(self,p, pos):
        if isinstance(p, WPiece):
            test = BKing
        else:
            test = WKing
        x = pos % 8
        y = pos // 8
        arr = []
        while (x <= 6):
            arr.append(pos+1)
            x += 1

        #1. find if king is alined -> find if checking piece is alined
        #horizontal pin
        # remove
        #vertical pin

        #diagonal pin


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
        x = pos % 8
        y = pos // 8

        arr = [(x, y-1),(x+1, y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1)]
        for pos in arr:
            if 0 <= pos[0] < 8 and 0 <= pos[1] < 8 and (isinstance(self.squares[pos[1]*8+pos[0]],test) or self.squares[pos[1]*8+pos[0]] == None):
                p.legal_moves.append(pos[1]*8+pos[0])


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
                self.king_moves(p,x)
                self.check_horizontal_pin(p,x)
                self.check_vertical_pin(p,x)
            x += 1

    def free_moves(self):
        for x in range(64):
            if isinstance(self.squares[x], Piece):
                self.squares[x].legal_moves = []
        self.legal = []
        for i in range(64):
            self.legal.append(None)
'''
print("black pieces:")
for y in range(2):
    for x in range(8):
        box = (0+x*103,0+y*103,103+x*103, 103+ y*103)
        tmp = im.crop(box)
        tmp.show()
'''
