#!/usr/bin/env python3
from subprocess import Popen, PIPE
from goban import Board


class User:
    def __init__(self, color, val):
        self.user = 'user'
        self.color = color
        self.val = val

    def genmove():
        # returns move in A1 format
        pass

    def play():
        # not necessary for user, sees board
        pass

    def turn(self, board, move):
        print(f" {self.color.capitalize()} to play.")
        move.update(input(' Enter move: '))
        if move.current == 'PASS' or move.current == 'pass':
            return
        elif move.current == ':q':
            exit()  # does not exit quietly
        elif is_valid_move(move.current, board, self.val):
            board_update(move.current, board, self.val)
        else:
            print('Invalid Move.')


class Engine:
    def __init__(self, size, komi, color, val):
        self.engine = Popen(['gnugo', '--mode', 'gtp'],
                            stdin=PIPE, stdout=PIPE)
        self.write(f"boardsize {size}")
        self.write(f"komi {komi}")
        self.color = color
        self.val = val

    def write(self, msg: str):
        msg = str(msg + '\n').encode('utf-8')
        self.engine.stdin.write(msg)
        self.engine.stdin.flush()

    def read(self):
        """For GTP protocol, the  out stream
        must be advanced one '\n' each iter"""
        out = self.engine.stdout.readline().decode()
        self.engine.stdout.flush()
        self.engine.stdout.readline()
        return out

    def close(self):
        self.engine.stdin.close()
        print('Waiting for self.engine to exit')
        self.engine.wait()
        if str(self.engine.returncode) == '0':
            print('Closed successfully.')
            return
        print('Clossed with errors.')

    def genmove(self):
        msg = f"genmove {'W' if self.color == 'white' else 'B'}"
        self.write(msg)
        move = self.read()
        A1 = ''
        for char in move:
            if char.isalnum():
                A1 += char
        return A1  # returns move in A1 format, or "PASS"

    def play(self, move):
        msg = f"play {'W' if self.color != 'white' else 'B'} {move}"
        self.write(msg)
        out = self.read()
        if '?' in out:
            return False
        return True

    def turn(self, board, move):
        """Updates engine with previous move,
        and generates a new move"""
        print(f"{self.color.capitalize()} to play.")
        if move.last:
            self.play(move.last)
        gen = self.genmove()
        if gen == 'PASS' or gen == 'pass':
            return
        move.update(gen)
        board_update(gen, board, self.val)


# def engine_setup(engine, size, komi):
#     print("Starting gnugo.")
#     engine.write(f"boardsize {size}")
#     print(engine.read())
#     engine.write(f"komi {komi}")
#     print(engine.read())


def game_setup():
    """Asks user for game parameters"""
    print("""
       dango

    \033[0;30;43m 🮢 · · · · \033[0m
    \033[0;30;43m · \033[0;31;43m●\033[0;30;43m · · · \033[0m
    \033[0;30;43m · · \033[0;37;43m●\033[0;30;43m · · \033[0m
    \033[0;30;43m · · · \033[0;32;43m●\033[0;30;43m · \033[0m
    \033[0;30;43m · · · ·🮡  \033[0m
    """)
    while True:
        size, komi = 19, 6.5
        size = input('What size board?: ')
        if size.isnumeric():
            size = int(size)
            if 0 < size <= 19:
                break
        print('Please enter a number between 1 and 19.')
    while True:
        komi = input('How many komi?: ')
        if komi.isnumeric():
            komi = float(komi)
            break
        print('Please enter a valid number.')
    while True:
        num = input('How many [human] players? (0, 1 or 2) ')
        if num == '2':
            return Board(size), Move(), User('black', -1), User('white', 1)
        elif num == '1':
            return Board(size), Move(), User('black', -1), Engine(size, komi, 'white', 1)
        elif num == '0':
            return Board(size), Move(), Engine(size, komi, 'black', -1), Engine(size, komi, 'white', 1)


class Move:
    def __init__(self):
        self.current = None
        self.last = None
        self.hist = set()

    def update(self, user_move):
        self.last = self.current
        self.current = user_move
        self.hist.add(user_move)


def board_update(move, board, player):
    """Receives a board and a move, returns the resultant board"""
    row, col = move_to_coord(move, board)
    board.board[row][col] = player
    capture(row, col, -player, board)


def is_valid_move(move, board, player) -> bool:
    """Checks if spot is occupied or violates ko rule"""
    if move.upper() == 'PASS':
        return True
    row, col = move_to_coord(move, board)
    if board.board[row][col] != 0:
        return False
    if is_self_atari(move, board, player):
        return False
    return True


def move_to_coord(move, board):
    row = ''
    for k in move:
        if k.isupper():
            col = int('ABCDEFGHJKLMNOPQRST'.find(k))
        if k.islower():
            col = int('abcdefghjklmnopqrst'.find(k))
        elif k.isnumeric():
            row += k
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
                print("Group is this long")
                print(len(group))
                if player == 1:
                    board.black_captures += len(group)
                else:
                    board.white_captures += len(group)
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
    if (player and 0) not in values:
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


def clear():
    from os import system, name
    if name != 'nt':
        _ = system('clear')
    else:
        _ = system('cls')
    print('\033[0m')
