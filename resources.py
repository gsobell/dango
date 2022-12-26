BLACK = -1
EMPTY =  0
WHITE =  1
SIZE = 19

class Color:
    def __init__(self):
        self.white  = '\033[0;37;43m'
        self.black  = '\033[0;30;43m'
        self.goban  = '\033[0;30;43m'
        self.normal = '\033[0m'

class Goban:
    def __init__(self):
        self.stone = '●'
        self.blank = '○'
        self.empty = '·'
        self.hoshi = '+'

class Player:
    def __init__(self):
        self.current = -1
        self.black = -1
        self.white = 1

    def switch(self):
        self.current *= -1

class Move:
    def __init__(self):
        self.current = None
        self.last = None

    def update(self):
        self.last = self.current


class Groups:
    """Only groups that are also chains, for simplicity"""
    def __init__(self):
        self.pointer = ''
        self.stones = []
        self.liberties = []


    def find_pointer(group):
        """Sets the uppermost leftmost stone in a group"""

def clear():
    from os import system, name
    if name != 'nt':
        _= system('clear')
    else:
        _ = system('cls')
    print(color.normal)


color = Color()
goban = Goban()
player = Player()
move = Move()
groups = Groups()
