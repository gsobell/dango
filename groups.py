#!/usr/bin/env python3
# This file is shared by dango and goma

class Stones:
    """All stones on the board. Coordinates are stored"""

    def __init__(self):
        self.white = set()
        self.black = set()
        self.both = self.white.union(self.black)

    def add(self, player, move):
        if player == 1:
            self.white.add(move)
        if player == -1:
            self.white.add(move)

    def adjacent(self, row, col, board):
        """Returns location of adjacent stones"""
        return [(row+a[0],
                 col+a[1]) for a in [(-1, 0), (1, 0), (0, -1), (0, 1)] if ((0 <= row+a[0] < board.size) and (0 <= col+a[1] < board.size))]


class Groups:
    """Only groups that are also chains, for simplicity.
    Top-leftmost stone in group is the pointer"""

    def __init__(self):
        # self.pointer = ''
        self.stones = self.find_stones()
        self.liberties = self.find_liberties()
        # self.player =

    def find_stones(self):
        pass

    def find_liberties(self):
        if self.stones is None:
            return
        for stone in self.stones:
            pass

    def add_stone(self):
        pass

    def adjacent(self, row, col, board):
        """Returns values of adjacent stones"""
        location = [(row+a[0], col+a[1]) for a in [(-1, 0), (1, 0), (0, -1), (0, 1)] if ((0 <= row+a[0] < board.size) and (0 <= col+a[1] < board.size))]
        return [board.board[a[0]][a[1]] for a in location]


def group_maintanence(move, board, player):
    """Creates and removes groups. Adds stone to existing group """
    pass
