import random

from read_text import get_all_lines_from_file
from text.load_helpers import (
    get_body_part,
    get_npc,
    get_person,
    get_daedric_lord,
    get_divine, get_race, get_location, get_faction, get_creature, get_adverb,
)
from text.format import pluralize, possessive


def assist_phrase_npc() -> str:
    return random.choice(
        [
            "for",
            "on behalf of",
            "with the help of",
        ]
    )


def assist_phrase_object() -> str:
    return random.choice(
        [
            "using",
            "with",
            "wielding",
            "with the help of",
        ]
    )


def conditional_adjective(
    target_str: str, format_as_plural: bool = False, probability: int = 70
) -> str:
    """
    Roughly 30% chance to prefix the given string with an adjective. Automatically filters out certain adjectives if the
    target string is a fantasy race to avoid bad vibes.
    """
    formatted_target_str = pluralize(target_str) if format_as_plural else target_str
    if random.randint(1, 100) >= probability:
        lines = get_all_lines_from_file("adjectives")
        races = [r.lower() for r in get_all_lines_from_file("race")]
        if target_str.lower() in races or any(
            r.lower() in target_str.lower() for r in races
        ):
            lines = [
                l
                for l in lines
                if l not in get_all_lines_from_file("adjectives_exclude_person")
            ]
        return f"{random.choice(lines).lower()} {formatted_target_str}"
    return formatted_target_str


def major_minor():
    return random.choice(["Major", "Minor"])


def objective_at_location():
    return random.choice(
        [
            "Clear out",
            "Destroy",
            "Repair",
            "Clean",
            "Defend",
            "Annihilate",
        ]
    )


def object_suffix():
    suffix = ""
    gold_value = random.choices(
        [random.randint(1, 100), random.randint(1, 1000), random.randint(1, 10000)],
        [1, 3, 1],
    )[0]
    if random.randint(1, 10) >= 9:
        suffix += " [STOLEN]"
    return (
        suffix
        + random.choices(
            [
                " added to inventory",
                " removed from inventory",
                f" sold for {gold_value} gold",
                f" equipped to {get_body_part()}",
                f" repaired for {gold_value} gold",
                f" purchased for {gold_value} gold",
                "",
            ],
            [10, 10, 10, 5, 10, 10, 85],
        )[0]
    )


def group_creature(noun: str) -> str:
    singular_suffix_groups = ["hive", "nest"]
    plural_prefix_groups = ["pack", "group", "clan", "gang", "flock"]
    choices = []
    choices += [f"{noun} {group}" for group in singular_suffix_groups]
    choices += [f"{group} of {pluralize(noun)}" for group in plural_prefix_groups]
    return random.choice(choices)


def group_generic_npc(generic_npc: str, adjective_probability: int = 70):
    group_types = [
        "swarm",
        "gang",
        "council",
        "cult",
        "congregation",
        "pack",
        "team",
    ]
    group_types_only_suffix = [
        "crew",
        "power couple",
        "duo",
        "trio",
        "clique",
        "cabal",
        "posse",
        "polycule",
        "community",
    ]
    group_types_only_prefix = ["band"]
    selections = []
    selections += [
        f"{t} of {conditional_adjective(generic_npc, True, adjective_probability)}"
        for t in group_types + group_types_only_prefix
    ]
    selections += [f"{generic_npc} {t}" for t in group_types + group_types_only_suffix]
    choice = random.choice(selections)
    return (
        f"the {conditional_adjective(choice, False, probability=adjective_probability)}"
    )


def get_person_or_npc(singular_only: bool = False):
    if singular_only:
        return random.choices(["the " + get_person(), get_npc()], [30, 20])[0]
    return random.choices(
        ["the " + conditional_adjective(get_person(), probability=20), "the " + conditional_adjective(get_race(), probability=20), group_generic_npc(get_person()), get_npc()],
        [20, 20, 15, 10],
    )[0]


