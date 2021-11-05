import random

def get_from_file(f):
    with open("words/" +  f + ".txt", 'r') as l:
        line = random.choice(l.readlines())
        l.close()
        line = line.rstrip()
        return line
