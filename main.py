# The rules of the game
# main.py calls leftKeyPress() / rightKeyPress() when a key is pressed,
# and reads te variables below to decide what to draw
# It sets up an empty robot and startBuilding() empties it again at the start of every new game
# main.py - the file you run. Everything visual is in here
# This is the only file that uses pygame. The rules of the game are in game.py

import pygame
import random
from robot import Robot
from robot import Part
from battle import Battle

class Game:
    def __init__(self):
        self.gameState = "menu"
        self.keyDown = False
        self.playerBot = Robot("player") # creates a robot with no parts
        self.parts = [] # 4 lists, one per body part, 3 offers in each
        self.partIndex = 0 # body part: 0 legs, 1 torso, 2 arms, 3 head
        self.offerIndex = 0 # offer on screen: 0, 1 or 2
        self.battle = None # no battle until the robot is finished

    def load_assets(self):
        heads,bodies,arms,legs,light_on,light_off = []
        types = ["pile","scrap","service","toy","companion","eco"]

        for t in types:
            legs.append(pygame.image.load('assets/' + t + '_legs.png').convert())
            bodies.append(pygame.image.load('assets/'+ t + '_body.png').convert())
            arms.append(pygame.image.load('assets/' + t + '_arms.png').convert())
            heads.append(pygame.image.load('assets/' + t +'_head.png').convert())

        frame = pygame.image.load('assets/frame.png').convert()
        background_img = pygame.image.load('assets/background_img.png').convert()
        shelf = pygame.image.load('assets/shelf.png').convert()
        fire = pygame.image.load('assets/fire.png').convert()
        button_1 = pygame.image.load('/assets/button_1.png').convert()
        button_2 = pygame.image.load('/assets/button_2.png').convert()

        for i in range (0,3):
            light_on.append(pygame.image.load('assets/light' + i + '_on.png').convert())
            light_on.append(pygame.image.load('assets/light' + i + '_on.png').convert())

        return heads,bodies,arms,legs,light_on,light_off,frame,background_img,shelf,fire,button_1,button_2

    def leftKeyPress(self):
        match self.gameState:
            case "menu":
                self.startBuilding() # begin building process
            case "building":
                self.acceptPart() # accept piece, send to robot
            case "battle":
                self.battle.leftAction() # attack

    def rightKeyPress(self):
        match self.gameState:
            case "menu":
                self.running = False # quit game
            case "building":
                self.rejectPart() # refuse piece, get next
            case "battle":
                self.battle.rightAction() # other attack

    def createOffers(self, partType):
        # Make 3 parts of one type, each one being a different, random tier
        tiers = random.sample([0, 1, 2, 3, 4, 5], 3)

        # Turns each tier number into a part e.g. [5, 2, 4] -> Eco bot, Toy bot, Companion bot
        offers = []
        for tier in tiers:
            offers.append(Part(partType,tier))
        return offers
    
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
        self.parts = []
        for i in range(0,4):
            self.parts.append(self.createOffers(i))
        self.partType = 0
        self.partIndex = 0
        

    def startBattling(self):
        self.gameState = "battle"
        #create enemies

    def buildLoop(self):
        self.currentPart = self.parts[self.partType][self.partIndex]
        screen.blit(self.currentPart.img, (960,80))
        #for part in self.playerBot
        

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
        
        heads_img,bodies_img,arms_img,legs_img,light_on_img,light_off_img,frame_img,background_img,shelf_img,fire_img,button_1_img,button_0_img = theGame.load_assets()
        
        #draw background
        screen.blit(background_img, (0,0))
        screen.blit(frame_img, (0,0))
        screen.blit(shelf_img,(960,0))
        for i in range(0,3):
            screen.blit(light_on[i], 980,600)
            screen.blit(light_off[i], 980,600)
        screen.blit(button_1_img, 970,620)
        screen.blit(button_2_img, 990,620)

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

clock = pygame.time.Clock()
# fill the screen with a color to wipe away anything from last frame
screen.fill("#404040")


playerBot = 0 #Robot(empty)
theGame = Game()
theGame.beginGame()
pygame.quit()
