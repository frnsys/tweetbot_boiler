from collections import namedtuple

import tweepy
from tweepy import TweepError

import config

Tweet = namedtuple('Tweet', ['id', 'text'])

def _api():
    """
    Load auth info from config.
    Setup things on Twitter's end at:
    https://apps.twitter.com/
    """
    auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_SECRET)

    # Return API object.
    return tweepy.API(auth)

api = _api()

def user_tweets(username, count=200):
    """
    Returns 200 last tweets for a user.
    """
    return [Tweet(tweet.id, tweet.text)
            for tweet in api.user_timeline(screen_name=username, count=count)]

def retweet(id):
    """
    Retweet a tweet by id.
    """
    try:
        api.retweet(id)
    except TweepError as err:
        # Assume we may have violated some rate limit
        # and forget about it
        if '403' in err:
            print('403 error when trying to retweet. Possibly hit a rate limit.')
        else:
            raise err


def tweet(text):
    """
    Tweet something from your account.
    """
    try:
        api.update_status(text)
    except TweepError as err:
        # Assume we may have violated some rate limit
        # and forget about it
        if '403' in err:
            logger.info('403 error when trying to tweet. Possibly hit a rate limit.')
        else:
            raise err