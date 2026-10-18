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

    def name(self):
        # e.g. "Toy bot Legs"
        return tier_names[self.tier] + " " + self.partType.title()

    def imagePath(self):
        # Art team saves images with these names so the program can find the right picture for any part
        return "assets/" + self.partType + "/tier" + str(self.tier) + ".png"



class Robot:
    def __init__(self, type):
        if type == "player":
            self.legs = None
            self.body = None
            self.arms = None
            self.head = None
        else:
            self.legs = Part(0,random.randint(0,5))
            self.body = Part(1,random.randint(0,5))
            self.arms = Part(2,random.randint(0,5))
            self.head = Part(3,random.randint(0,5))