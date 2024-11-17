import random
import read_text
import config


def item():
    varieties = {
        'weapon': (weapon, 50),
        'armor': (armor, 50),
        'shout': (shout, 50),
        'spell': (spell, 50),
        'potion': (potion, 50),
        'misc': (misc, 30),
        'blessings': (blessing, 30),
        'diseases': (disease, 30),
        'objectives': (objective, 60)
    }

    flags = config.get_json("flags.json")
    for feature in ["blessings", "diseases", "objectives"]:
        if config.is_disabled(flags[feature]):
            varieties.pop(feature)

    function_list = [f[0] for f in list(varieties.values())]
    weights_list = [w[1] for w in list(varieties.values())]
    return random.choices(function_list, weights_list)[0]()


def ismajor():
    return random.choice(["Major", "Minor"])


def weapon():
    adjective = read_text.get_from_file("adjectives")
    weapon = read_text.get_from_file("weapons")
    weapon_type = read_text.get_from_file("weapon_types")
    effect = read_text.get_from_file("effects")
    race = read_text.get_from_file("race")
    magnitude = ismajor()
    choices = [
        f"{adjective} {weapon} of {effect}",
        f"{weapon_type} {weapon} of {effect}",
        f"{adjective} {weapon}",
        f"{weapon_type} {weapon} of {effect}",
        f"{adjective} {race} {weapon} of {effect}",
        f"{adjective} {weapon} of {magnitude} {effect}"
    ]
    return random.choice(choices)


def armor():
    adjective = read_text.get_from_file("adjectives")
    armor_type = read_text.get_from_file("armor_types")
    effect = read_text.get_from_file("effects")
    race = read_text.get_from_file("race")
    person = read_text.get_from_file("people")
    quality = read_text.get_from_file("quality")
    skill_rank = read_text.get_from_file("skill_rank")
    armor = read_text.get_from_file("armor_sfw") if skill_rank == "Novice" else read_text.get_from_file("armor")
    school = read_text.get_from_file("schools")
    choices = [
        f"{adjective} {armor} of {effect}",
        f"{armor_type} {armor} of {effect}",
        f"{adjective} {race} {armor} of {effect}",
        f"{person} {adjective} {armor}",
        f"{adjective} {armor} of {effect}",
        f"{quality} {person}'s {adjective} {armor}",
        f"{quality} {armor_type} {armor}",
        f"{quality} {person}'s {armor}",
        f"{skill_rank} {armor} of {adjective} {effect}",
        f"{adjective} {skill_rank} {armor}",
        f"{adjective} {armor} of {effect}",
        f"{skill_rank} {armor} of {school}",
    ]
    return random.choice(choices)


def shout():
    prefix = "Word of Power Learned: "
    action = read_text.get_from_file("actions")
    adjective = read_text.get_from_file("adjectives")
    misc = read_text.get_from_file("misc")
    effect = read_text.get_from_file("effects")
    poison_rank = read_text.get_from_file("poisonrank")
    weapon = read_text.get_from_file("weapons")
    choices = [
        f"{action} {adjective} {misc}",
        f"{action} {adjective} {effect}",
        f"{action} {poison_rank} {effect}",
        f"{weapon} {adjective} {misc}"
    ]
    return prefix + random.choice(choices)


def spell():
    prefix = "Spell Tome: "
    action = read_text.get_from_file("actions")
    second_action = read_text.get_from_file("actions")
    person = read_text.get_from_file("people")
    adjective = read_text.get_from_file("adjectives")
    misc = read_text.get_from_file("misc")
    effect = read_text.get_from_file("effects")
    alter = read_text.get_from_file("alter")
    choices = [
        f"{action} {person}",
        f"{adjective} {action}",
        f"{adjective} {misc}",
        f"{adjective} {effect}",
        f"{action} {second_action}",
        f"{alter} {misc}"
    ]
    return prefix + random.choice(choices)


