#import twitter
import tweepy
import config
import time
import forge

#Set the script configuration
about = config.getJSON('about.json')
flags = config.getJSON("flags.json")
twitter_credentials = config.getJSON("credentials/twitter.json")#previously had ../../ as a path prefix. Not sure why. This might be important

#Posts a tweet
def tweet(body):
    newTweet = api.PostUpdate(body)

#Initializes twitter api and posts, if not disabled
if not config.isDisabled(flags['twitter']):
    #Initialize twitter api
    client = tweepy.Client(consumer_key=twitter_credentials["consumer_key"],
        consumer_secret=twitter_credentials["consumer_secret"],
        access_token=twitter_credentials["access_token_key"],
        access_token_secret=twitter_credentials["access_token_secret"])
    #Post the tweet

    response = client.create_tweet(text=forge.item())

print(response)

##############################Debug##################################
def timed_test(seconds):
    start_time = time.time()
    iterations = 0

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        print(forge.item())
        iterations += 1

        if elapsed_time > seconds:
            print("Test completed. " + str(iterations) + " items generated in " + str(seconds) + " second(s).")
            break

#tweet(forge.item())
#timed_test(1)
