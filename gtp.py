from subprocess import Popen, PIPE
size = 19 # change when passes unit tests
komi = 6.5

class Engine:
    def __init__(self):
        self.engine = Popen(['gnugo', '--mode', 'gtp'], stdin=PIPE, stdout=PIPE)

    def write(self, msg: str):
        msg = str(msg + '\n').encode('utf-8')
        self.engine.stdin.write(msg)
        self.engine.stdin.flush()

    def read(self):
        """For GTP protocol, the  out stream
        must be advanced one '\n' each iter"""
        out = self.engine.stdout.readline().decode()
        self.engine.stdout.flush()
        self.engine.stdout.readline()
        return out

    def close(self):
        self.engine.stdin.close()
        print('Waiting for self.engine to exit')
        self.engine.wait()
        if str(self.engine.returncode) == '0':
            print('Closed successfully.')
            return
        print('Clossed with errors.')

    def genmove(self, player):
        msg = f"genmove {'W' if player == 1 else 'B'}"
        self.write(msg)
        move = self.read()
        A1 = ''
        for char in move:
            if char.isalnum():
                A1 += char
        return A1 # returns move in A1 format


    def play(self, player, move):
        msg = f"play {'W' if player == 1 else 'B'} {move}"
        self.write(msg)
        out = self.read()
        if '?' in out:
            return False
        return True

def setup(engine, size):
    print(f"Starting gnugo.")
    engine.write(f"boardsize {size}")
    print(engine.read())
    engine.write(f"komi {komi}")
    print(engine.read())

gnugo = Engine()
setup(gnugo, 19)
print(gnugo.genmove(1))
gnugo.play(1, 'A1')
print(gnugo.genmove(1))
