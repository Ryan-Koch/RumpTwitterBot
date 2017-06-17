import tweepy
import json
import re
from credentials import *
import glob
import tweet_cache

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
wrong = glob.glob("wrong.gif")

def get():
    # Set up your authorisations
    # wrong = Image.open('wrong.jpg')

    results = api.search(q="@realTrumpyBot", count = 50)
    mention_tweets = tweet_cache.cache_and_trim('mention_ids.csv', results)

    return mention_tweets

def reply(tweets):

    for tweet in tweets:
        mention_text = tweet.text
        goofy_user = tweet.user.screen_name
        mention_id = tweet.id
        tweet_string = "@" + goofy_user + " WRONG!"
        try:
            api.update_with_media(wrong[0], tweet_string, in_reply_to_status_id = mention_id)
        except IndexError as e:
            log.log(e)
