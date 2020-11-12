# Twitter bot to retweet, follow, and DM people who interact with 
# specific user  from interaction
import tweepy
import time
import os 

# Assign twitter Oauth variables
consumer_key = 'MNG12P35j6DE18AgvRmC7dzyy'
consumer_secret = '47KuoW8b5GFFyy19buhqWIlpkCmEgrnadV8AAnIB9Sz65gbjvz'
key = '1288313457029390337-y856XMgPEnZg2i7p30d2x2zWTTaOKy'
secret = 'D3g4GCcTDrDIDXOD9cVHfYzPaU8SyAgJl3HS6z2OQG2wu'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
twittername ='@somediceguys'

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
def follow_followers():
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


follow_followers
diceguys_mentions