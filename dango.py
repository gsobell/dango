#!/usr/bin/env python3
from goban import *
from resources import *
from gtp import *
from game_play import *
# from nigiri import nigiri

def game_setup():
    SIZE = int(input('What size board?: '))
    # KOMI = float(input('How many komi?: '))
    return Board(SIZE)


def game_round(board):
    print(f"{'White' if player.current == 1 else 'Black'}'s move.")
    move.current = (input('Enter move: '))
    if move.current == 'PASS' or move.current == 'pass':
        player.switch()
        return
    if is_valid_move(move, board):
        board_update(move, board, player)
        # move.update()
        player.switch()
    else:
        print('Invalid Move.')

def play():
    board = game_setup()
    while True:
    # while game_not_over():
        board.display()
        game_round(board)
        clear()

play()

# if __name__ == "__main__":
    # main()
