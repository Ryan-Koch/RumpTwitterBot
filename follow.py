import tweepy
from credentials import *

# Set up your authorisations
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#follow POTUS friends
followers = api.followers('realDonaldTrump', -1)
print(followers)
