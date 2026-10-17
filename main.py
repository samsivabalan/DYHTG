import pygame
import random
#import parts

class Game:
    

    def __init__(self):
        self.gameState = "menu"
        self.keyDown = False
    
    def leftKeyPress(self):
        match self.gameState:
            case "menu":
                #begin building phase
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
                #quit game
                self.running = False
            case "building":
                pass
                #refuse piece, get next
            case "battle":
                pass
                #other attack
    
    def acceptPart(self):
        #add part to robot
        #playerBot.assemble(self.partType, self.currentPart)
        #move along to next item
        if self.partIndex == 2:
            if self.partType == 3:
                #end build phase
                pass
            else:
                self.partType += 1
                self.partIndex = 0

    def rejectPart(self):
        #burn the part

        #move along to next item
        if self.partIndex == 2:
            #add part to robot
            #playerBot.assemble(self.partType, self.currentPart)
            if self.partType == 3:
                #end build phase
                pass
            else:
                self.partType += 1
                self.partIndex = 0
        

    def startMenu(self):
        #menu UI will be drawn here
        pass

    def startBuilding(self):
        #update game state
        self.gameState = "building"

        #create lists of random parts
        self.parts = [[0]*3]*4
        for i in range(0,4):
            remainingTiers = [0, 1, 2, 3, 4, 5]
            for j in range(0,3):
                tier = random.choice(remainingTiers)
                remainingTiers.remove(tier)
                self.parts[i][j] = 0 #Part(i, tier)
        self.partType = 0
        self.partIndex = 0
        

    def startBattling(self):
        self.gameState = "battle"
        #create enemies

    def buildLoop(self):
        self.currentPart = self.parts[self.partType][self.partIndex]
        screen.blit(self.currentPart.img, (960,80))
        

    def battleLoop(self):
        pass

    def mainLoop(self):
            while self.running:
                #screen.fill("green")
            
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
                for event in pygame.event.get():
                        match event.type:
                            case pygame.QUIT:
                                running = False
                            case pygame.KEYDOWN:
                                if self.keyDown == False:
                                    if event.key == pygame.K_a:
                                        self.leftKeyPress()
                                    elif event.key == pygame.K_d:
                                        self.rightKeyPress()
                                    self.keyDown = True
                            case pygame.KEYUP:
                                self.keyDown = False
                # flip() the display to put your work on screen
                pygame.display.flip()
                clock.tick(60)  # limits FPS to 60
        
            match self.gameState:
                case "building":
                    self.buildLoop()
                case "battle":
                    self.battleLoop()

    def beginGame(self):
        #draw background
        screen.blit(background_img, (0,0))

        #set loop condition
        self.running = True

        #draw menu
        self.startMenu()

        #begin the main loop
        self.mainLoop()





#pygame setup stuff
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.toggle_fullscreen

#Assets
#We will want multiple of each kind ofc
legs_img = pygame.image.load('assets/appleLegs.png').convert() 
body_img = pygame.image.load('assets/appleBody.png').convert()
arms_img = pygame.image.load('assets/appleArms.png').convert()
head_img = pygame.image.load('assets/appleHead.png').convert()
background_img = pygame.image.load('assets/background_draft.png').convert()


clock = pygame.time.Clock()
# fill the screen with a color to wipe away anything from last frame
screen.fill("#404040")


playerBot = 0 #Robot(empty)
theGame = Game()
theGame.beginGame()
pygame.quit()