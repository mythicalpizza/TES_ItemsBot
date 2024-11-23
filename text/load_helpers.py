import random
from typing import Optional

from select import select

from read_text import get_from_file, get_lines_from_file


def get_action():
    return get_from_file("actions")

def get_action_target_npc():
    return get_from_file("actions_target_npc")

def get_action_target_obj():
    return get_from_file("actions_target_obj")

def get_adjective():
    return get_from_file("adjectives")

def get_alter():
    return get_from_file("alter")

def get_armor(skill_rank: Optional[str] = None):
    if skill_rank == "Novice":
        return get_from_file("armor_sfw")
    return get_from_file("armor")

def get_armor_type():
    return get_from_file("armor_types")

def get_body_part():
    return get_from_file("body_parts")

def get_daedric_lord():
    return get_from_file("daedric_lord")

def get_divine():
    return get_from_file("divines")

def get_effect():
    return get_from_file("effects")

def get_gem():
    return get_from_file("gem")

def get_jewelry():
    return get_from_file("jewelry")

def get_jewelry_type():
    return get_from_file("jewelry_types")

def get_location():
    return get_from_file("location")

def get_location_type():
    return get_from_file("location_type")

def get_misc():
    return get_from_file("misc")

def get_npc():
    return get_from_file("npcs")

def get_object():
    return get_from_file("objects")

def get_person():
    return get_from_file("people")

def get_poison_rank():
    return get_from_file("poisonrank")

def get_quality():
    return get_from_file("quality")

def get_race():
    return get_from_file("race")

def get_school():
    return get_from_file("schools")

def get_skill_rank():
    return get_from_file("skill_rank")

def get_vicinity():
    return get_from_file("vicinity")

def get_weapon_type():
    return get_from_file("weapon_types")

def get_weapon():
    return get_from_file("weapons")

def get_effect_that_is_also_noun():
    return random.choice([l for l in get_lines_from_file("effects") if not (l.endswith("ing"))])

def get_person_or_npc():
    return random.choices(
        [
            "the " + get_person(),
            generic_npc_group(get_person()),
            get_npc()
        ], [30, 70, 20]
    )[0]

def get_location_or_type():
    return random.choices(
        [
        "the " + get_location_type(),
        get_location()
            ],
        [80, 20]
    )[0]

def get_potential_adjective():
    adjective = get_adjective()
    if adjective in ["illegal"]:
        return ""
    if random.randint(1, 10) >= 7:
        return f"{get_adjective().lower()} "
    return ""

def generic_npc_group(generic_npc: str, singular: bool = False):
    race = get_race()
    if race != "Redguard":
        # avoid being racist
        generic_npc = random.choice([generic_npc, race])
    if random.randint(1, 1000) == 1000:
        # extremely rare chance that a proper noun is treated as a generic for funny
        generic_npc = get_npc()
    if generic_npc.startswith("the "):
        generic_npc = generic_npc[4:]
    plural = f"{generic_npc}s"
    if generic_npc.endswith("y"):
        plural = f"{generic_npc[:-1]}ies"
    if any(generic_npc.endswith(x) for x in ["s", "ss", "sh", "ch", "x", "z"]):
        plural = f"{generic_npc}es"
    if generic_npc.endswith("f"):
        plural = f"{generic_npc[:-1]}ves"
    group_types = ["swarm", "gang", "council", "cult", "congregation", "pack", "team"]
    group_types_only_suffix = ["crew", "power couple", "duo", "trio", "clique", "club", "cabal", "posse", "polycule", "community"]
    group_types_only_prefix = ["band"]
    selections = []
    if not singular:
        selections += [
            f"{t} of {get_potential_adjective()}{plural}" for t in group_types + group_types_only_prefix
        ]
    selections += [
        f"{generic_npc} {t}" for t in group_types + group_types_only_suffix
    ]
    if generic_npc.startswith("g"):
        selections.append(f"gaggle of {plural}")
    if random.randint(1, 10) >= 9:
        return "the " + get_adjective().lower() + " " + random.choice(selections)
    return "the " + random.choice(selections)

def get_quest_character():
    return random.choices([
        get_npc(),
        get_daedric_lord(),
        get_divine(),
        generic_npc_group(get_person()),
        "the " + get_person(),
    ], [65, 10, 10, 40, 10])[0]

def get_adjective_object():
    return f"{get_adjective()} {get_object()}"

