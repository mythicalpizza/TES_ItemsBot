import random

from text import get_body_part


def assist_phrase_npc():
    return random.choice(["for", "on behalf of", "with the help of"])

def assist_phrase_object():
    return random.choice(["using", "with", "wielding", "with the help of"])

def obtain_word():
    return random.choice(["Get", "Steal", "Take", "Pick up", "Obtain", "Purchase", "Buy", "Secure", "Acquire", "Procure", "Seize", "Accept", "Capture"])

def major_minor():
    return random.choice(["Major", "Minor"])

def objective_at_location():
    return random.choice([
        "Clear out",
        "Destroy",
        "Repair",
        "Clean",
        "Defend",
        "Annihilate",
    ])

def object_suffix():
    suffix = ""
    if random.randint(1, 10) >= 8:
        suffix += " [STOLEN]"
    return suffix + random.choices([
        " added to inventory",
        " removed from inventory",
        f" sold for {random.randint(1,9999)} gold",
        f" equipped to {get_body_part()}",
        f" repaired for {random.randint(1, 9999)} gold",
        ""
    ], [10, 10, 10, 5, 10, 65])[0]
