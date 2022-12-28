#!/usr/bin/env python3
def board_update(move, board, player):
    """Recieves a board and a move, returns the resultant board"""
    col, row = move_to_coord(move, board)
    board.board[col][row] = player.current


def is_valid_move(move, board, player) -> bool:
    """Checks if spot is occupied or violates ko rule"""
    if move.current.upper() == 'PASS':
        return True
    col, row = move_to_coord(move, board)
    if board.board[col][row] != 0:
        return False
    # if not is_alive(move, board, player):
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

def is_alive(move, board, player):
    """Recursive check of life/death upon stone placement - Recursive """
    col, row = move_to_coord(move, board)
    adjacent = [(row+a[0], col+a[1])
                for a in [(-1,0), (1,0), (0,-1), (0,1)]
                if ( (0 <= row+a[0] < board.size) and (0 <= col+a[1] < board.size))]
    # print(col, row)
    # print('move ^')
    # print(adjacent)
    # print('left, right, up, down^')
    # print(player.current)
    # print('player ^')
    collect = []
    for a in adjacent:
        collect.append(board.board[a[0]][a[1]])
    # print(adjacent)
    # print('left, right, up, down^')
    if 0 in collect: # random 0s appear in the collection, don't know why..'
        return True
    if player.current not in collect:
        return False
    return recursive_check()

def is_legal(move, board):
    """Makes sure stone placement isn't suicidal to the group"""


def recursive_check(start, find):
    """Given a move, a color to check, and a board, it will check if the group is alive"""
    return True