def potion():
    prefix = "Potion of "
    adjective = read_text.get_from_file("adjectives")
    effect = read_text.get_from_file("effects")
    action = read_text.get_from_file("actions")
    person = read_text.get_from_file("people")
    misc = read_text.get_from_file("misc")
    alter = read_text.get_from_file("alter")
    body_part = read_text.get_from_file("body_parts")
    choices = [
        f"{adjective} {effect}",
        f"{action} {effect}",
        f"{adjective} {person}",
        f"{action} {misc}",
        f"{alter} {body_part}",
        f"{adjective} {body_part}"
    ]
    return prefix + random.choice(choices)


def misc():
    adjective = read_text.get_from_file("adjectives")
    misc = read_text.get_from_file("misc")
    effect = read_text.get_from_file("effects")
    person = read_text.get_from_file("people")
    race = read_text.get_from_file("race")
    choices = [
        f"{adjective} {misc} of {effect}",
        f"{adjective} {misc}",
        f"{person}'s {misc} of {effect}",
        f"{person}'s {misc}",
        f"{adjective} {race}",
    ]
    return random.choice(choices)

def blessing():
    divine = read_text.get_from_file("divines")
    daedric_lord = read_text.get_from_file("daedric_lord")
    effect = read_text.get_from_file("effects")
    adjective = read_text.get_from_file("adjectives")
    choices = [
        f"{divine}'s Blessing of {effect}",
        f"{daedric_lord}'s Curse of {effect}",
        f"{divine}'s {adjective} Curse",
        f"{divine}'s {adjective} Blessing",
        f"{daedric_lord}'s {adjective} Curse",
        f"{daedric_lord}'s {adjective} Blessing",
    ]
    return random.choice(choices)


def disease():
    return "Disease"


def objective():
    adjective = read_text.get_from_file("adjectives")
    object = read_text.get_from_file("objects")
    daedric_lord = read_text.get_from_file("daedric_lord")
    divine = read_text.get_from_file("divines")
    npc = read_text.get_from_file("npcs")
    other_npc = read_text.get_from_file("npcs")
    vicinity = read_text.get_from_file("vicinity")
    location = read_text.get_from_file("location")
    action = read_text.get_from_file("actions")
    adj_obj = f"{adjective} {object}"
    retrieve_obj = random.choices([f"{adj_obj}", armor(), weapon()], [10, 20, 20])[0]
    quest_character = random.choices([npc, daedric_lord, divine], [90, 30, 10])[0]
    npc_action = read_text.get_from_file("actions_target_npc")
    obj_action = read_text.get_from_file("actions_target_obj")
    assist_npc = random.choice(["for", "on behalf of", "with the help of"])
    assist_obj = random.choice(["using", "with", "wielding", "with the help of"])
    get_word = random.choice(["Get", "Steal", "Take", "Pick up", "Obtain"])
    choices = [
        f"Return the {retrieve_obj} to {quest_character}",
        f"Meet {npc} {vicinity} {location} with the {random.choice([weapon(), armor()])}",
        f"Defeat {npc} {vicinity} {location}{random.choices(['', f' {assist_obj} the {weapon()}'], [70, 30])[0]}",
        f"{get_word} the {retrieve_obj} from {location} {assist_npc} {quest_character}",
        f"{get_word} the {retrieve_obj} from {location}",
        f"{get_word} the {retrieve_obj} from {quest_character}",
        f"Travel to {location} to {obj_action.lower()} the {random.choice([weapon(), armor()])}",
        f"Tell {quest_character} about the {random.choice([weapon(), armor()])}",
        f"Go to {location} to {npc_action.lower()} {quest_character}",
        f"{npc_action} {quest_character} {assist_obj} the {random.choice([weapon(), armor()])}",
        f"Find a way to bestow {blessing()} upon {quest_character}"
    ]
    return "New Objective: " + random.choice(choices)
