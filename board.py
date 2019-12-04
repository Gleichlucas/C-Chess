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






    def check_for_pinning_piece_h(self, king_colour, pos, dir):
        pinned = False
        tmp = pos
        tmp += dir
        while(tmp % 8 <= 7 and tmp % 8 >= 0):

            if self.squares[tmp] == None:
                tmp += dir
                continue
            if (isinstance(self.squares[tmp], Rook) or isinstance(self.squares[tmp], Queen)) and self.squares[tmp].colour != king_colour:
                print("king colour is " + str(king_colour) +" and colour of piece " + str(self.squares[tmp].colour))
                pinned = True
                break
            else:
                break
        if not pinned:
            return
        print(str(type(self.squares[pos])) + " on "+ str(pos//8 +1)+ ","+str(pos%8 + 1) + " is horizontal pinned")
        self.squares[pos].legal_moves[:] = [x for x in self.squares[pos].legal_moves if x // 8 == pos // 8]

    def check_for_pinning_piece_v(self, king_colour, pos, dir):

        pinned = False
        tmp = pos
        tmp += dir

        while(tmp // 8 <= 7 and tmp // 8 >= 0):

            if self.squares[tmp] == None:
                tmp += dir
                continue
            if (isinstance(self.squares[tmp], Rook) or isinstance(self.squares[tmp], Queen)) and self.squares[tmp].colour != king_colour:
                print("king colour is " + str(king_colour) +" and colour of piece " + str(self.squares[tmp].colour))
                pinned = True
                break
            else:
                break

        if not pinned:
            return
        print("king colour is " + str(king_colour))
        print(str(type(self.squares[pos])) + " on "+ str(pos//8 +1)+ ","+str(pos%8 + 1) + " is vertical pinned")
        self.squares[pos].legal_moves[:] = [x for x in self.squares[pos].legal_moves if x % 8 == pos % 8]


    def check_horizontal_pin(self,p, pos):
        # looking for the first horizontal piece of the same colour as the king that might be pinned
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
                tmp -= 1
                continue
            if self.squares[tmp].colour == p.colour:
                self.check_for_pinning_piece_h(p.colour,tmp, -1)
                break
            else:
                break

    def check_vertical_pin(self,p, pos):
        tmp = pos + 8
        while(tmp // 8 <= 7):
            if self.squares[tmp] == None:
                tmp +=8
                continue
            if self.squares[tmp].colour == p.colour:
                self.check_for_pinning_piece_v(p.colour, tmp, 8)
                break
            else:
                break
        tmp = pos - 8
        while(tmp // 8 >= 0):
            if self.squares[tmp] == None:
                tmp -= 8
                continue
            if self.squares[tmp].colour == p.colour:
                self.check_for_pinning_piece_v(p.colour,tmp, -8)
                break
            else:
                break

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
                p.move(x, self.squares)
                self.check_horizontal_pin(p,x)
                self.check_vertical_pin(p,x)
            x += 1

    def free_moves(self):
        for x in range(64):
            if self.squares[x] != None:
                self.squares[x].legal_moves = []
        self.legal = []
        for _ in range(64):
            self.legal.append(None)
