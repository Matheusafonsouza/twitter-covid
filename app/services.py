import requests
import os
from requests import api
import tweepy
from bs4 import BeautifulSoup

class CoronaService:
    def __init__(self):
        self.base_url = 'https://www.worldometers.info/coronavirus/'

    def get_info(self, country=None):
        try:
            url = self.base_url
            if country:
                url += f'country/{country}/'

            response = requests.get(url)
        except Exception:
            raise Exception('Something gone bad on corona request')

        soup = BeautifulSoup(response.text, 'html.parser')
        container = soup.findAll('div', { "class": "maincounter-number" })

        if not container or len(container) < 1:
            raise Exception('Corona scrapper return nothing :(')

        return dict(
            cases=self.format_counter(container[0]),
            deaths=self.format_counter(container[1]),
            recovered=self.format_counter(container[2]),
            country=country
        )

    def format_counter(self, container):
        counter = container.text
        if not counter:
            return '0'
        return counter.strip()

class TweetService:
    def __init__(self):
        self.service = None
        self.authenticate()

    def authenticate(self):
        api_key = os.environ.get('TWEET_API_KEY')
        api_secret = os.environ.get('TWEET_API_SECRET')
        access_token = os.environ.get('TWEET_API_ACCESS_TOKEN')
        access_secret = os.environ.get('TWEET_API_ACCESS_SECRET')

        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)

        try:
            api = tweepy.API(auth)
            api.verify_credentials()
            self.service = api
        except Exception:
            raise Exception('Something gone bad on tweet service auth')

    def tweet(self, message):
        try:
            self.service.update_status(message)
        except Exception:
            raise Exception('Something gone bad when creating a tweet')