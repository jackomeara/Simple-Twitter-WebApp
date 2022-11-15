import tweepy
from configparser import ConfigParser
from time import sleep

class TwitterBot():
    def __init__(self):
        config = ConfigParser()
        config.read("creds.ini")
        consumer_key = config.get("twitter_creds", "api_key")
        consumer_secret = config.get("twitter_creds", "api_secret")
        access_token = config.get("twitter_creds", "access_token")
        access_secret = config.get("twitter_creds", "access_secret")
        auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret,
        access_token, access_secret
        )
        self.client = tweepy.API(auth)
        # self.client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_secret)

    def get_trending(self, place_id):
        data = self.client.get_place_trends(place_id)
        data = data[0]['trends']
        trends = [trend['name'] for trend in data]
        return trends



