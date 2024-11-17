import tweepy
from tweepy import HTTPException

from sites.social_media_site import SocialMediaSite
from sites import SocialMediaSitePostingException


class Twitter(SocialMediaSite):
    """
    Represents connection to Twitter API
    """
    def __init__(self, creds_file_path: str):
        super().__init__(creds_file_path)
        self.client = tweepy.Client(consumer_key=self.creds["consumer_key"],
                               consumer_secret=self.creds["consumer_secret"],
                               access_token=self.creds["access_token_key"],
                               access_token_secret=self.creds["access_token_secret"])

    def post(self, content: str):
        try:
            self.client.create_tweet(text=content)
        except HTTPException as e:
            raise SocialMediaSitePostingException(f"Could not make tweet: {e}")
