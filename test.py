import time
import forge
from text import generic_npc_group, get_person


def timed_test(seconds):
    start_time = time.time()
    iterations = 0

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        print(forge.item())
        iterations += 1

        if elapsed_time > seconds:
            print("Test completed. " + str(iterations) + " items generated in " + str(seconds) + " second(s).")
            break


def test_all_forge_functions():
    gens = [
        "weapon: " + forge.weapon(),
        "armor: " + forge.armor(),
        "misc: " + forge.misc(),
        "armor: " + forge.armor(),
        "spell: " + forge.spell(),
        "objective: " + forge.objective(),
        "blessing: " + forge.blessing(),
        "disease: " + forge.disease(),
        "potion: " + forge.potion(),
        "generic_npc_group: " + generic_npc_group(get_person()),
    ]
    for item in gens:
        print(item)


if __name__ == "__main__":
    test_all_forge_functions()
    print("======")
    for _ in range(1, 200):
        print(forge.item())
