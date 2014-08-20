"""
Doughnut bot
============

Responds to tweets mentioning
"doughnut" (or some variation)
with a gif of a doughnut.
"""

import time

import twitkit
from giphypop import Giphy

g = Giphy()

class DoughnutBot():
    def __init__(self, username):
        """
        Only interact with a specific
        user; we don't want to spam folks!
        """
        self.username = username
        self.seen_tweet_ids = []
        self.run()

    def run(self):
        self.think()
        while True:
            time.sleep(60.0)
            self.think()

    def think(self):
        for tweet in self.new_tweets():
            if any(w in tweet.text.lower() for w in ['doughnut', 'donut']):
                gif_url = g.screensaver(tag='doughnut').media_url
                twitkit.tweet('@{0} DOUGHNUTS: {1}'.format(self.username, gif_url))

    def new_tweets(self):
        """
        Yield only tweets
        which haven't been seen before.
        """
        for tweet in twitkit.user_tweets(self.username):
            if tweet.id not in self.seen_tweet_ids:
                self.seen_tweet_ids.append(tweet.id)
                yield tweet


