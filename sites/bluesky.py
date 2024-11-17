import atproto.exceptions
from atproto import Client
from atproto_client.exceptions import UnauthorizedError
from atproto_core.exceptions import AtProtocolError

from sites.social_media_site import SocialMediaSite
from sites import SocialMediaSitePostingException, SocialMediaSiteCredentialsException


class BlueSky(SocialMediaSite):
    """
    Represents connection to BlueSky API
    """
    def __init__(self, creds_file_path: str):
        super().__init__(creds_file_path)
        self.client = Client()
        try:
            self.client.login(self.creds["bsky_username"], self.creds["bsky_app_password"])
        except UnauthorizedError as e:
            raise SocialMediaSiteCredentialsException(f"BlueSky credentials invalid: {e}")

    def post(self, content: str):
        try:
            self.client.send_post(text=content)
        except SocialMediaSitePostingException as e:
            raise RuntimeError(f"Could not make BlueSky post: {e}")
