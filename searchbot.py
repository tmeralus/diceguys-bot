# Twitter bot to search, like, and retweet specific hashtags
import tweepy
import time
# Assign twitter variables
consumer_key = 'MNG12P35j6DE18AgvRmC7dzyy'
consumer_secret = '47KuoW8b5GFFyy19buhqWIlpkCmEgrnadV8AAnIB9Sz65gbjvz'

key = '1288313457029390337-y856XMgPEnZg2i7p30d2x2zWTTaOKy'
secret = 'D3g4GCcTDrDIDXOD9cVHfYzPaU8SyAgJl3HS6z2OQG2wu'

# OAuth1 authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# name for file saving tweet records
# ttrpg, pathfinder podcast dndstream roleplaying

# specify hashtag to search for and number of hashtags
hashtag1 = '#actualplay'
hashtag2 = '#ttrpg'
hashtag3 = '#pathfinder'
hashtag4 = '#dndstream'
hashtag5 = '#dungeonsandragons'
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag1).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            print("Retweet done!")
            time.sleep(3)
            #time.sleep(3600)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3)
            #time.sleep(3600)

searchBot()
