# Twitter bot to read, reply, and retweet
# from interaction
# tutorial link https://www.youtube.com/watch?v=ewq-91-e2fw&list=WL&index=2&t=112s
# stopped at 13:40
import tweepy
# Assign twitter variables
consumer_key = 'MNG12P35j6DE18AgvRmC7dzyy'
consumer_secret = '47KuoW8b5GFFyy19buhqWIlpkCmEgrnadV8AAnIB9Sz65gbjvz'

key = '1288313457029390337-y856XMgPEnZg2i7p30d2x2zWTTaOKy'
secret = 'D3g4GCcTDrDIDXOD9cVHfYzPaU8SyAgJl3HS6z2OQG2wu'

# OAuth1 authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# Test tweet with authentication
#api.update_status('We need more pods, Roll for more episodes!')

# Returns the 20 most recent mentions, including retweets.
tweets = api.mentions_timeline()

# print last 20 tweets in reverse chronological order
# reading the most recent tweet at the end of the output
#print(tweets[0])

# for loop
for tweet in tweets:
# if statement to check if @somediceguys was tweeted
#    if '@somediceguys' in tweet.text.lower():
        print(str(tweet.id) + ' - ' + tweet.text)
