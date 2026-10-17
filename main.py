#put code here?
class Game:
    def __init__(self):
        self.gameState = "menu"
        #begin GUI
    
    def leftKeyPress(self):
        match self.gameState:
            case "menu":
                self.startBuilding()
            case "building":
                pass
                #accept piece, send to robot
            case "battle":
                pass
                #attack

    def rightKeyPress(self):
        match self.gameState:
            case "menu":
                pass
                #quit game
            case "building":
                pass
                #refuse piece, get next
            case "battle":
                pass
                #other attack

    def startBuilding(self):
        self.gameState = "building"
        self.parts = [[]*3]*4
        for i in range(0,4):
            for j in range(0,3):
                self.parts[i][j] = 0 #call create part 
        #create lists of random parts

    def menuLoop(self):
        pass

    def buildLoop(self):
        pass

    def battleLoop(self):
        pass

    def mainLoop(self):
        pass
        #gui stuff here
        match self.gameState:
            case "menu":
                self.menuLoop()
            case "building":
                pass
                #call building function
            case "battle":
                pass
                #other attack


theGame = Game()
theGame.mainLoop()