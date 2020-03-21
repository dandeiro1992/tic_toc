import sys
from time import sleep
from Game import *


if __name__ == '__main__':
    if len(sys.argv) == 2:
        game = Game(sys.argv[0], sys.argv[1])
    else:
        game = Game()
    while 1:
        game.update()
        # sleep(0.01)
