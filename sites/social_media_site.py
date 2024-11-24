import json
from abc import ABCMeta, abstractmethod
from json import JSONDecodeError
from typing import Optional

import forge
from sites.exceptions import SocialMediaSiteCredentialsException


class SocialMediaSite(metaclass=ABCMeta):
    """
    Represents a social media site
    """

    def __init__(self, creds_file_path: str):
        classname = self.__class__.__name__
        try:
            with open(creds_file_path, "r") as creds_file:
                self.creds = json.load(creds_file)
        except (IOError, JSONDecodeError) as e:
            raise SocialMediaSiteCredentialsException(
                f"Could not get credentials for {classname}: {e}"
            )
        if any(not self.creds[key] for key in self.creds.keys()):
            raise SocialMediaSiteCredentialsException(
                f"At least one item in the credentials file is blank for {classname}"
            )

    @abstractmethod
    def post(self, content: str):
        """
        Override this method with one that interacts with a service's API
        """
        raise NotImplementedError()

    def items_bot_post(self, item: Optional[str]):
        """
        Create a new item if one wasn't passed in, and then post it to social media
        """
        if item is None:
            item = forge.item()
        return self.post(item)
