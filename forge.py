import random
from math import factorial
from typing import Optional

import config
from text.format import possessive, smart_title_case, pluralize
from text.load_helpers import (
    get_adjective,
    get_weapon_type,
    get_weapon,
    get_effect,
    get_race,
    get_armor_type,
    get_person,
    get_quality,
    get_skill_rank,
    get_armor,
    get_school,
    get_action,
    get_misc,
    get_poison_rank,
    get_alter,
    get_body_part,
    get_jewelry_type,
    get_gem,
    get_jewelry,
    get_divine,
    get_daedric_lord,
    get_vicinity,
    get_location,
    get_adjective_object,
    get_action_target_npc,
    get_action_target_obj,
    get_noun_effect,
    get_npc,
    get_creature,
    get_obtain_word,
    get_ing_effect, get_faction,
)
from text.phrase_generators import (
    major_minor,
    object_suffix,
    assist_phrase_object,
    assist_phrase_npc,
    group_generic_npc,
    get_person_or_npc,
    get_quest_character,
    get_healing_improving_word,
    conditional_adjective,
    get_travel_word,
    get_defeat_word,
    group_creature,
    get_affinity_word, get_resolution_phrase, conditional_resolution_phrase, get_location_relationship_phrase,
    get_end_relationship_phrase, get_quest_update_prefix, conditional_adverb,
)


def item():
    varieties = {
        "weapon": (weapon, 50),
        "armor": (armor, 50),
        "shout": (shout, 40),
        "spell": (spell, 30),
        "potion": (potion, 30),
        "misc": (misc, 30),
        "blessings": (blessing, 20),
        "diseases": (disease, 30),
        "objectives": (objective, 60),
        "jewelry": (jewelry, 30),
    }

    flags = config.get_json("flags.json")
    for feature in ["blessings", "diseases", "objectives", "jewelry"]:
        if config.is_disabled(flags.get(feature, "disabled")):
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
        f"{adjective} {weapon} of {magnitude} {effect}",
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
    group = group_generic_npc(person)
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
        f"{quality} {possessive(person)} {adjective} {armor}",
        f"{quality} {armor_type} {armor}",
        f"{quality} {possessive(person)} {armor}",
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
        f"{weapon} {adjective} {misc}",
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
        f"{alter} {misc}",
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
        f"{adjective} {body_part}",
    ]
    return prefix + random.choice(choices)


def misc(exclude_groups: bool = False):
    adjective = get_adjective()
    misc = get_misc()
    effect = get_effect()
    person = get_person()
    race = get_race()
    group = group_generic_npc(person)
    if not exclude_groups:
        p = smart_title_case(random.choice([person, group]))
    else:
        p = person
    choices = [
        f"{adjective} {misc} of {effect}",
        f"{adjective} {misc}",
        f"{possessive(p)} {misc} of {effect}",
        f"{possessive(p)} {misc}",
        smart_title_case(conditional_adjective(race, probability=0)),
    ]
    return random.choice(choices)


