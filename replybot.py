import tweepy
import time
import os
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME, TWEET_NUMBER
# Assign twitter Oauth variables
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
# Twitter search strings variables for liking and retweeting trending hashtags
tweetNumber = 20
hashtag1 = '#actualplay'
hashtag1tweets = tweepy.Cursor(api.search, hashtag1).items(tweetNumber)
hashtag2 = '#ttrpg'
hashtag2tweets = tweepy.Cursor(api.search, hashtag2).items(tweetNumber)
hashtag3 = '#pathfinder'
hashtag3tweets = tweepy.Cursor(api.search, hashtag3).items(tweetNumber)
hashtag4 = '#dnd'
hashtag4tweets = tweepy.Cursor(api.search, hashtag4).items(tweetNumber)
hashtag5 = '#dungeonsandragons'
hashtag5tweets = tweepy.Cursor(api.search, hashtag5).items(tweetNumber)

hashtaglist = ['#actualplay', '#ttrpg', '#pathfinder', '#dndstream', '#dungeonsanddragons' ]

# name for file saving tweet records
FILE_NAME = 'last_seen.txt'
# Read method for reading last_seen.txt file for reading latest tweets
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

# Write method to write to last_seen.txt file for reading latest tweets
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

# ID of the recipient
recipient_id = @techgameteddy

# text to be sent
text = "Dice Bot was run"

# sending the direct message
direct_message = api.send_direct_message(recipient_id, text)

# printing the text of the sent direct message
print(direct_message.message_create['message_data']['text'])
