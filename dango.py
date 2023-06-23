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


def logo():
    print("""
       dango

    \033[0;30;43m 🮢 · · · · \033[0m
    \033[0;30;43m · \033[0;31;43m●\033[0;30;43m · · · \033[0m
    \033[0;30;43m · · \033[0;37;43m●\033[0;30;43m · · \033[0m
    \033[0;30;43m · · · \033[0;32;43m●\033[0;30;43m · \033[0m
    \033[0;30;43m · · · ·🮡  \033[0m
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
        logo()
        print("    issue or bug? \n @gsobell on github")
        exit()
    elif arg == "-l":
        print("Under GPL3 licence.\n \
Full license distribuited \
with copy of software")
        exit()
    elif arg == "-c" or arg == "controls":
        print("""Use vim or arrow keys to move,
space or enter to place a stone.
You can also use your mouse, double click to place a stone.
'p' to pass, 'u' to undo.""")
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
    stdscr.keypad(True)     # Enable keypad mode
    curses.mousemask(True)  # Enable mouse event reporting
    curses.curs_set(0)      # Hide cursor
    curses.start_color()    # Enable colors if supported
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)  # board B
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_YELLOW)  # board W
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)   # select B
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)   # select W
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)   # background
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_RED)     # error
    curses.init_pair(7, curses.COLOR_RED, curses.COLOR_YELLOW)    # logo
    curses.init_pair(8, curses.COLOR_GREEN, curses.COLOR_YELLOW)  # logo
    stdscr.bkgd(' ', curses.color_pair(5))
    stdscr.refresh()


def place_piece(y, x, color, stones, moves, captures, stdscr):
    """recieves curses (y,x) and draws on board.
    also handle group capture as needed."""
    if color is WHITE:
        stdscr.addstr(y, x, STONE + SPACE, curses.color_pair(2))
        stones.white.append((y, x))
    if color is BLACK:
        stdscr.addstr(y, x, STONE + SPACE, curses.color_pair(1))
        stones.black.append((y, x))
    if (y, x) in stones.empty:
        stones.empty.remove((y, x))
    captured = stones.capture_check(y, x, color)
    if captured:
        for k in captured:
            captures.append(k)
            stones.remove(stdscr, k)
    else:
        captures.append(None)
    moves.append((y, x))
    stdscr.refresh()


def replace_piece(y, x, color, stones, moves, captures, stdscr):
    """Stone placement of `n`, where stones.black and stones.white
are not changed, and no capture is done"""
    if color is WHITE:
        stdscr.addstr(y, x, STONE + SPACE, curses.color_pair(2))
    elif color is BLACK:
        stdscr.addstr(y, x, STONE + SPACE, curses.color_pair(1))
    elif color is EMPTY:
        stdscr.addstr(y, x, EMPTY + SPACE, curses.color_pair(1))
    stdscr.refresh()


class Stones:
    def __init__(self):
        """Stones reflect (y,x) cordinates of curses board.
        All methods must be cordinate offset agnostic."""
        self.white = []
        self.black = []
        self.empty = [(y, x) for y in range(1, SIZE + 1)
                      for x in range(3, SIZE*2 + 2)]  # updated if capture
        self.total = set(self.empty)  # immutable

    def legal_placement(self, y, x, color, captures) -> bool:
        if (y, x) in self.white or (y, x) in self.black:
            return False
        if self.capture_check(y, x, color):
            if self.is_ko(y, x, color, captures):
                return False
            return True
        return self.liberty_count(y, x, color)

    def is_ko(self, y, x, color, captures) -> bool:
        last_capture = captures[-1] if captures else None
        if last_capture and len(last_capture) == 1 and (y, x) in last_capture:
            return True
        return False


    def capture_check(self, y, x, color):
        """Checks if playing color at (y, x) captures neighbor
        (any neighbor has one remaining liberty)"""
        if color == WHITE:
            same = self.white
            other = self.black
        else:
            same = self.black
            other = self.white
        captured = []
        stones = [k for k in self.adjacent(y, x) if k in other]
        for stone in stones:
            q = [k for k in self.adjacent(*stone) if k != (y, x)]
            count = 0
            visited = [(y, x), stone]
            while q:
                curr = q.pop()
                visited.append(curr)
                if curr in other:
                    q.extend([k for k in self.adjacent(*curr)
                              if k not in visited])
                    continue
                elif curr in same:
                    continue
                elif curr in self.empty:
                    count += 1
            if not count:
                captured.append([k for k in visited if k in other])
        return captured if captured else None

    def liberty_count(self, y, x, color) -> int:
        """True if group @color including @(y,x) has liberties"""
        checked = [(y, x)]
        count = 0
        same = self.white if color == WHITE else self.black
        q = self.adjacent(y, x)
        while q:
            curr = q.pop()
            checked.append(curr)
            if curr in self.empty:
                count += 1
            elif curr in same:
                q.extend([k for k in
                          self.adjacent(curr[0], curr[1])
                          if k not in checked])
            else:
                continue
        return count

    def remove(self, stdscr, to_remove) -> None:
        """Removes group from board containing stone (y, x)"""
        self.empty.extend(to_remove)
        to_remove = set(to_remove)
        self.white = list(set(self.white) - to_remove)
        self.black = list(set(self.black) - to_remove)
        for stone in to_remove:
            stdscr.addstr(stone[0], stone[1], EMPTY, curses.color_pair(1))

    def adjacent(self, y, x):
        a = [(y + 1, x), (y - 1, x),
             (y, x + 2), (y, x - 2)]
        return list(set(a) & set(self.total))

    def player_color(self, y, x, color):
        if ((y, x) in self.white) or color == 1:
            return self.white, self.black
        elif ((y, x) in self.black) or color == -1:
            return self.black, self.white


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
        # stdscr.chgat(y, x, 2, curses.color_pair(6))
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


def yx_to_a1(y, x):
    return int(x/2), 20 - y


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
    curses_setup(stdscr)
    moves = []     # moves (y,x), for undo. None if pass
    captures = []  # list of stones removed, per move
    n_toggle = 0
    stones = Stones()
    color = -1
    draw_A1(stdscr)
    draw_board(stdscr)
    stdscr.getch()
    y, x = 3, SIZE*2 - 3  # top right corner
    while "game loop":
        while "input loop":
            old_cursor = y, x
            c = stdscr.getch()
            clear_message(stdscr)  # after getch(), so can be read
            if c == 10 or c == ord(" "):
                if stones.legal_placement(y, x, color, captures):
                    place_piece(y, x, color, stones, moves, captures, stdscr)
                    moves.append((y, x))
                    color *= -1
                else:
                    error_out(stdscr, "Not a valid move")
                    break
            elif c == curses.KEY_MOUSE:
                click = curses.getmouse()
                if (1 <= click[2] <= SIZE) and (MARGIN_X <=
                                                click[1] +
                                                click[1] % 2 - 1 <
                                                SIZE * 2 + MARGIN_X):
                    x = click[1] + click[1] % 2 - 1
                    y = click[2]
                    if ((old_cursor[0] == y) and (x <=
                                                  old_cursor[1] <= x + 1)):
                        if stones.legal_placement(y, x, color, captures):
                            place_piece(y, x, color, stones,
                                        moves, captures, stdscr)
                            moves.append((y, x))
                            color *= -1
                        else:
                            error_out(stdscr, "Not a valid move")
                            break
                else:
                    error_out(stdscr, "Not a valid place to click")
            elif c == ord(":"):
                pass  # vim style command in
            elif c == ord("P") or c == ord("p"):
                standard_out(stdscr, "Pass.")
                moves.append(None)
                captures.append(None)
                color *= -1
            elif c == ord("N") or c == ord("n"):  # toggle kifu
                if not moves:
                    break
                if n_toggle:
                    for group in captures:  # redraw captures first
                        if group:
                            for move in group:
                                replace_piece(move[0], move[1], EMPTY,
                                              stones, moves, captures, stdscr)
                    for move in moves:
                        if (not move) or (move in stones.empty):
                            continue
                        if move in stones.white:
                            replace_piece(move[0], move[1], WHITE,
                                          stones, moves, captures, stdscr)
                        if move in stones.black:
                            replace_piece(move[0], move[1], BLACK,
                                          stones, moves, captures, stdscr)
                    n_toggle = 0
                else:
                    i = 1
                    for move in moves:
                        if move in stones.black:
                            stdscr.addstr(move[0], move[1], str(i),
                                          curses.color_pair(1))
                        elif move in stones.white:
                            stdscr.addstr(move[0], move[1], str(i),
                                          curses.color_pair(2))
                        else:  # captured stones
                            stdscr.addstr(move[0], move[1], str(i),
                                          curses.color_pair(7))
                        i += 1
                    n_toggle = 1
            elif c == ord("U") or c == ord("u"):
                standard_out(stdscr, "Undo.")
                if not moves:
                    error_out(stdscr, "No move to undo.")
                    break
                undo = moves.pop()
                replace = captures.pop()
                if undo:
                    stones.empty.append(undo)
                    stdscr.addstr(undo[0], undo[1], EMPTY +
                                  SPACE, curses.color_pair(1))
                    if undo in stones.white:
                        stones.white.remove(undo)
                        if replace:
                            for piece in replace:
                                place_piece(piece[0], piece[1], BLACK,
                                            stones, moves, captures, stdscr)
                    elif undo in stones.black:
                        stones.black.remove(undo)
                        if replace:
                            for piece in replace:
                                place_piece(piece[0], piece[1], WHITE,
                                            stones, moves, captures, stdscr)
                    else:
                        standard_out(stdscr, "Undo pass.")
                color *= -1
            else:
                y, x = get_move(c, y, x, stdscr)
            draw_cursor((y, x), old_cursor, stones, stdscr)
            # A1 = yx_to_a1(y, x)
            # standard_out(stdscr, f"cords are: {A1}")
            # standard_out(stdscr, f"click is: {click}")
            # standard_out(stdscr, f"(y,x) is: {y, x}")
            standard_out(stdscr,f"{'White' if color == 1 else 'Black'} to play.")
            stdscr.refresh()


if __name__ == "__main__":
    try:
        wrapper(play)
    except KeyboardInterrupt:
        print('Thank you for the game.')
    # except:
        # print("Something went wrong. Let us know, we'll try to fix it!")
