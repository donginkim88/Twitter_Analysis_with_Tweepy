# -*- coding: utf-8 -*-
import tweepy
import json
import pprint
import geocoder
import time
import pandas as pd
import datetime as dt
from tweepy import Stream
from tweepy.streaming import StreamListener


# Twitter Credentials
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# Authentificaiton 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Creation of the actual interface
api = tweepy.API(auth, 
	wait_on_rate_limit=True,  #wait when running out of calls to replenish
    wait_on_rate_limit_notify=True,
	retry_count=3, retry_delay=5,  #handle temporary failures
	retry_errors=set([401, 404, 500, 503]))


# Geocoding
g = geocoder.google('California')
ca = g.geojson["bbox"]  # get lat, long

# Create MyListener Class
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('/Users/DonginKim/Documents/Python/Social Media/Sample.txt', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
 
    def on_error(self, status):
        print("Error:", status)
        return True


# Execute Twitter Streaming
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(locations=ca)

#[SWlongitude, SWLatitude, NElongitude, NELatitude]
#twitter_stream.filter(locations=[170.59, 18.77, -66.88, 71.53])
#twitter_stream.filter(track=['trump'])  #filter by keywords 
#twitter_stream.filter(follow=["2211149702"])  #filter by id
#twitter_stream.filter(track=['#python'])  #filter by hashtag
#filter by language: language=['en']