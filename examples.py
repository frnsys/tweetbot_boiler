import sys
from examples import DoughnutBot, WallyBot

if __name__ == '__main__':
    bot_name = sys.argv[1]
    if bot_name == 'doughnut':
        b = DoughnutBot(*sys.argv[2:])
    elif bot_name == 'wally':
        b = WallyBot(*sys.argv[2:])
    b.run()
