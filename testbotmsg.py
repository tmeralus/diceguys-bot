import tweepy
import time
import datetime
import os
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME, TWEET_NUMBER
# Assign twitter Oauth variables
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
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

# Retweet people who mention twittername
def diceguys_mentions():
    # Returns the 20 most recent mentions, including retweets.
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    # for loop to like and retweet any
    # tweets containing @somediceguys
    for tweet in reversed(tweets):
        if twittername in tweet.full_text.lower():
            print("New twitter interaction")
            tweet.retweet()
            api.create_favorite(tweet.id)


# the screen name of the user
screen_name = "techgameteddy"

# fetching the user ID
user = api.get_user(screen_name)
ID = user.id_str
# debug print ID of user
#print("The ID of the user is : " + ID)

# ID of the recipient
recipient_id = '198385563'

# Use datetime to store current time
ct = datetime.datetime.now()
#print("current time:-", ct)

# text to be sent
text = 'Dice Bot was run at today at '
endtext = " using python3"

# sending the direct message
direct_message = api.send_direct_message(recipient_id, text + str(ct))

# printing the text of the sent direct message
print(direct_message.message_create['message_data']['text'])
