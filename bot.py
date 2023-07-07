import tweepy
from atproto import Client
import pytumblr2
import config
import time
import forge

#Set the script configuration
about = config.getJSON('about.json')
flags = config.getJSON("flags.json")
twitter_credentials = config.getJSON("../../credentials/twitter.json")
bsky_credentials = config.getJSON("../../credentials/bluesky.json")
tumblr_credentials = config.getJSON("../../credentials/tumblr.json")


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

#Initializes bluesky api and posts, if not disabled
if not config.isDisabled(flags['bluesky']):
    #Initialize the bluesky AT Protocol
    client = Client()
    client.login(bsky_credentials["bsky_username"], bsky_credentials["bsky_app_password"])

    #Post the skeet
    response = client.send_post(text=forge.item())
    print(response)

#Initializes the Tumblr API, if not disabled
if not config.isDisabled(flags['tumblr']):
    #Initialize the tumblr api
    client = pytumblr2.TumblrRestClient(
    tumblr_credentials["consumer_key"], tumblr_credentials["consumer_secret"], tumblr_credentials["oauth_token"], tumblr_credentials["oauth_secret"])

    #Post the ... post
    response = client.create_post("TES-ItemsBot", content=[{'type': 'text', 'text': forge.item()}])
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