def jewelry():
    quality = get_quality()
    jewelry_type = get_jewelry_type()
    gem = get_gem()
    jewelry = get_jewelry()
    effect = get_effect()
    person = get_person_or_npc().replace("the ", "").title().replace("Of", "of")
    adjective = get_adjective()
    choices = [
        f"{adjective} {jewelry_type} {jewelry} of {effect}",
        f"{adjective} {jewelry_type} and {gem} {jewelry} of {effect}",
        f"{possessive(person)} {jewelry_type} {jewelry} of {effect}",
        f"{possessive(person)} {jewelry_type} and {gem} {jewelry} of {effect}",
        f"{possessive(person)} {jewelry_type} {jewelry} of {effect}",
        f"{possessive(person)} {adjective} {jewelry} of {effect}",
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


def objective(debug: Optional[bool] = False):
    npc = smart_title_case(get_person_or_npc()).replace("The", "the")
    vicinity = get_vicinity()
    location = get_location()
    adj_obj = get_adjective_object()
    retrieve_obj = random.choices(
        [f"{adj_obj}", armor(True), weapon(True)], [10, 20, 20]
    )[0]
    quest_character = smart_title_case(get_quest_character()).replace("The", "the")
    npc_action = get_action_target_npc()
    obj_action = get_action_target_obj()
    named_npc = get_npc()
    body_part = get_body_part().lower()
    collectible_body_part = body_part if body_part.endswith("s") else f"a {body_part}"
    effect = get_noun_effect()
    weapon_or_armor = random.choice([weapon(True), armor(True)])
    non_group_npc = random.choice(["the " + get_person(), get_npc()])
    group = smart_title_case(group_generic_npc(get_person())).replace("The", "the")
    creatures = get_creature(True)
    creature = get_creature()
    creature_group = smart_title_case(group_creature(creature)).replace("The", "the")
    obtain_word = get_obtain_word()
    ing_effect = get_ing_effect()
    divine = get_divine()
    healing_improving_word = get_healing_improving_word()
    travel_phrase = get_travel_word()
    defeat_phrase = get_defeat_word()
    magic_school = get_school()
    random_num = random.randint(2,10)
    faction = get_faction()
    plural_non_group_generic_npc = pluralize(random.choice([get_person(), get_race()]))

    choices = [
        f"Return the {retrieve_obj} to {quest_character}{conditional_resolution_phrase()}",
        f"Meet {npc} {vicinity} {location} with the {weapon_or_armor}",
        f"{defeat_phrase} {npc} {vicinity} {location}{random.choices(['', f' {assist_phrase_object()} the {weapon(True)}'], [70, 30])[0]}",
        f"{defeat_phrase} {npc} {assist_phrase_object()} the {weapon(True)}",
        f"{defeat_phrase} {npc} {vicinity} {location}{get_resolution_phrase()}",
        f"{obtain_word} the {retrieve_obj} from {location} {assist_phrase_npc()} {quest_character}",
        f"{obtain_word} the {retrieve_obj} from {location}",
        f"{obtain_word} the {retrieve_obj} from {npc}",
        f"Convince {non_group_npc} to {conditional_adverb(probability=50, string='remove').lower()} their {random.choice([get_armor().lower(), armor(True)])}{get_resolution_phrase()}",
        f"Take back your {get_affinity_word()} {retrieve_obj} from {npc}{conditional_resolution_phrase()}",
        f"Collect {collectible_body_part} from the {creature_group}{get_resolution_phrase()}",
        f"Remove the cursed {armor(True)} {assist_phrase_npc()} {quest_character}",
        f"Retrieve {possessive(npc)} {get_affinity_word()} pet {creature} from {location}{conditional_resolution_phrase()}",
        f"Lure {npc} to {location} with their {get_affinity_word()} {get_adjective().lower()} {get_misc().lower()}",
        f"Help {named_npc} find their {get_affinity_word()} {get_adjective().lower()} {get_misc().lower()} {vicinity} {location}{conditional_resolution_phrase()}",
        f"{travel_phrase} {location} to {conditional_adverb(string=obj_action).lower()} the {weapon_or_armor}",
        f"Tell {quest_character} about the {weapon_or_armor}",
        f"Mount your {get_affinity_word()} {creature} and {travel_phrase.lower()} {location} within {random_num} days{conditional_resolution_phrase()}",
        f"Try to {conditional_adverb(string='demonstrate').lower()} your {ing_effect.lower()} abilities to {random.choice([group, faction])}{conditional_resolution_phrase()}",
        f"Prove your loyalty to {faction} by {ing_effect.lower()} your {body_part}",
        f"Prove your {magic_school} mastery to {random.choice([quest_character, faction])} by {conditional_adverb(string='demonstrating')} your {effect}",
        f"{travel_phrase} {location} to {conditional_adverb(string=npc_action.lower()).lower()} {npc}",
        f"{conditional_adverb(string=npc_action)} {quest_character} {assist_phrase_object()} the {weapon_or_armor}",
        f"Blend in with the {group} {get_location_relationship_phrase()} {location}{conditional_resolution_phrase(probability=40)}",
        f"Find a way to bestow {blessing(True)} upon {npc}",
        f"{travel_phrase } a temple of {divine} to {healing_improving_word} your {conditional_adjective(body_part, probability=30)}",
        f"Find a way to {conditional_adverb(string='free').lower()} {quest_character} from {blessing(False)}",
        f"{defeat_phrase} the {get_adjective().lower()} {faction.replace('The ', '').rstrip('s')} operatives {get_location_relationship_phrase()} {location}{get_resolution_phrase()}",
        f"Report back to {quest_character} about {random.choice([npc, 'the ' + weapon_or_armor])}{conditional_resolution_phrase(30)}",
        f"Contain the aftermath of {possessive(non_group_npc)} {effect.lower()}",
        f"Protect {quest_character} from {possessive(non_group_npc)} {effect.lower()}",
        f"{defeat_phrase} the {smart_title_case(random.choice([effect, body_part.rstrip('s')]))} Cultists {get_location_relationship_phrase()} {location}{get_resolution_phrase()}",
        f"{get_end_relationship_phrase(named_npc)}{conditional_resolution_phrase(probability=0)}",
        f"Ask the {plural_non_group_generic_npc} {vicinity} {location} about {possessive(named_npc)} whereabouts",
        f"Uncover the secrets of the {location} {plural_non_group_generic_npc}{get_resolution_phrase()}",
        f"{conditional_adverb(string=npc_action).lower()} {quest_character}{conditional_resolution_phrase(20)}",
        f"{conditional_adverb(probability=0, string=npc_action.lower())} {quest_character}{get_resolution_phrase()}",
    ]
    if debug:
        for choice in choices:
            print(choice)
    quest_prefix = random.choices(
        [
            get_quest_update_prefix(),
            "",
        ],
        [10, 70],
    )[0]
    return f"{quest_prefix} {random.choice(choices)}".strip()
