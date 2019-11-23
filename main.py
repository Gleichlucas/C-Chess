import pygame as pg
import time
from board import Board
from piece import Legal
H1 = 28
def setup():
    #background = pg.image.load("imgs/board.png")
    #apple = pg.transform.scale(apple, (16, 16))
    pg.display.set_caption("chess")

    return pg.display.set_mode((640,640))
'''
top left = 28, 28
piece size is 75 pixel
'''
def draw(screen, board,m_piece , mx, my):
    screen.blit(board.image, (0, 0))
    x = 0
    for i in range (28,600,75):
        for j in range(28,600,75):
            if board.legal[x] is not None:
                screen.blit(board.legal[x].image,(j, i))
            if board.squares[x] is not None:
                screen.blit(board.squares[x].image,(j, i))
            x+=1
    if m_piece != None:
        screen.blit(m_piece.image,(mx-37, my-37))



     #screen.blit(pawn.image, (20, 20))
     #screen.blit(board.testp, (0, 0), pg.Rect((0,0), (664/8, 215/2)))
    pg.display.flip()

def pixel_to_array(x,y):
    if x < 20 or x > 619 or y < 20 or y > 619: #offboard
        return None
    x = (x-20)//75
    y = ((y-20)//75)*8
    return y + x

def main():
    pg.init()
    screen = setup()
    board = Board()
    running = True
    mx, my = 0, 0
    m_piece = None
    while (running):

        s = time.perf_counter()
        mx,my = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if m_piece:
                    if pixel_to_array(mx,my) != None:
                        m_piece.FirstMove = False
                        board.squares[pixel_to_array(mx,my)] = m_piece
                        board.free_moves()
                        m_piece = None

                else:
                    if pixel_to_array(mx,my) != None:
                        board.legal_moves()
                        if board.WTurn == True:
                            board.WTurn = False
                        else:
                            board.WTurn = True
                        m_piece = board.squares[pixel_to_array(mx,my)]
                        for x in m_piece.legal_moves:
                            board.legal[x] = Legal()
                        board.squares[pixel_to_array(mx,my)] = None

        draw(screen, board, m_piece, mx, my)
        keys = pg.key.get_pressed()
        t = time.perf_counter()
        fps = 1/(t-s)
        #print("FPS: " + str(fps))

        #if keys[pg.K_w]:

if __name__=="__main__":
    main()
