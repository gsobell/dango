#!/usr/bin/env python3
from goban import *
from resources import *
from gtp import *
from groups import *
from game_play import *
# from nigiri import nigiri

def game_setup():
    while True:
        SIZE = input('What size board?: ')
        if SIZE.isnumeric():
            SIZE = int(SIZE)
            if 0 < SIZE <= 19:
                break
    # KOMI = float(input('How many komi?: '))
    return Board(SIZE), Move()


def game_round(board, move):
    print(f"{'White' if player.current == 1 else 'Black'}'s move.")
    move.update(input('Enter move: '))
    if move.current == 'PASS' or move.current == 'pass':
        player.switch()
        return
    if is_valid_move(move, board, player):
        board_update(move, board, player)
        player.switch()
    else:
        print('Invalid Move.')


def play():
    board, move = game_setup()
    while game_not_over(move):
        try:
            board.display()
            game_round(board, move)
        except:
            input('Please try again. Press enter to continue')
        clear()
    input('Thank you for the game')
    clear()



if __name__ == "__main__":
     play()
