# What a robot part is and how random parts are made.
import random

part_types = ["legs", "torso", "arms", "head"] # build order from bottom to top

tier_names = {
    0: "The Pile",
    1: "Scrap bot",
    2: "Toy bot",
    3: "Service bot",
    4: "Companion bot",
    5: "Eco bot",
}

class Part:
    def __init__(self, partType, tier):
        self.partType = partType
        self.tier = tier
        self.value = (tier + 1) * 20

    def name(self):
        # e.g. "Toy bot Legs"
        return tier_names[self.tier] + " " + self.partType.title()

    def imagePath(self):
        # Art team saves images with these names so the program can find the right picture for any part
        return "assets/" + self.partType + "/tier" + str(self.tier) + ".png"

    def getValue(self):
        return self.value



class Robot:
    def __init__(self, type):
        if type == "player":
            self.parts = [None, None, None, None]
        else:
            self.parts[Part(0,random.randint(0,5)), Part(1,random.randint(0,5)), Part(2,random.randint(0,5)), Part(3,random.randint(0,5))]

    def assemble(partType, part):
        self.parts[partType] = part

    def getStat(self, partType):
        return self.parts[partType].getValue
        
