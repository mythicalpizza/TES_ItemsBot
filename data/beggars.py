from modules.components.enums.faction import Faction
from modules.components.enums.race import Race
from modules.components.enums.skillgroup import SkillGroup
from modules.components.enums.homecity import HomeCity

from modules.components.person import Person


beggars = [
    Person("Penniless Olvus", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.ANVIL),
    Person("Imus the Dull", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.ANVIL),
    Person("Wretched Aia", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.BRAVIL),
    Person("Cosmus the Cheat", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.BRAVIL),
    Person("Jorck the Outcast", Race.NORD, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.BRUMA),
    Person("Fetid Jofnhild", Race.NORD, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.BRUMA),
    Person("Bruccius the Orphan", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.CHEYDINHAL),
    Person("Luckless Lucina", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.CHEYDINHAL),
    Person("Nermus the Mooch", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.CHORROL),
    Person("Lazy Kaslowyn", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.CHORROL),
    Person("Simplicia the Slow", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.IMPERIALCITY),
    Person("No-Coint Draninus", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.IMPERIALCITY),
    Person("Ragbag Buntara", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.IMPERIALCITY),
    Person("Puny Ancus", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.IMPERIALCITY),
    Person("Deeh the Scalawag", Race.ARGONIAN, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.LEYAWIIN),
    Person("Rancid Ra'dirsha", Race.KHAJIIT, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.LEYAWIIN),
    Person("Nigidius the Needy", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.SKINGRAD),
    Person("Foul Fagus", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.SKINGRAD),
    Person("No-Coins Draninus", Race.IMPERIAL, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.IMPERIALCITY),
    Person("Fimmion", Race.WOODELF, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.BLISS),
    Person("Uungor", Race.WOODELF, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.BLISS),
    Person("Bhisha", Race.KHAJIIT, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.CRUCIBLE),
    Person("Bolwing", Race.WOODELF, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.CRUCIBLE),
    Person("Gloorolros", Race.WOODELF, [Faction.BEGGARS], SkillGroup.STEALTH, HomeCity.CRUCIBLE)
]

"""
I am assigning skillgroups primarily based on Oblivion's approach, which is derived from the NPC class specified on the UESP wiki.
Beggars in Oblivion nearly exclusively have the "Commoner" class, which has a primary skill group type of stealth.
"""
