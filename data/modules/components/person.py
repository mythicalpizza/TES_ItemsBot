from components.enums.faction import Faction
from components.enums.race import Race
from components.enums.skillgroup import SkillGroup
from components.enums.homecity import HomeCity

class Person():
    def __init__(self, name, race, faction, skillgroup = SkillGroup.COMBAT, homecity = HomeCity.RANDOM):
        self.name = name
        self.race = race
        self.faction = list(faction)
        self.skillgroup = skillgroup
        self.homecity = homecity
