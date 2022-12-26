#!/usr/bin/env python3
#include <ncurses.h>
import curses
SIZE = 19

def start():
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)

def end():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

start()

# program goes her



end()


