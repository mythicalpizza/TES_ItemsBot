import random
from typing import List


def get_from_file(f: str) -> str:
    """
    Gets a random line from the given file
    """
    with open(f"words/{f}.txt", 'r') as words_file:
        line = random.choice(words_file.readlines())
        return line.rstrip()

def get_lines_from_file(f: str) -> List[str]:
    """
    Gets all lines from the given file and returns them as a list
    """
    with open(f"words/{f}.txt", 'r') as words_file:
        lines = words_file.readlines()
        return [l.rstrip() for l in lines if l.rstrip() != ""]