def get_quest_character():
    return random.choices(
        [
            get_person_or_npc(),
            get_daedric_lord(),
            get_divine(),
        ],
        [65, 20, 10],
    )[0]


def get_healing_improving_word():
    return random.choice(
        [
            "heal",
            "restore",
            "cure",
            "mend",
            "soothe",
            "treat",
        ]
    )


def get_travel_word():
    return random.choice(
        [
            "Travel to",
            "Hurry to",
            "Rush to",
            "Journey to",
            "Set off for",
            "Seek out",
            "Find",
            "Visit",
            "Return to",
            "Locate",
            "Crawl towards",
        ]
    )


def get_defeat_word():
    return random.choice(
        [
            "Kill",
            "Confront",
            "Defeat",
            "Vanquish",
            "Accost",
            "Ambush",
            "Eradicate",
            "Destroy",
            "Eliminate",
            "Take out",
            "Slay",
            "Dominate",
            "Overthrow",
            "Crush",
            "Finish off",
        ]
    )


def get_affinity_word():
    return random.choice(
        [
            "favorite",
            "precious",
            "prized",
            "beloved",
            "heirloom",
            "priceless",
            "revered",
            "cherished",
            "treasured",
            "trusty",
        ]
    )


def get_resolution_phrase():
    named_npc = get_npc()
    possessive_named_npc = possessive(named_npc)
    faction = get_faction()
    return random.choice([
        " once and for all",
        ", no matter the consequences",
        ", no matter the cost",
        f", despite {possessive_named_npc} warnings",
        ", risking both life and limb in the process",
        " and finish the job",
        " and end this madness",
        ", even if it kills you",
        f", even if it means suffering the {conditional_adjective('consequences', probability=40)}",
        ", whatever the cost may be",
        f" and see this through til the {conditional_adjective('end', probability=0)}",
        f", whatever it takes ",
        f", to win back {possessive_named_npc} affection",
        f", to secure a position in {possessive_named_npc} inner circle",
        f", despite the risk this poses to your {get_body_part().lower()}",
        f", even though {named_npc} disagrees",
        f" behind {possessive_named_npc} back",
        f", even in the face of certain doom",
        f", as a final act of defiance",
        f", knowing that this could change everything",
        f", with or without {possessive_named_npc} blessing",
        f". There's no going back now.",
        f", it's what {named_npc} would have wanted.",
        f", or risk losing your status with {faction}",
        f", against the wishes of {faction}",
        f" to complete your initiation into {faction}",
        f" to impress the members of {faction}",
    ])


def conditional_resolution_phrase(probability: int = 65, string: str = ""):
    if random.randint(1, 100) >= probability:
        return f"{string}{get_resolution_phrase()}"
    return string


def conditional_adverb(probability: int = 65, string: str = ""):
    adverb = get_adverb()
    if random.randint(1, 100) >= probability:
        return f"{adverb} {string}"
    return string


def get_location_relationship_phrase():
    return random.choice(
        [
            "operating out of",
            "living in",
            "working out of",
            "residing in",
            f"doing their {conditional_adjective('business in', probability=20)}"
        ]
    )


def get_end_relationship_phrase(npc_name: str):
    return random.choice(
        [
            f"Break off your engagement with {npc_name}",
            f"Break up with {npc_name}",
            f"Divorce {npc_name}",
            f"Remove {npc_name} from your polycule",
            f"Tell {npc_name} that you no longer feel the same way about them",
            f"Cut ties with {npc_name}",
            f"Call it quits with {npc_name}",
            f"Ask {npc_name} to move out of your shared home in {get_location()}",
            f"Sever your bond with {npc_name}",
            f"End your casual relationship with {npc_name}",
        ]
    )


def get_quest_update_prefix() -> str:
    return random.choice([
        "Quest updated:",
        "Quest failed:",
        "New objective:",
        "Journal updated:",
        "Objective failed:",
        "Quest added:",
        "Quest completed:",
        "Objective complete:"
    ])