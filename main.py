# Some basic Twitter bot script fun.

import tweet
import create_image
import get_tweets
import clean_up_imgs
import mentions
import log


tweets = get_tweets.get_tweets()

if(len(tweets) > 0):

	create_image.imagify_tweet(tweets)
	tweet.send(tweets)
	clean_up_imgs.clean()

else:
	log.log("No tweets to tweet :(")

# mentions bro
mention_list = mentions.get()

if(len(mention_list) > 0):
	mentions.reply(mention_list)

else:
	log.log("No mentions to tweet :(")
