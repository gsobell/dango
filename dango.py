#!/usr/bin/env python3
# from goban import Board
# from groups import *
# from goban import Board
# from nigiri import nigiri
# from game import *
from sys import argv, exit
import curses
from curses import wrapper

BLACK = -1
EMPTY = 0
WHITE = 1
SIZE = 19
MARGIN_X = 3
MARGIN_Y = 1
MESSAGE = (SIZE + 2, 2)
EMPTY = '·'
STONE = '●'
SPACE = ' '

"""note that implementing curses will have breaking changes on API
this is also an opportunity to fix previous bad choices"""


def show_usage():
    print("dango.py")
    print("a goban for your terminal")
    print("usage: python dango.py [options]")
    print("Options:")
    print(" -s,  --size     board size")
    print(" -k,  --komi     game komi")
    print(" -h,  --help     display this help message")
    print(" -v,             print version number.")
    print(" -a,  --about    about dango")
    print(" -c,  --controls print version number.")
    print(" -l,             show licence.")


def flag_error():
    print("One or more arguments are invalid.")
    show_usage()
    exit()


def about():
    print("""
       dango

    \033[0;30;43m 🮢 · · · · \033[0m
    \033[0;30;43m · \033[0;31;43m●\033[0;30;43m · · · \033[0m
    \033[0;30;43m · · \033[0;37;43m●\033[0;30;43m · · \033[0m
    \033[0;30;43m · · · \033[0;32;43m●\033[0;30;43m · \033[0m
    \033[0;30;43m · · · ·🮡  \033[0m

    issue or bug?
 @gsobell on github
    """)


# Check if flags present
i = 1
while i < len(argv):
    arg = argv[i]
    if arg == "-h" or arg == "--help":
        show_usage()
        exit()
    elif arg == "-v":
        print("version 0.4.0")
        exit()
    elif arg == "-a" or arg == "--about":
        about()
        exit()
    elif arg == "-l":
        print("Under GPL3 licence.\n \
Full license distribuited \
with copy of software")
        exit()
    elif arg == "-c" or arg == "controls":
        print("""Use vim or arrow keys to move,
space or enter to place a stone.
You can also use your mouse, double click to place a stone""")
        exit()
    try:
        if arg == "-s" or arg == "--pads":
            SIZE = int(argv[i+1])
            if SIZE < 1 or SIZE > 19:
                raise ValueError
            MESSAGE = (SIZE + 2, 2)
        if arg == "-k" or arg == "--komi":
            KOMI = float(argv[i+1])
            if KOMI < 0:
                raise ValueError
    except ValueError:
        flag_error()
    i += 1


def curses_setup(stdscr):
    """Sets up the screen and paints the pond blue"""
    stdscr.clear()   # Clear the screen
    curses.noecho()  # Turn off echoing of keys
    curses.cbreak()  # Turn off normal tty line buffering
    stdscr.keypad(True)   # Enable keypad mode
    curses.mousemask(True)
    curses.curs_set(0)    # Hide cursor
    curses.start_color()  # Enable colors if supported
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)  # board B
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_YELLOW)  # board W
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)   # select B
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)   # select W
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)   # background
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_RED)     # error
    stdscr.bkgd(' ', curses.color_pair(5))
    stdscr.refresh()


def place_piece(y, x, color, stones, stdscr):
    """recieves curses (y,x) and draws on board.
    also handle group capture as needed."""
    if color is WHITE:
        stdscr.addstr(y, x, STONE + SPACE, curses.color_pair(2))
        stones.white.append((y, x))
    if color is BLACK:
        stdscr.addstr(y, x, STONE + SPACE, curses.color_pair(1))
        stones.black.append((y, x))
    # for k in stones.adjacent(y, x):  # removal of groups!
    #     if (k in stones.white) or (k in stones.black):
    #         liberty = False
    #         group = [k]
    #         visited = [k]
    #         to_check = [k for k in stones.adjacent(*k) if k not in visited]
    #         while to_check:
    #             curr = to_check.pop()
    #             if curr == 0:
    #                 liberty =  True
    #                 break
    #             elif ((curr in stones.white and k in stones.white) or
    #                     (curr in stones.black and k in stones.black)):
    #                 visited.append(k)
    #                 to_check.append([k for k in stones.adjacent(*k)
    #                                  if k not in visited])
    #                 group.append(k)
    #             else:
    #                 visited.append(k)
    #             if not liberty:
    #                 stones.remove(group, stdscr)
    stdscr.refresh()


