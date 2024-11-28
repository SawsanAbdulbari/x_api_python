import tweepy
from config.config import *

def get_client():
   return tweepy.Client(
       BEARER_TOKEN, API_KEY, API_SECRET_KEY,
       ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
       wait_on_rate_limit=True
   )
def get_api():
   auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
   auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
   return tweepy.API(auth, wait_on_rate_limit=True)