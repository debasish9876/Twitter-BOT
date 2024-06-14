import tweepy
import time

# Twitter API credentials
consumer_key = 'wOqeJ43FocaXGHWOySg8A9IMN'
consumer_secret = 'oxjsZ80BGdFE4Gc0lCEAOX1xmBEYDCQIXV8L0ZH5Emun0ISyQ7'
access_token = '1697119403975020544-R2BYELXjgwPdkkBdK1bYf5tW9mHrpo'
access_token_secret = 'QcFtHq7BWw9atOiO3PCOzHoBIH988JOAiQgocl72f93bl'


auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)


api = tweepy.API(auth)


keywords = ["Python", "AI", "Machine Learning"]


def retweet_keyword_tweets():
    for keyword in keywords:
        tweets = api.search_tweets(keyword)
        for tweet in tweets:
            try:
                tweet.retweet()
                print("Retweeted tweet by @" + tweet.user.screen_name)
            except tweepy.TweepError as e:
                print(e.reason)


def like_keyword_tweets():
    for keyword in keywords:
        tweets = api.search_tweets(keyword)
        for tweet in tweets:
            try:
                tweet.favorite()
                print("Liked tweet by @" + tweet.user.screen_name)
            except tweepy.TweepError as e:
                print(e.reason)


def respond_to_keyword_tweets():
    for keyword in keywords:
        tweets = api.search_tweets(keyword)
        for tweet in tweets:
            try:
                api.update_status("@" + tweet.user.screen_name + " Thanks for tweeting about " + keyword + "!")
                print("Replied to tweet by @" + tweet.user.screen_name)
            except tweepy.TweepError as e:
                print(e.reason)


def main():
    while True:
        retweet_keyword_tweets()
        like_keyword_tweets()
        respond_to_keyword_tweets()
        time.sleep(60)  

if __name__ == "__main__":
    main()
