import pyscreenshot as ImageGrab
import time
import functools

if __name__ == '__main__':
    # part of the screen
    im = ImageGrab.grab(bbox=(227, 136, 1051, 960))  # X1,Y1,X2,Y2
    im = im.convert('L')
    #one field is 103x103 -> 51- 51
    flag = True
    c = []
    while(1):
        time.sleep(1)
        print("time passed")
        if flag:
            b = []
        else:
            c = []
        for y in range(8):
            lst = []
            for x in range(8):
                p =  im.getpixel((53+x*103, 80+y*103))
                conv = 'E'
                if p == 83:
                    conv = 'B'
                elif p == 248:
                    conv = 'W'
                lst.append(conv)
            if flag:
                b.append(lst)
            else:
                c.append(lst)
        if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, b, c), True):
            if flag:
                print(b)
            else:
                print(c)
        flag = not flag
