import random
import readText
import config

def item():
    varieties = {
    'weapon': (weapon, 50),
    'armor': (armor, 50),
    'shout': (shout, 50),
    'spell': (spell, 50),
    'potion': (potion, 50),
    'misc': (misc, 30),
    'blessing': (blessing, 30),
    'disease': (disease, 30),
    'objective': (objective, 45)
    }

    flags = config.getJSON("flags.json")
    if config.isDisabled(flags['blessings']):
        varieties.pop('blessing')
    if config.isDisabled(flags['diseases']):
        varieties.pop('disease')
    if config.isDisabled(flags['objectives']):
        varieties.pop('objective')

    function_list = [f[0] for f in list(varieties.values())]
    weights_list = [w[1] for w in list(varieties.values())]

    return random.choices(function_list, weights_list)[0]()

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
    potentials = {
        0: "Return the " + readText.get_from_file("adjectives") + " " + readText.get_from_file("objects") + " to " + readText.get_from_file("npcs"),
        1: "Meet " + readText.get_from_file("npcs") + " " + readText.get_from_file("vicinity") + " the " + readText.get_from_file("location"),
        2: "Bring the " + weapon() + " to " + readText.get_from_file("npcs"),
        3: "Bring the " + armor() + " to " + readText.get_from_file("npcs"),
        4: "Bring the " + potion() + " to " + readText.get_from_file("npcs"),
        5: "Retrieve the " + readText.get_from_file("adjectives") + " " + readText.get_from_file("objects") + " for " + readText.get_from_file("npcs")
    }

    return potentials[random.randint(0, len(potentials)-1)]
#readText.get_from_file()
#print(item())
