import random
from typing import List


def get_all_lines_from_file(f: str) -> List[str]:
    """
    Gets all lines from the given file and returns them as a list. Excludes blanks and lines starting with "#" so you
    can format and include comments as you see fit
    """
    with open(f"words/{f}.txt", "r") as words_file:
        lines = [l.strip() for l in words_file.readlines()]
        lines = [l for l in lines if l and not l.startswith("#")]
        return lines


def get_random_line_from_file(f: str) -> str:
    """
    Gets a random line from the given file
    """
    lines = get_all_lines_from_file(f)
    return random.choice(lines)
