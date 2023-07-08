import tweepy
from atproto import Client
import pytumblr2
import config
import time
from datetime import datetime
import forge
import log


#Set the script configuration
about = config.getJSON('about.json')
flags = config.getJSON("flags.json")

#Attempt to create log directory. This is important to be first because all further errors should be logged
if not config.isDisabled(flags["logs"]):
    try:
        log.createDirectory("logs")
        print("Log directory successfully created.")
        #Try and create the log file itself now
        try:
            date_time = datetime.fromtimestamp(time.time())
            log.createEntry("Log file initialized at % s " % date_time.strftime("%d-%m-%Y, %H:%M:%S"))
            print("Log file successfully created")
        except:
            print("Error: unable to create log file.")
    except:
        print("Error: unable to create log directory.")
else:
    print("Logs disabled.")

######################################################################################################
#Initializes twitter api and posts, if not disabled
if not config.isDisabled(flags['twitter']):
    try:
        #Fetch credentials file
        twitter_credentials = config.getJSON("../../credentials/twitter.json")

        try:
            #Attempt to log in to twitter
            client = tweepy.Client(consumer_key=twitter_credentials["consumer_key"],
                consumer_secret=twitter_credentials["consumer_secret"],
                access_token=twitter_credentials["access_token_key"],
                access_token_secret=twitter_credentials["access_token_secret"])

            #Post the tweet
            response = client.create_tweet(text=forge.item())
            print(response)
        except:
            print("Unable to authenticate twitter credentials.")
            log.createEntry("Unable to authenticate twitter credentials.")
    except:
        print("Unable to fetch twitter credentials from file")
        log.createEntry("Unable to fetch twitter credentials from file")


#Initializes bluesky api and posts, if not disabled
if not config.isDisabled(flags['bluesky']):
    try:
        #Fetch credentials file
        bsky_credentials = config.getJSON("../../credentials/bluesky.json")

        try:
            #Attempt to log into BlueSky
            client = Client()
            client.login(bsky_credentials["bsky_username"], bsky_credentials["bsky_app_password"])

            #Post the skeet
            response = client.send_post(text=forge.item())
            print(response)
        except:
            print("Unable to authenticate BlueSky credentials.")
            log.createEntry("Unable to authenticate BlueSky credentials.")
    except:
        print("Unable to fetch BlueSky credentials from file")
        log.createEntry("Unable to fetch BlueSky credentials from file")

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
