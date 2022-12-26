# import pexpect
import subprocess

def start_engine():
    print('Game started:')
    game =  subprocess.Popen(['gnugo', '--mode', 'gtp'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    game.stdin.write(user_move())
    output = game.stdout.read()
    print(output.decode())

def parse(s=None):
    if s is None:
        return
    s.decode("utf-8")
    return 'tomato'.encode('utf8')


def move(game):
    game.stdin.write(user_move())
    # game.communicate(user_move())

def show_board(game):
    print(game.stdin.write('showboard'.encode('utf8')))


def user_move():
    return ( 'play' + input("Enter move: ")).encode()

def cpu_move():
    return subprocess.run('genmove')

def valid_move():
    pass

def game_over(move, move_prev):
    if move == PASS and prev_move == PASS:
        return True
    return False
