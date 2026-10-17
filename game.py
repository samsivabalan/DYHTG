# The rules of the game, and the game's main file. 
# It sets up an empty robot and startBuilding() empties it again at the start of every new game

from parts import part_types, createOffers
from battle import Battle

class Game:
    def __init__(self):
        self.gameState = "menu" # Either "menu", "building" or "battle"
        self.running = True # Window closes when False