import random
from typing import Optional

import config
from text import *
from text.load_helpers import get_effect_that_is_also_noun


def item():
    varieties = {
        'weapon': (weapon, 50),
        'armor': (armor, 50),
        'shout': (shout, 40),
        'spell': (spell, 30),
        'potion': (potion, 30),
        'misc': (misc, 30),
        'blessings': (blessing, 20),
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


def weapon(standalone: bool = False):
    adjective = get_adjective()
    weapon = get_weapon()
    weapon_type = get_weapon_type()
    effect = get_effect()
    race = get_race()
    magnitude = major_minor()
    choices = [
        f"{adjective} {weapon} of {effect}",
        f"{weapon_type} {weapon} of {effect}",
        f"{adjective} {weapon}",
        f"{weapon_type} {weapon} of {effect}",
        f"{adjective} {race} {weapon} of {effect}",
        f"{adjective} {weapon} of {magnitude} {effect}"
    ]
    flags = config.get_json("flags.json")
    if standalone or flags.get("advanced_items", "enabled") == "disabled":
        return random.choice(choices)
    return random.choice(choices) + object_suffix()


def armor(standalone: bool = False):
    adjective = get_adjective()
    armor_type = get_armor_type()
    effect = get_effect()
    race = get_race()
    person = get_person()
    group = generic_npc_group(person)
    quality = get_quality()
    skill_rank = get_skill_rank()
    armor = get_armor(skill_rank)
    school = get_school()
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
    flags = config.get_json("flags.json")
    choice = random.choice(choices)
    if standalone or flags.get("advanced_items", "enabled") == "disabled":
        return choice
    if choice.lower().endswith("shoes") and random.randint(1, 100) == 100:
        return "For Sale: " + choice + " (Never Worn)"
    return choice + object_suffix()


def shout():
    prefix = "Word of Power Learned: "
    action = get_action()
    adjective = get_adjective()
    misc = get_misc()
    effect = get_effect()
    poison_rank = get_poison_rank()
    weapon = get_weapon()
    choices = [
        f"{action} {adjective} {misc}",
        f"{action} {adjective} {effect}",
        f"{action} {poison_rank} {effect}",
        f"{weapon} {adjective} {misc}"
    ]
    return prefix + random.choice(choices)


def spell():
    prefix = "Spell Tome: "
    action = get_action()
    second_action = get_action()
    person = get_person()
    adjective = get_adjective()
    misc = get_misc()
    effect = get_effect()
    alter = get_alter()
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
    adjective = get_adjective()
    effect = get_effect()
    action = get_action()
    person = get_person()
    misc = get_misc()
    alter = get_alter()
    body_part = get_body_part()
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
    adjective = get_adjective()
    misc = get_misc()
    effect = get_effect()
    person = get_person()
    race = get_race()
    group = "T" + generic_npc_group(person)[1:]
    p = random.choice([person, group])
    choices = [
        f"{adjective} {misc} of {effect}",
        f"{adjective} {misc}",
        f"{p}'s {misc} of {effect}",
        f"{p}'s {misc}",
        f"{adjective} {race}",
    ]
    return random.choice(choices)


def blessing(only_good: Optional[bool] = None):
    divine = get_divine()
    daedric_lord = get_daedric_lord()
    effect = get_effect()
    adjective = get_adjective()
    choices = []
    good_choices = [
        f"{divine}'s Blessing of {effect}",
        f"{divine}'s {adjective} Blessing",
        f"{daedric_lord}'s {adjective} Blessing",
    ]
    bad_choices = [
        f"{daedric_lord}'s Curse of {effect}",
        f"{divine}'s {adjective} Curse",
        f"{daedric_lord}'s {adjective} Curse",
    ]
    if only_good is None:
        choices += good_choices
        choices += bad_choices
    elif only_good:
        choices += good_choices
    else:
        choices += bad_choices
    return random.choice(choices)


def disease():
    return "Disease"


def objective():
    npc = get_person_or_npc()
    vicinity = get_vicinity()
    location = get_location()
    adj_obj = get_adjective_object()
    retrieve_obj = random.choices([f"{adj_obj}", armor(True), weapon(True)], [10, 20, 20])[0]
    quest_character = get_quest_character()
    npc_action = get_action_target_npc()
    obj_action = get_action_target_obj()
    body_part = get_body_part().lower()
    effect = get_effect_that_is_also_noun()
    if not body_part.endswith("s"):
        body_part = f"a {body_part}"
    weapon_or_armor = random.choice([weapon(True), armor(True)])
    non_group_npc = random.choice(["the " + get_person(), get_npc()])
    group = generic_npc_group(get_person())
    #
    choices = [
        f"Return the {retrieve_obj} to {quest_character}",
        f"Meet {npc} {vicinity} {location} with the {weapon_or_armor}",
        f"Defeat {npc} {vicinity} {location}{random.choices(['', f' {assist_phrase_object()} the {weapon(True)}'], [70, 30])[0]}",
        f"{obtain_word()} the {retrieve_obj} from {location} {assist_phrase_npc()} {quest_character}",
        f"{obtain_word()} the {retrieve_obj} from {location}",
        f"{obtain_word()} the {retrieve_obj} from {npc}",
        f"Collect {body_part} from {npc}",
        f"Travel to {location} to {obj_action.lower()} the {weapon_or_armor}",
        f"Tell {quest_character} about the {weapon_or_armor}",
        f"Go to {location} to {npc_action.lower()} {npc}",
        f"{npc_action} {quest_character} {assist_phrase_object()} the {weapon_or_armor}",
        f"Find a way to bestow {blessing(True)} upon {npc}",
        f"Find a way to free {quest_character} from {blessing(False)}",
        f"Report back to {quest_character} about the {random.choice([npc, weapon_or_armor])}",
        f"Contain the aftermath of {non_group_npc}'s {effect.lower()}",
        f"Protect {quest_character} from {non_group_npc}'s {effect.lower()}",
    ]
    quest_prefix = random.choice(
        ["New Objective: ", "", "Quest Log Updated: ", "Objective Completed: ", "Quest Failed: "])
    return quest_prefix + random.choice(choices)
