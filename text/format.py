import random

from read_text import get_all_lines_from_file


def pluralize(noun: str) -> str:
    """
    Return the correct plural form of a given noun
    """
    # singular plurals
    if noun in get_all_lines_from_file("race") and noun.endswith("mer"):
        return noun
    if any(noun.lower().endswith(word) for word in ["sheep", "deer", "daedra", "fish", "forsworn", "alik'r"]):
        return noun
    if noun.lower().endswith("ach"):
        return noun + "s"
    if noun.endswith("y"):
        return noun[:-1] + "ies"
    if noun.endswith("f"):
        return noun[:-1] + "ves"
    if noun.endswith("fe"):
        return noun[:-2] + "ves"
    if any(noun.endswith(x) for x in ["s", "ss", "sh", "ch", "x", "z"]):
        return noun + "es"
    return noun + "s"


def smart_title_case(string: str) -> str:
    """
    Return string in title case except it doesn't capitalize a couple things lol
    """
    return string.title().replace("Of", "of").replace(" The", " the").replace("'R", "'r")


def possessive(string: str) -> str:
    """
    Return proper possessive form of the given string
    """
    if string.endswith("s") and not string.endswith("ss"):
        return string + "'"
    return string + "'s"
