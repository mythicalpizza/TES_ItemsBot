import json

#Open config file and return as pythion dict
def getJSON(file):
    f = open(file)
    data = json.load(f)
    f.close
    return data

def isDisabled(value):
    if value == "disabled":
        return True
    elif value == "enabled":
        return False
