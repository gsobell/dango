import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

echo()

def get_input():
    getch()


def uncurse():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()


