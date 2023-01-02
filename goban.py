#!/usr/bin/env python3
from resources import *
# from math import ceil


class Board:
    def __init__(self, SIZE):
        """Using the '1-1 Style'. the 'A1' style.
        Note that 'i' is ommited to avoid confusion with 'j'."""
        self.board = [[EMPTY for col in range(SIZE)] for row in range(SIZE)]
        self.size = SIZE
        self.row_alpha = 'ABCDEFGHJKLMNOPQRST'

    def display(self):
        """Board is passed around without coordinates, which are added at printing."""
        col_num = iter(range(1, self.size + 2))
        print('   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))
        print('\n'.join(color.normal + f"{next(col_num):>2}" + ' ' + ' '.join(str(color.white + goban.stone if piece == 1 else color.black + goban.stone if piece == -1 else color.goban + goban.empty) for piece in row) for row in self.board))
        print(color.normal + '   ' + ' '.join(['ABCDEFGHJKLMNOPQRST'[row] for row in range(self.size)]))


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
