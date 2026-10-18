# What a robot part is and how random parts are made.
import random

part_types = ["legs", "body", "arms", "head"] # build order from bottom to top

tier_names = {
    0: "pile",
    1: "scrap",
    2: "toy",
    3: "service",
    4: "companion",
    5: "eco",
}

class Part:
    def __init__(self, partType, tier, image):
        self.partType = partType
        self.tier = tier
        self.value = (tier + 1) * 20
        #image will be part + tier key (eg: pile_legs.png)
        self.image = image

    def name(self):
        # e.g. "The toy bot legs"
        return "The " +tier_names[self.tier] + " bot " + self.partType.title()

    def imagePath(self):
        # Art team saves images with these names so the program can find the right picture for any part
        #assets/legs/pile_legs.png
        return "assets/" + self.partType + "/" + self.image

    def getImage(self):
        return self.image

    def getValue(self):
        return self.value



class Robot:
    def __init__(self, type):
        if type == "player":
            self.parts = [None, None, None, None]
        else:
            self.parts[Part(0,random.randint(0,5)), Part(1,random.randint(0,5)), Part(2,random.randint(0,5)), Part(3,random.randint(0,5))]

    def assemble(self, partType, part):
        self.parts[partType] = part

    def getParts(self, partType):
        return self.parts