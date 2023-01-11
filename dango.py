#!/usr/bin/env python3
from goban import Board
from resources import *
from gtp import *
from groups import *
from game_play import *
# from nigiri import nigiri


def game_setup(player):
    """Asks user for game parameters"""
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
        num = input('How many [human] players? (0, 1 or 2)') # continue here
        if num == '2':
            break
        elif num == '1':
            player.user = (-1)
            break
        elif num == '0':
            player.user = (-1, 1)
            break
    return Board(size), Move(), Stones()


def game_round(board, move, stones):
    print(f"{'White' if player.current == 1 else 'Black'}'s move.")
    # if current.player not in user.player:
        # engine.play(-player.current, move.current)
        # move.update(engine.genmove())
    # else:
    move.update(input('Enter move: '))
    if move.current == 'PASS' or move.current == 'pass':
        player.switch()
        return
    if is_valid_move(move, board, player):
        board_update(move, board, player, stones)
        player.switch()
    else:
        print('Invalid Move.')


def play():
    player = Player()
    board, move, stones = game_setup(player)
    engine = Engine()
    while game_not_over(move):
        try:
            board.display()
            game_round(board, move, stones)
        except:
            input('Please try again. Press enter to continue')
        clear()
    input('Thank you for the game')
    clear()


if __name__ == "__main__":
    play()