class Stones:
    def __init__(self):
        """Stones reflect (y,x) cordinates of curses board.
        All methods must be cordinate offset agnostic."""
        self.white = []
        self.black = []
        self.empty = [(y, x) for y in range(1, SIZE + 1) for x in range(1, SIZE*2 +1)]
        self.total = set(self.empty)  # immutable

    def legal_placement(self, y, x, color) -> bool:
        if (y, x) in self.white or (y, x) in self.black:
            return False
        return True

    def remove(self, to_remove, stdscr) -> None:
        """Removes group from board containing stone (y, x)"""
        to_remove = set(to_remove)
        self.white = list(set(self.white) - to_remove)
        self.black = list(set(self.black) - to_remove)
        for stone in to_remove:
            stdscr.addstr(stone[0], stone[1], EMPTY, curses.color_pair(1))

    def adjacent(self, y, x):
        a = [(y + 1, x), (y - 1, x),
             (y, x + 1), (y, x - 1)]
        return list(set(a) & set(self.total))

    def player_color(self, y, x, color):
        if ((y, x) in self.white) or color == 1:
            return self.white, self.black
        elif ((y, x) in self.black) or color == -1:
            return self.black, self.white

    def liberty_count(self, y, x, color=0):
        """Receives (y, x), returns libery count for group it has
        Color is non-zero if piece needs to be checked before placement"""
        same, other = self.player_color(y, x, color)
        liberties = 0
        to_check = self.adjacent(y, x)
        checked = []
        while to_check:
            curr = to_check.pop()
            if curr in same:
                if [k for k in self.adjacent(*curr) if k not in checked]:
                    to_check.append([k for k in self.adjacent(*curr)
                                    if k not in checked])
            elif curr in other:
                pass  # for logical clarity, make concise later
            else:
                liberties += 1
            checked.append(curr)
        return liberties


def draw_A1(stdscr):
    for k in range(0, SIZE):
        if k < 8:  # A1 scheme does not have 'i' to avoid confusion
            stdscr.addstr(0, k*2 + MARGIN_X, chr(65 + k), curses.color_pair(5))
            stdscr.addstr(SIZE + 1, k*2 + MARGIN_X,
                          chr(65 + k), curses.color_pair(5))
        if k >= 8:
            stdscr.addstr(0, k*2 + MARGIN_X,
                          chr(65 + k + 1), curses.color_pair(5))
            stdscr.addstr(SIZE + 1, k*2 + MARGIN_X,
                          chr(65 + k + 1), curses.color_pair(5))
    for k in range(0, SIZE):
        stdscr.addstr(k + 1, 0,  f"{str(SIZE - k):>2}", curses.color_pair(5))
        stdscr.addstr(k + 1, SIZE * 2 + MARGIN_X + 1,
                      f"{str(SIZE - k):<2}", curses.color_pair(5))


def draw_board(stdscr):
    for j in range(1, SIZE + 1):
        for k in range(1, SIZE + 1):
            stdscr.addstr(j, k*2 + 1, EMPTY + SPACE, curses.color_pair(1))
            stdscr.addstr(j, k*2 + 1, EMPTY + SPACE, curses.color_pair(1))


