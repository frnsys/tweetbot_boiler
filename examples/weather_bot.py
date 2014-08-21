"""
Wally the Weather bot
=====================

Tweets weather forecasts
and some helpful advice.
"""

import time

import twitkit
import weatherpy

class WallyBot(twitkit.TwitterBot):
    def __init__(self):
        pass

    def run(self):
        self.think()
        while True:
            # Every hour
            time.sleep(360.0)
            self.think()

    def think(self):
        """
        WOEID for 11211 = 12761729
        http://woeid.rosselliot.co.nz/
        """
        r = weatherpy.Response('Wally the Weather Bot', 12761729, metric=False)
        conditions = r.condition

        body = ''
        code_text = self.text_for_code(conditions.code)
        temp_text = self.text_for_temp(conditions.temperature)

        if code_text and temp_text:
            body = code_text + ' AND ' + temp_text
        else:
            body = code_text + temp_text

        if body:
            twitkit.tweet(body)
        else:
            print('I am speechless for:')
            print(conditions.code)
            print(conditions.temperature)
            print(conditions.text)



    def text_for_code(self, code):
        """
        https://developer.yahoo.com/weather/#codes
        """
        return {
            9: 'Just a little drizzle right now',
            11: 'LOTS OF RAIN BRING AN UMBRELLA',
            12: 'LOTS OF RAIN BRING AN UMBRELLA',
            17: 'HUGE ICE CHUnks ARE FALLINg STAY INSIDE',
            32: 'It\'s beautiful outside, GTFO',
            34: 'A calm day today, take a moment and relax :)'
        }.get(code, '')

    def text_for_temp(self, temp):
        text = ''
        if temp < 32:
            text = 'IT IS BELoW FREezzNG STAY INSIDE'
        elif temp < 44:
            text = 'it\'s kinda chilly wear a jacket pls'
        elif temp < 60:
            text = 'hm it\'s kinda warm, bring a light sweater buddy'
        elif temp < 80:
            text = 'pretty warm out there today pal'
        elif temp < 100:
            text = 'it is SWELteRING be CAREFUL drink lots of WATER folks'
        return text
