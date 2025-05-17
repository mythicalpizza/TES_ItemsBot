from components.enums.faction import Faction
from components.enums.race import Race
from components.enums.skillgroup import SkillGroup
from components.enums.homecity import HomeCity

from components.person import Person


beggars = [
Person("Penniless Olvus", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.ANVIL)
]


#print(beggars[0].name)
