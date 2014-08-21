import sys
from MYBOT import MyBot

if __name__ == '__main__':
    b = MyBot(*sys.argv[1:])
    b.run()
