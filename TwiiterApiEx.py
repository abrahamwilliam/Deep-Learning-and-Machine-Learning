import tweepy
from textblob import TextBlob
import csv

consumer_key='0dJqgiNFA3mHYSFymLta1g7Pu'
consumer_secret='VZMjNJjlJLhZ0C5KepzyaJk2MFonOfqBX5oYSPu4iez3pqXA91'

access_token='631788821-Ii9ps4URnZ8b8Hk9gEJ3o84rWTnMKF4k8M9IQX9L'
access_token_secret='CJbamHcN04BibPG7Rln6P2wAc6TroPgnNU2EYHBja5DLA'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)


public_tweets=api.search('Abraham William')
for tweet in public_tweets:
	print(tweet.text)
	
	analysis=TextBlob(tweet.text)
	print(analysis.sentiment)

tweets_2d=[[tweet.id_str, tweet.created_at,tweet.text, tweet.text.encode("utf-8")] for tweet in public_tweets]
csv.writer(open('C:/Machine learing CMPE257/PythonLearningProjects/sample.csv','w')).writerow(tweets_2d)