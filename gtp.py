from subprocess import Popen, PIPE
size = 19 # change when passes unit tests
komi = 6.5

def __init__(self):

def start_engine(size):
    print(f"Starting gnugo.")
    engine = Popen(['gnugo', '--mode', 'gtp'], stdin=PIPE, stdout=PIPE)
    engine_write(engine, f"boardsize {size}")
    print(engine_read(engine))
    engine_write(engine, f"komi {komi}")


def engine_write(engine, msg: str):
    msg = str(msg + '\n').encode('utf-8')
    engine.stdin.write(msg)
    engine.stdin.flush()

def engine_read(engine):
    """For GTP protocol, the  out stream
    must be advanced one '\n' each iter"""
    out = engine.stdout.readline().decode()
    engine.stdout.flush()
    engine.stdout.readline()
    return out

def engine_close(engine):
    engine.stdin.close()
    print('Waiting for engine to exit')
    engine.wait()
    if str(engine.returncode) == '0':
        print('Closed successfully.')
        return
    print('Clossed with errors.')


def genmove(engine, player):
    msg = f"genmove {'W' if player == 1 else 'B'}"
    engine_write(engine, msg)
    move = engine_read(engine)
    A1 = ''
    for char in move:
        if char.isalnum():
            A1 += char
    return A1 # returns move in A1 format


def play(engine, player, move):
    msg = f"play {'W' if player == 1 else 'B'} {move}"
    engine_write(engine, msg)
    out = engine_read(engine)
    if '?' in out:
        return False
    return True


start_engine(size)
