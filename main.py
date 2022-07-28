import tweepy
from time import sleep
import os



API_Key = os.environ.get("API_Key")
API_Key_Secret = os.environ.get("API_Key_Secret")
Bearer_Token = os.environ.get("Bearer_Token")
Access_Token = os.environ.get("Access_Token")
Access_Token_Secret = os.environ.get("Access_Token_Secret")

def api():
    auth = tweepy.OAuthHandler(API_Key,API_Key_Secret)
    auth.set_access_token(Access_Token,Access_Token_Secret)

    return tweepy.API(auth)

def retweet(tweepy_api: tweepy.API,hashtag:str,delay=60,items=10):
    for tweet in tweepy.Cursor(tweepy_api.search_tweets,q=hashtag).items(items):
        try:
            tweet_id = dict(tweet._json)['id']
            tweepy_api.retweet(tweet_id)
            tweepy_api.create_favorite(tweet_id)
        except tweepy.TweepyException:
            pass
            sleep(.5)
    sleep(delay)    

if __name__=="__main__":
    api=api()
    while True:
        retweet(api,"#Python",delay=5,items=1)
        retweet(api,"#100DaysOfCode",delay=5,items=1)
