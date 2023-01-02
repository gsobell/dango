BLACK = -1
EMPTY = 0
WHITE = 1
SIZE = 19


class Color:
    def __init__(self):
        self.white = '\033[0;37;43m'
        self.black = '\033[0;30;43m'
        self.goban = '\033[0;30;43m'
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
        self.current = 'sente'
        self.last = 'gote'
        self.hist = set()

    def update(self, user_move):
        self.last = self.current
        self.current = user_move
        self.hist.add(user_move)


def clear():
    from os import system, name
    if name != 'nt':
        _ = system('clear')
    else:
        _ = system('cls')
    print(color.normal)


# initialize backend classes here
color = Color()
goban = Goban()
player = Player()
