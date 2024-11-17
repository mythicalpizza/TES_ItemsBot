import random


def get_from_file(f: str) -> str:
    """
    Gets a random line from the given file
    """
    with open(f"words/{f}.txt", 'r') as words_file:
        line = random.choice(words_file.readlines())
        return line.rstrip()
