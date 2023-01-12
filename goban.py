#!/usr/bin/env python3
# from math import ceil
BLACK = -1
EMPTY = 0
WHITE = 1
SIZE = 19


class Board:
    def __init__(self, SIZE):
        """Using the '1-1 Style'. the 'A1' style.
        Note that 'i' is ommited to avoid confusion with 'j'."""
        self.board = [[EMPTY for col in range(SIZE)] for row in range(SIZE)]
        self.size = SIZE
        self.row_alpha = 'ABCDEFGHJKLMNOPQRST'
        self.white = '\033[0;37;43m'
        self.black = '\033[0;30;43m'
        self.goban = '\033[0;30;43m'
        self.normal = '\033[0m'
        self.stone = '●'
        self.blank = '○'
        self.empty = '·'
        self.hoshi = '+'

    def display(self):
        """Board is passed around without coordinates,
        which are added at printing."""
        col_num0 = iter(range(self.size, 0, -1))
        col_num1 = iter(range(self.size, 0, -1))
        print('   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))
        print('\n'.join(self.normal + f"{next(col_num0):>2}" + ' ' + ' '.join(str(self.white + self.stone if piece == 1 else self.black + self.stone if piece == -1 else self.goban + self.empty) for piece in row) + self.normal + ' ' + f"{next(col_num1):<2}" for row in self.board))
        print(self.normal + '   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))


#
# def hoshi_add(SIZE):
#     """Add hoshi in proper places to any odd sided board"""
#     if SIZE % 2 == 0:
#         return
#     print(1)
#     half = fill = int((SIZE // 2))
#     while half > 3:
#         board[half] = fill * EMPTY + HOSHI + fill * EMPTY
#         half = int((half // 2))
#     if SIZE <= 14:
#         return
