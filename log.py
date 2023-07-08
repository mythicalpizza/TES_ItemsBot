import os
from datetime import datetime
import time

def createDirectory(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print("Created new directory '% s'" % path)
    else:
        print("Error: A directory named '% s' already exists!" % path)

def createEntry(message):
    if not os.path.exists("logs/teslog.txt"):
        f = open("logs/teslog.txt", "x")
        f.write(message)
        f.close()
    else:
        f = open("logs/teslog.txt", "a")
        date_time = datetime.fromtimestamp(time.time())
        f.write("\n" + date_time.strftime("%d-%m-%Y, %H:%M:%S") + ": " + message)
        f.close()
