import tweepy
import time
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)

user=api.me()

#print(user.followers_count)

def limit_rate(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

search_string='@alluarjun'
numberoftweets=2
for tweet in limit_rate(tweepy.Cursor(api.search,search_string).items(numberoftweets)):
    try:
        tweet.favorite()
        print('i liked that tweet')
    except tweepy.TweepError as er:
        print(er.reason)
    except StopIteration:
        break





""" generous bot          
for follower in tweepy.Cursor(api.followers).items():
    if follower.name=='Ratna REDDY':
        follower.follow()
        break """