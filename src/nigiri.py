# nigiri.py
# nigiri is a Japanese go term (from the Japanese, lit. "grab", "grasp", "squeeze") adopted into English, referring to the procedure common in Japan at the beginning of an even game to decide who will play as black.
import random

WHITE = 1
BLACK = - WHITE

def nigiri():
    """Returns black or white."""
    if random.randint(0, 1) == 0:
        return nigiri0()
    return nigiri1()


def nigiri0():
    """nigiri where user guesses"""
    guess = int(input("Even (2) or odd (1)?: " ))
    stones = random.randint(1, 10)
    choice = ('even' if guess == 2 else 'odd')
    print(f'You guessed {choice} and the number was {stones}')
    if stones % 2 == guess % 2:
        color = input("Would you like to play as black (b) or as white (w)?: " )
    else:
        color = random.choice(('white', 'black'))
        print(f"The computer has chosen {color}")
    return BLACK if color[0] == 'b' or 'B' else WHITE


def nigiri1():
    """nigiri where cpu guesses"""
    stones = int(input("How many stones would you like to grab?: " ))
    guess = random.randint(1, 2)
    choice = ('even' if guess == 2 else 'odd')
    print(f'The computer guessed {choice} and the number was {stones}')
    if stones % 2 != guess % 2:
        color = input("Would you like to play as black (b) or as white (w)?: " )
    else:
        color = random.choice(('white', 'black'))
        print(f"The computer has chosen {color}")
    return BLACK if color[0] == 'b' or 'B' else WHITE
