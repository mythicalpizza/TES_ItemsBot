import twitter
import config
import time
import forge

#Set the script configuration
about = config.getJSON('about.json')
flags = config.getJSON("flags.json")


#Initialize api
api = twitter.Api(consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret='')

#Posts a tweet
def tweet(body):
    newTweet = api.PostUpdate(body)
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

#timed_test(1)
