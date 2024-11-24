import json
from typing import Union, Dict, List, Optional


def get_json(file) -> Union[Dict, List]:
    """
    Read from JSON file on disk
    """
    with open(file, "r") as infile:
        data = json.load(infile)
    return data


def is_disabled(value) -> Optional[bool]:
    """
    Returns True if the value is disabled or False if the value is enabled. Returns None otherwise
    :param value:
    :return:
    """
    if value == "disabled":
        return True
    elif value == "enabled":
        return False
