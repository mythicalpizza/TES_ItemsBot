from modules.components.enums.faction import Faction
from modules.components.enums.race import Race
from modules.components.enums.skillgroup import SkillGroup
from modules.components.enums.homecity import HomeCity

from modules.components.person import Person


beggars = [
    Person("Penniless Olvus", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.ANVIL)
]

print(beggars[0].name)
