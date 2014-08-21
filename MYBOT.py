import twitkit
from twitkit import TwitterBot

class MyBot(TwitterBot):
    """
    Implement your cool new twitter bot!
    """
    def __init__(self, *args):
        print(args)

    def run(self):
        print('running')
