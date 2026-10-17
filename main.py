import pygame
import random

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
                self.running = false
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
            while self.running:
                screen.blit(legs_img, (30,30))
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
                case "menu":
                    self.menuLoop()
                case "building":
                    pass
                    #call building function
                case "battle":
                    pass
                    #other attack

    def beginGame(self):
        self.running = True
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
background_img = pygame.image.load('assets/apple.png').convert() # the apple is 740 x 740  btw


clock = pygame.time.Clock()
# fill the screen with a color to wipe away anything from last frame
screen.fill("purple")


theGame = Game()
theGame.beginGame()
pygame.quit()