def get_move(c, y, x, stdscr):
    """Given y, x, getch(), returns the new (y, x) or None if no change"""
    if c == curses.KEY_LEFT or c == ord('h'):
        x -= 2
        if x > SIZE*2:
            x = MARGIN_X
        if x < MARGIN_X:
            x = SIZE*2 + 1
    elif c == curses.KEY_RIGHT or c == ord('l'):
        x += 2
        if x > SIZE*2 + 2:
            x = MARGIN_X
        if x < MARGIN_X:
            x = SIZE*2 + 1
    elif c == curses.KEY_UP or c == ord('k'):
        y -= 1
        if y > SIZE:
            y = 1
        if y < 1:
            y = SIZE
    elif c == curses.KEY_DOWN or c == ord('j'):
        y += 1
        if y > SIZE:
            y = 1
        if y < 1:
            y = SIZE
    else:
        stdscr.addstr(y, x, EMPTY, curses.color_pair(6))
        stdscr.addstr(SIZE + 1, 3, "Not a valid input key",
                      curses.color_pair(6))
    return (y, x)


def draw_cursor(new_cursor, old_cursor, stones, stdscr):
    """Draws the new cursor, and returns old cursor to bg color"""
    y, x = new_cursor
    if old_cursor in stones.white:
        stdscr.chgat(*old_cursor, 2, curses.color_pair(2))
    else:
        stdscr.chgat(*old_cursor, 2, curses.color_pair(1))
    if (y, x) in stones.white:
        stdscr.chgat(y, x, 2, curses.color_pair(4))
    else:
        stdscr.chgat(y, x, 2, curses.color_pair(3))


def error_out(stdscr, message):
    stdscr.addstr(*MESSAGE, message, curses.color_pair(6))
    stdscr.refresh()


def standard_out(stdscr, message):
    stdscr.addstr(*MESSAGE, message, curses.color_pair(5))
    stdscr.refresh()


def clear_message(stdscr):
    """Clears the previous message"""
    for k in range(curses.COLS - 1):
        stdscr.addstr(MESSAGE[0], k, " ",
                      curses.color_pair(5))  # clear curr message
    stdscr.refresh()


def play(stdscr):
    stones = Stones()
    color = -1
    curses_setup(stdscr)
    draw_A1(stdscr)
    draw_board(stdscr)
    stdscr.getch()
    y, x = 3, SIZE*2 - 3  # top right corner
    # pass_count = 0
    # error_count = 0  # show help after 3 errors
    while "game loop":
        while "input loop":
            old_cursor = y, x
            c = stdscr.getch()
            clear_message(stdscr)  # after getch(), so can be read
            if c == 10 or c == ord(" "):
                if stones.legal_placement(y, x, color):
                    place_piece(y, x, color, stones, stdscr)
                    color *= -1
                else:
                    error_out(stdscr, "Not a valid move")
                    break
            elif c == ord(":"):
                pass  # vim style command in
            elif c == ord("P") or c == ord("p"):
                standard_out(stdscr, "Pass.")
                color *= -1
            elif c == curses.KEY_MOUSE:
                click = curses.getmouse()
                if (1 < click[2] <= SIZE) and (MARGIN_X <= click[1] + click[1] % 2 - 1 < SIZE * 2 + MARGIN_X):
                    x = click[1] + click[1] % 2 - 1
                    y = click[2]
                    if (old_cursor[0] == y) and (x <= old_cursor[1] <= x + 1):
                        if stones.legal_placement(y, x):
                            place_piece(y, x, color, stones, stdscr)
                            color *= -1
                        else:
                            error_out(stdscr, "Not a valid move")
                            break
                else:
                    error_out(stdscr, "Not a valid place to click")
            else:
                y, x = get_move(c, y, x, stdscr)
            draw_cursor((y, x), old_cursor, stones, stdscr)
            stdscr.refresh()


if __name__ == "__main__":
    try:
        wrapper(play)
    except KeyboardInterrupt:
        print('Thank you for the game.')
