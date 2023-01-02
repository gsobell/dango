#!/usr/bin/env python3
def board_update(move, board, player, stones):
    """Recieves a board and a move, returns the resultant board"""
    row, col = move_to_coord(move, board)
    board.board[row][col] = player.current
    stones.add(move, player.current)
    capture(row, col, -player.current, board)


def is_valid_move(move, board, player) -> bool:
    """Checks if spot is occupied or violates ko rule"""
    if move.current.upper() == 'PASS':
        return True
    row, col = move_to_coord(move, board)
    if board.board[row][col] != 0:
        return False
    if is_self_atari(move, board, player):
        return False
    return True


def move_to_coord(move, board):
    row = ''
    for k in move.current:
        if k.isupper():
            col = int('ABCDEFGHJKLMNOPQRST'.find(k))
        if k.islower():
            col = int('abcdefghjklmnopqrst'.find(k))
        elif k.isnumeric():
            row += k
        else:
            print('Not a valid move')
            return
    row = board.size - int(row)
    return row, col


def game_not_over(move):
    """Only duplicate move allowed is pass"""
    if move.last.upper() == move.current.upper() == 'PASS':
        return False
    return True


def capture(row, col, player, board):
    """Check capture upon stone placement of adjacent groups
    Parameters:
    row, col: starting point
    player: color of group we are checking if alive
    chain: list chain to capture, if it has no liberties"""
    locations, values = adjacent(row, col, board)
#   Checking the four surrounding values:
    for loc, val in zip(locations, values):
        if val == (-player or 0):
            continue
        if val == player:
            group = recursive_capture(loc[0], loc[1], player, board, [loc])
            if group:
                for location in group:
                    board.board[location[0]][location[1]] = 0
                group = []


def recursive_capture(row, col, player, board, visited):
    """Using DFS to visit all stones in group"""
    locations, values = adjacent(row, col, board)
    if 0 in values:
        return False
    for loc, val in zip(locations, values):
        """Halting condition is when every cell
        is surounded by other or visited"""
        if (val == -player) or (loc in visited):
            continue
        visited.append(loc)
        visited = recursive_capture(loc[0], loc[1], player, board, visited)
    return visited


def is_self_atari(move, board, player):
    """Makes sure stone placement isn't self atari  to the group
    Parameters:
    row, col: starting point
    player: color of group we are checking if alive"""
    row, col = move_to_coord(move, board)
    locations, values = adjacent(row, col, board)
    # print(adjacent)
    if 0 in values:
        return False
    if (player.current and 0) not in values:
        return True
    for loc, val in zip(locations, values):
        if val == player:
            if recursive_capture(loc[0], loc[1], player, board, [loc]):
                return True
    return False


def adjacent(row, col, board):
    location = [(row+a[0], col+a[1])
                for a in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if ((0 <= row+a[0] < board.size) and
                    (0 <= col+a[1] < board.size))]
    values = [board.board[a[0]][a[1]] for a in location]
    return location, values
