from modules.components.enums.moralalignment import MoralAlignment


class Deity():
    def __init__(self, name, moralalignment):
        self.name = name#Used to identify deity
        self.moralalignment = moralalignment#Identifies deity primary demeanor
