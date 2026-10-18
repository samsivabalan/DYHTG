# The rules of the game
# main.py calls leftKeyPress() / rightKeyPress() when a key is pressed,
# and reads te variables below to decide what to draw
# It sets up an empty robot and startBuilding() empties it again at the start of every new game

from parts import part_types, tier_names, createOffers
from battle import Battle

class Game:
    def __init__(self):
        self.gameState = "menu" # Either "menu", "building" or "battle"
        self.running = True # Window closes when False

        # The robot starts with no parts as we are building it from scratch
        self.robot = [] # parts the player has accepted, in build order
        self.parts = [] # 4 lists, one per body part, 3 offers in each
        self.partIndex = 0 # body part: 0 legs, 1 torso, 2 arms, 3 head
        self.offerIndex = 0 # offer on screen: 0, 1 or 2
        self.battle = None # no battle until the robot is finishe

    def leftKeyPress(self):
        match self.gameState:
            case "menu":
                self.startBuilding() # begin building process
            case "building":
                self.acceptPart() # accept piece, send to robot
            case "battle":
                self.battle.leftAction() # attack
                self.checkBattleOver()

    def rightKeyPress(self):
        match self.gameState:
            case "menu":
                self.running = False # quit game
            case "building":
                self.rejectPart() # refuse piece, get next
            case "battle":
                self.battle.rightAction() # other attack
                self.checkBattleOver()

    # building process

    def createOffers(self, partType):
        # Make 3 parts of one type, each one being a different, random tier
        tiers = random.sample([0, 1, 2, 3, 4, 5], 3)

        # Turns each tier number into a part e.g. [5, 2, 4] -> Eco bot, Toy bot, Companion bot
        offers = []
        for tier in tiers:
            offers.append(Part(partType,tier))
        return offers

    def startBuilding(self):
        # Runs at the start of every game, so it resets everything
        self.gameState = "building"
        self.robot = []

        # 4 lists, one per body part, each holding 3 random parts
        self.parts = []
        for partType in part_types:
            self.parts.append(self.createOffers(partType))

        self.partIndex = 0 # start on the legs
        self.offerIndex = 0 #start on the first offer

    def currentPart(self):
        return self.parts[self.partIndex][self.offerIndex]

    def isLastOffer(self):
        return self.offerIndex == 2

    def acceptPart(self):
        self.robot.append(self.currentPart()) # add part to robot
        self.partIndex += 1 # move to the next body part
        self.offerIndex = 0
        if self.partIndex == len(part_types): # if all 4 body parts are chosen, start the battle
            self.startBattling()

    def rejectPart(self):
        if not self.isLastOffer(): # the 3rd offer can't be rejected
            self.offerIndex += 1

    # scoring

    def score(self):
        total = 0
        for part in self.robot:
            total += part.tier
        return total

    def maxScore(self):
        # best tier (5) x no. of parts (4) = 20
        return max(tier_names) * len(part_types)

    def averageTier(self):
        return round(self.score() / len(part_types))

    # battle
    def startBattling(self):
        self.gameState = "battle"
        self.battle = Battle(self.robot) # will create enemies inside battle.py later

    def checkBattleOver(self):
        if self.battle.isOver():
            self.gameState = "menu" # return to menu if battle is over