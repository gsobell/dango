#!/usr/bin/env python3
def board_update(move, board, player):
    """Recieves a board and a move, returns the resultant board"""
    col, row = move_to_coord(move, board)
    board.board[col][row] = player.current


def is_valid_move(move, board) -> bool:
    """Checks if spot is occupied or violates ko rule"""
    if move.current.upper() == 'PASS':
        return True
    col, row = move_to_coord(move, board)
    if board.board[col][row] != 0:
        return False
    # if not is_alive(move, board):
        # return False
    return True


def move_to_coord(move, board):
    col = ''
    for k in move.current:
        if k.isupper():
            row = int('ABCDEFGHJKLMNOPQRST'.find(k))
        if k.islower():
            row = int('abcdefghjklmnopqrst'.find(k))
        elif k.isnumeric():
            col += k
        else:
            print('Not a valid move')
            return
    col = int(col) - 1
    return col, row


def game_not_over(move):
    """Only duplicate move allowed is pass"""
    if move.last.upper() == move.current.upper() == 'PASS':
            return False
    return True

def if_alive(move, board, player):
    """Recursive check of life/death upon stone placement - Recursive """
    col, row = move_to_coord(move, board)
    adjacent = [(row+a[0], col+a[1]) for a in
                    [(-1,0), (1,0), (0,-1), (0,1)]
                    if ( (0 <= x+a[0] < board.size) and (0 <= y+a[1] < board.size))]
    print(col, row)
    print(adjacent)
    if 0 in adjacent:
        return True
    if current.player not in adjacent:
        return False
    return True
    return recursive_check()

def if_legal(move, board):
    """Makes sure stone placement isn't suicidal to the group"""


def recursive_check():
    """Given a move, a color to check, and a board, it will check if the group is alive"""
    pass





