# What a robot is and how random parts are made.
import random

part_types = ["legs", "torso", "arms", "head"]

tier_names = {
    0: "The Pile",
    1: "Scrap bot",
    2: "Toy bot",
    3: "Service bot",
    4: "Companion bot",
    5: "Eco bot",
}

class Part:
    def __init___(self, partType, tier):
        self.partType = partType
        self.tier = tier

    def name(self):
        return tier_names[self.tier] + " " + self.partType.title()

    def imagePath(self):
        # Art team saves images with these names so the program can find the right picture for any part
        return "assets/" + self.partType + "/tier" + str(self.tier) + ".png"

    def createOffers(partType):
        # Make 3 parts of one type, each one being a different, random tier
        tiers = random.sample([0, 1, 2, 3, 4, 5], 3)

        # Turns each tier number into a part e.g. [5, 2, 4] -> Eco bot, Toy bot, Companion bot
        offers = []
        for tier in tiers:
            offers.append(Part(partType,tier))
        return offers