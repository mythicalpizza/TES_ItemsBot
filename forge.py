import random
import readText
import config

def item():

    varieties = {
    0: weapon,
    1: armor,
    2: shout,
    3: spell,
    4: potion,
    5: misc
    }

    flags = config.getJSON("flags.json")
    if config.isDisabled(flags["blessings"]) != True:
        varieties[6] = blessing

    if config.isDisabled(flags["diseases"]) != True:
        varieties[7] = disease

    if config.isDisabled(flags["objectives"]) != True:
        varieties[8] = objective

    return varieties[random.randint(0, len(varieties)-1)]()

def ismajor():
    m = ["Major", "Minor"]
    random.shuffle(m)
    return m[0]

def weapon():
    potentials = {
        0: readText.get_from_file("adjectives") + " " + readText.get_from_file("weapons") + " of " + readText.get_from_file("effects"),
        1: readText.get_from_file("weapon_types") + " " + readText.get_from_file("weapons") + " of " + readText.get_from_file("effects"),
        2: readText.get_from_file("adjectives") + " " + readText.get_from_file("weapons"),
        3: readText.get_from_file("weapon_types") + " " + readText.get_from_file("weapons") + " of " + readText.get_from_file("effects"),
        4: readText.get_from_file("adjectives") + " " + readText.get_from_file("race") + " " + readText.get_from_file("weapons") + " of " + readText.get_from_file("effects"),
        5: readText.get_from_file("adjectives") + " " + readText.get_from_file("weapons") + " of " + ismajor() + " " + readText.get_from_file("effects")
    }

    return potentials[random.randint(0, 5)]

def armor():
    potentials = {
        0: readText.get_from_file("adjectives") + " " + readText.get_from_file("armor") + " of " + readText.get_from_file("effects"),
        1: readText.get_from_file("armor_types") + " " + readText.get_from_file("armor") + " of " + readText.get_from_file("effects"),
        2: readText.get_from_file("adjectives") + " " + readText.get_from_file("race") + " " + readText.get_from_file("armor") + " of " + readText.get_from_file("effects"),
        3: readText.get_from_file("people") + " " + readText.get_from_file("adjectives") + " " + readText.get_from_file("armor"),
        4: readText.get_from_file("adjectives") + " " + readText.get_from_file("armor") + " of " + readText.get_from_file("effects"),
        5: readText.get_from_file("quality") + " " + readText.get_from_file("people") + "'s " + readText.get_from_file("adjectives") + " " + readText.get_from_file("armor"),
        6: readText.get_from_file("quality") + " " + readText.get_from_file("armor_types") + " " + readText.get_from_file("armor"),
        7: readText.get_from_file("quality") + " " + readText.get_from_file("people") + "'s " + readText.get_from_file("armor"),
        8: readText.get_from_file("skill_rank") + " " + readText.get_from_file("armor") + " of " + readText.get_from_file("adjectives") + " " + readText.get_from_file("effects"),
        9: readText.get_from_file("adjectives") + " " + readText.get_from_file("skill_rank") + " " + readText.get_from_file("armor"),
        10: readText.get_from_file("adjectives") + " " + readText.get_from_file("armor") + " of " + readText.get_from_file("effects"),
        11: readText.get_from_file("skill_rank") + " " + readText.get_from_file("armor") + " of " + readText.get_from_file("schools")
    }

    return potentials[random.randint(0, 11)]

def shout():
    prefix = "Word of Power Learned: "
    potentials = {
        0: readText.get_from_file("actions") + " " + readText.get_from_file("adjectives") + " " + readText.get_from_file("misc"),
        1: readText.get_from_file("actions") + " " + readText.get_from_file("adjectives") + " " + readText.get_from_file("effects"),
        2: readText.get_from_file("actions") + " " + readText.get_from_file("poisonrank") + " " + readText.get_from_file("effects"),
        3: readText.get_from_file("weapons") + " " + readText.get_from_file("adjectives") + " " + readText.get_from_file("misc")
    }

    return prefix + potentials[random.randint(0, 3)]

def spell():
    prefix = "Spell Tome: "
    potentials = {
        0: readText.get_from_file("actions") + " " + readText.get_from_file("people"),
        1: readText.get_from_file("adjectives") + " " + readText.get_from_file("actions"),
        2: readText.get_from_file("adjectives") + " " + readText.get_from_file("misc"),
        3: readText.get_from_file("adjectives") + " " + readText.get_from_file("effects"),
        4: readText.get_from_file("actions") + " " + readText.get_from_file("actions"),
        5: readText.get_from_file("alter") + " " + readText.get_from_file("misc")
    }

    return prefix + potentials[random.randint(0, 5)]

def potion():
    prefix = "Potion of "
    potentials = {
        0: readText.get_from_file("adjectives") + " " + readText.get_from_file("effects"),
        1: readText.get_from_file("actions") + " " + readText.get_from_file("effects"),
        2: readText.get_from_file("adjectives") + " " + readText.get_from_file("people"),
        3: readText.get_from_file("actions") + " " + readText.get_from_file("misc"),
        4: readText.get_from_file("alter") + " " + readText.get_from_file("body_parts"),
        5: readText.get_from_file("adjectives") + " " + readText.get_from_file("body_parts")
    }
    return prefix + potentials[random.randint(0, 5)]

def misc():
    potentials = {
        0: readText.get_from_file("adjectives") + " " + readText.get_from_file("misc") + " of " + readText.get_from_file("effects"),
        1: readText.get_from_file("adjectives") + " " + readText.get_from_file("misc"),
        2: readText.get_from_file("people") + "'s " + readText.get_from_file("misc") + " of " + readText.get_from_file("effects"),
        3: readText.get_from_file("people") + "'s " + readText.get_from_file("misc"),
        4: readText.get_from_file("adjectives") + " " + readText.get_from_file("race")
    }

    return potentials[random.randint(0, 4)]

def blessing():
    potentials = {
        0: readText.get_from_file("divines") + "'s Blessing of " + readText.get_from_file("effects"),
        1: readText.get_from_file("daedric_lord") + "'s Curse of " + readText.get_from_file("effects"),
        2: readText.get_from_file("divines") + "'s " + readText.get_from_file("adjectives") + " Curse",
        3: readText.get_from_file("divines") + "'s " + readText.get_from_file("adjectives") + " Blessing",
        4: readText.get_from_file("daedric_lord") + "'s " + readText.get_from_file("adjectives") + " Curse",
        5: readText.get_from_file("daedric_lord") + "'s " + readText.get_from_file("adjectives") + " Blessing"
    }

    return potentials[random.randint(0, 5)]

def disease():
    return "Disease"

def objective():
    return "Objective"

#item()
