import pygame as pg

from piece import Piece, Legal, Pawn, Knight, Bishop, Rook, Queen, King

class Board:

    def __init__(self):
        self.image = pg.transform.scale(pg.image.load("imgs/board.png"), (640,640))
        self.testp = pg.image.load("imgs/pieces.png")
        self.squares = []
        self.legal = []

        for i in range(64):
            self.legal.append(None)

        #add pieces
        self.squares.append(Rook('B'))
        self.squares.append(Knight('B'))
        self.squares.append(Bishop('B'))
        self.squares.append(Queen('B'))
        self.squares.append(King('B'))
        self.squares.append(Bishop('B'))
        self.squares.append(Knight('B'))
        self.squares.append(Rook('B'))
        for i in range(8):
            self.squares.append(Pawn('B'))
        for i in range(4 * 8):
            self.squares.append(None)
        for i in range(8):
            self.squares.append(Pawn('W'))
        self.squares.append(Rook('W'))
        self.squares.append(Knight('W'))
        self.squares.append(Bishop('W'))
        self.squares.append(Queen('W'))
        self.squares.append(King('W'))
        self.squares.append(Bishop('W'))
        self.squares.append(Knight('W'))
        self.squares.append(Rook('W'))

        self.WTurn = True
        self.time = 0

    def horizontal_move(self, p, x):
        y = x + 1 # looking at all positions to the right of p
        while (y % 8 != 0):
            if self.squares[y] == None:
                p.legal_moves.append(y)
            elif p.colour != self.squares[y].colour:
                p.legal_moves.append(y)
                break
            else:
                break
            y += 1

        y = x - 1 # looking at all the positions to left of p
        while (y % 8 != 7):
            if self.squares[y] == None:
                p.legal_moves.append(y)
            elif p.colour != self.squares[y].colour:
                p.legal_moves.append(y)
                break
            else:
                break
            y -= 1





    def vertical_move(self, p, x):
        y = x + 8
        while (y <= 63):
            if self.squares[y] == None:
                p.legal_moves.append(y)
            elif p.colour != self.squares[y].colour:
                p.legal_moves.append(y)
                break
            else:
                break
            y += 8
        y = x - 8
        while (y >= 0):
            if self.squares[y] == None:
                p.legal_moves.append(y)
            elif p.colour != self.squares[y].colour:
                p.legal_moves.append(y)
                break
            else:
                break
            y -= 8

    def pawn_moves(self, p, x):
        m = 1
        if p.colour == 'W':
            m = -1
        if x+8*m <= 63 and self.squares[x+8*m] == None:
            p.legal_moves.append(x+8*m)
        if x+9*m <= 63 and x % 8 != 7 and self.squares[x+9*m] != None and p.colour != self.squares[x+9*m].colour:
            p.legal_moves.append(x+9*m)
        if x+7*m <= 63 and x % 8 != 0 and self.squares[x+7*m] != None and p.colour != self.squares[x+7*m].colour:
            p.legal_moves.append(x+7*m)
        if p.FirstMove and x+16*m <= 63 and self.squares[x+8*m] == None and self.squares[x+16*m] == None:
            p.legal_moves.append(x+16*m)


    def jump_moves(self, p, pos):
        x = pos % 8
        y = pos // 8

        arr = [(x+1, y-2),(x+2, y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2),(x-2,y+1),(x-2,y-1),(x-1,y-2)]
        for pos in arr:
            if 0 <= pos[0] < 8 and 0 <= pos[1] < 8 and (self.squares[pos[1]*8+pos[0]] == None or p.colour != self.squares[pos[1]*8+pos[0]].colour):
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

    def check_for_pinning_piece_v(self, king_colour, pos, dir):

        pinned = False
        tmp = pos
        tmp += dir

        while(tmp // 8 <= 7 and tmp // 8 >= 0):

            if self.squares[tmp] == None:
                tmp += dir
                continue
            if (isinstance(self.squares[tmp], Rook) or isinstance(self.squares[tmp], Queen)) and self.squares[tmp] != king_colour:
                pinned = True
                break
            else:
                break

        if not pinned:
            return
        print(str(self.squares[pos]) + " is vertical pinned")
        self.squares[pos].legal_moves[:] = [x for x in self.squares[pos].legal_moves if x % 8 == pos % 8]


    def check_horizontal_pin(self,p, pos):
        # looking for the first horizontal piece of the same colour as the king that might be pinned
        if isinstance(p, WKing):
            test = WPiece
            killer = 1
        else:
            test = BPiece
            killer = -1


        tmp = pos + 1
        while(tmp % 8 <= 7):
            # this loop will break after it finds the first piece, if its of same colour it will check if its pinned
            if self.squares[tmp] == None:
                tmp +=1
                continue
            if self.squares[tmp].colour == p.colour:
                self.check_for_pinning_piece_h(p.colour, tmp, 1)
                break
            else:
                break
        tmp = pos - 1
        while(tmp % 8 >= 0):

            if self.squares[tmp] == None:
                tmp -=1
                continue
            if isinstance(self.squares[tmp], test):
                self.check_for_pinning_piece_h(p.colour,tmp, -1)
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

    def check_direction(self, p, pos, dir):

        # dir == 9: right-down, dir == -9 left-up, dir == 7 left-down, dir == -7 right-up
        # x and y are the translated position of the piece,
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
            elif p.colour != self.squares[tmp].colour:
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
        self.check_direction(p, pos, 9)
        self.check_direction(p, pos, -9)
        self.check_direction(p, pos, 7)
        self.check_direction(p, pos, -7)

    def king_moves(self, p , pos):
        x = pos % 8
        y = pos // 8

        arr = [(x, y-1),(x+1, y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1)]
        for pos in arr:
            if 0 <= pos[0] < 8 and 0 <= pos[1] < 8 and (self.squares[pos[1]*8+pos[0]] == None or p.colour != self.squares[pos[1]*8+pos[0]].colour):
                p.legal_moves.append(pos[1]*8+pos[0])


    def legal_moves(self):
        x = 0  #x is the postion in the list squares
        for p in self.squares:
            if isinstance(p, Pawn):
                self.pawn_moves(p, x)
            if isinstance(p, Knight):
                self.jump_moves(p, x)
            if isinstance(p, Bishop):
                self.diagonal_moves(p,x)
            if isinstance(p, Rook):
                self.horizontal_move(p, x)
                self.vertical_move(p,x)
            if isinstance(p, Queen):
                self.horizontal_move(p, x)
                self.vertical_move(p,x)
                self.diagonal_moves(p,x)
            if isinstance(p, Rook):
                self.horizontal_move(p, x)
                self.vertical_move(p,x)
            if isinstance(p, King):
                self.king_moves(p,x)
                #self.check_horizontal_pin(p,x)
                #self.check_vertical_pin(p,x)
            x += 1

    def free_moves(self):
        for x in range(64):
            if self.squares[x] != None:
                self.squares[x].legal_moves = []
        self.legal = []
        for i in range(64):
            self.legal.append(None)
