# import tweepy package for accessing twitter APIs
import tweepy
# import textblob package for sentiment analysis of strings
from textblob import TextBlob

# import csv package to store tweets in csv
import csv

# keys required for twitter API authentication
consumer_key = '###'
consumer_secret = '###'

access_token = '###'
access_token_secret = '###'

# authenticating with twitter to use the api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# api variable to talk to the twitter api 
api = tweepy.API(auth)

# get the searched tweets
public_tweets = api.search('Taco')

def get_label(analysis):
	if analysis.sentiment[0] > 0:
		return 'positive'
	else:
		return 'negative'

# store tweets in csv
with open('dataset.csv', 'w') as file:
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		file.write('%s,%s\n' %(tweet.text.encode('utf8'), get_label(analysis)))
