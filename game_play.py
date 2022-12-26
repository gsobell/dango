#!/usr/bin/env python3
def board_update(move, board, player):
    """Recieves a board and a move, returns the resultant board"""
    col, row = move_to_coord(move, board)
    # col = int(move.current[0]) - 1
    # row = int(move.current[1]) - 1
    board.board[col][row] = player.current


def is_valid_move(move, board) -> bool:
    """Checks if spot is occupied or violates ko rule"""
    if move.current == 'PASS' or move.current == 'pass':
        return True
    col, row = move_to_coord(move, board)
    # col = int(move.current[0]) - 1
    # row = int(move.current[1]) - 1
    if board.board[col][row] != 0:
        return False
    # if move.current in move.last_3:
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
    col = int(col) -1
    return col, row

def game_not_over(move):
    """Only duplicate move allowed is pass"""
    if move.last_3[1] == move.last_3[2]:
        return True







