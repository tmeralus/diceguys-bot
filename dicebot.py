import tweepy
import time
import os
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME, TWEET_NUMBER
# Assign twitter Oauth variables
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# Array for hashtags
hashtaglist = ['#actualplay', '#ttrpg', '#PathFinder', '#dndstream', '#dungeonsanddragons', '#DnD', '#dnd' ]
hashArraytweet = tweepy.Cursor(api.search, hashtaglist).items(tweetNumber)
hashtag1 = '#actualplay'
hashtag1tweets = tweepy.Cursor(api.search, hashtag1).items(tweetNumber)

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

# pull last tweet ID and saved to last seen file

# Send reply back to users
def reply():
    # Returns the 20 most recent mentions, including retweets.
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    # for loop to print tweet id and tweet in order
    # and responds to last seen tweet with a thank you
    for tweet in reversed(tweets):
        if twittername in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.create_favorite(tweet.id)
            #api.update_status("@" + tweet.user.screen_name + " Thank you!", tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

# Retweet people who mention twittername
def diceguys_mentions():
    # Returns the 20 most recent mentions, including retweets.
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    # for loop to like and retweet any
    # tweets containing @somediceguys
    for tweet in reversed(tweets):
        if twittername in tweet.full_text.lower():
            print("Retweeted twitter interaction")
            tweet.retweet()
            api.create_favorite(tweet.id)

# Send DM to new followers
def follow_back():
    # Returns the 20 most recent mentions, including retweets.
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    new_followers = API.followers(user)

    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
    # for loop to send direct messages to new followers
    for i in reversed(new_followers):
        if '@somediceguys' in tweet.full_text.lower():
            api.get_direct_message(tweet.id)
            api.send_direct_message(twitter_user, 'Thank you for following us. We are just getting started with our adventure. Feel free to listen to our podcast here https://linktr.ee/somediceguys ')
            print("New twitter follower, DM sent ")

# For loop to search and like hashtag list
def search_and_like():
    for tweet in hashtaglist:
        api.create_favorite(tweet.id)
        print( tweet + " found, adding to favorites")

# Search for hashtag variables, like, and retweet
def searchbot_ht1():
    for tweet in hashArraytweet:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            print( hashtag1 + " found, liked and retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3)

# Call selected functions
search_and_like()
searchbot_ht1()
reply()
follow_back()
diceguys_mentions()
