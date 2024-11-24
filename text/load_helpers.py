import random
from typing import Optional, List

from read_text import get_random_line_from_file, get_all_lines_from_file
from text.format import pluralize


def get_action() -> str:
    """
    Get an action
    """
    return get_random_line_from_file("actions")


def get_action_target_npc() -> str:
    """
    Get an action that makes sense to perform on a person
    """
    lines = get_all_lines_from_file("actions")
    lines = [
        l for l in lines if l not in get_all_lines_from_file("actions_exclude_person")
    ]
    return random.choice(lines)


def get_action_target_obj() -> str:
    """
    Get an action that makes sense to perform on an Object
    """
    lines = get_all_lines_from_file("actions")
    lines = [
        l for l in lines if l not in get_all_lines_from_file("actions_exclude_object")
    ]
    return random.choice(lines)


def get_adjective() -> str:
    return get_random_line_from_file("adjectives")


def get_alter() -> str:
    return get_random_line_from_file("alter")


def get_armor(skill_rank: Optional[str] = None) -> str:
    if skill_rank == "Novice":
        return random.choice(
            [
                f
                for f in get_all_lines_from_file("armor")
                if f not in get_all_lines_from_file("armor_restricted")
            ]
        )
    return get_random_line_from_file("armor")


def get_armor_type() -> str:
    return get_random_line_from_file("armor_types")


def get_body_part() -> str:
    return get_random_line_from_file("body_parts")


def get_daedric_lord() -> str:
    return get_random_line_from_file("daedric_lord")


def get_divine() -> str:
    return get_random_line_from_file("divines")


def get_effect() -> str:
    return get_random_line_from_file("effects")


def get_gem() -> str:
    return get_random_line_from_file("gem")


def get_jewelry() -> str:
    return get_random_line_from_file("jewelry")


def get_jewelry_type() -> str:
    return get_random_line_from_file("jewelry_types")


def get_location() -> str:
    return get_random_line_from_file("location")


def get_location_type() -> str:
    return get_random_line_from_file("location_type")


def get_misc() -> str:
    return get_random_line_from_file("misc")


def get_npc() -> str:
    return get_random_line_from_file("npcs")


def get_object() -> str:
    return get_random_line_from_file("objects")

def get_adverb() -> str:
    return get_random_line_from_file("adverbs")

def get_person() -> str:
    return get_random_line_from_file("people")


def get_poison_rank() -> str:
    return get_random_line_from_file("poisonrank")


def get_quality() -> str:
    return get_random_line_from_file("quality")


def get_race() -> str:
    return get_random_line_from_file("race")


def get_school() -> str:
    return get_random_line_from_file("schools")


def get_skill_rank() -> str:
    return get_random_line_from_file("skill_rank")


def get_vicinity() -> str:
    return get_random_line_from_file("vicinity")


def get_weapon_type() -> str:
    return get_random_line_from_file("weapon_types")


def get_faction() -> str:
    return get_random_line_from_file("faction")


def get_weapon() -> str:
    return get_random_line_from_file("weapons")


def get_noun_effect() -> str:
    return random.choice(
        [l for l in get_all_lines_from_file("effects") if not (l.endswith("ing"))]
    )


def get_ing_effect() -> str:
    return random.choice(
        [l for l in get_all_lines_from_file("effects") if l.endswith("ing")]
    )


def get_obtain_word() -> str:
    return get_random_line_from_file("obtain_words")


def get_potential_adjective():
    adjective = get_adjective()
    if adjective in ["illegal"]:
        return ""
    if random.randint(1, 10) >= 7:
        return f"{get_adjective().lower()} "
    return ""


def get_creature(plural: bool = False):
    creatures = get_all_lines_from_file("creature")
    if plural:
        creatures = [pluralize(c) for c in creatures]
    return random.choice(creatures)


def get_adjective_object():
    return f"{get_adjective()} {get_object()}"


def get_magnitude() -> str:
    choices: List[str] = [f"{i} " for i in get_all_lines_from_file("magnitude")]
    choices += [""]
    return random.choice(choices)
