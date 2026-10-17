# Currently a placeholder so the game can go from building to battle and then back to the menu
# Battle rules will go in here once the team decided how the battles will work

class Battle:
    def __init__(self, robot):
        self.robot = robot # List of the 4 body parts the player chose
        self.over = False
        self.message = "Battle starting soon! Press left or right"

    def leftAction(self):
        self.over = True

    def rightAction(self):
        self.over = True

    def isOver(self):
        return self.over

    # Currently, any battle key ends the battle straight away
    # When the battle rules are finalised, these will be added to the key press functions
    # self.over = True only when someone wins