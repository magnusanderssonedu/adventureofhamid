import random
import pygame
import os
class Tile:
    tile_id = (-1,-1)
    x = 0
    y = 0
    exits = {
        'n': 0,
        'e': 0,
        's': 0,
        'w': 0
    }
    tile_image = "walls_"
    def __init__(self, tile_id, entering_from):
        """tile id is same as room coord: tuple. entering_from is string 'n', 'e', 's' or 'w'"""

        # Checking valid entering_from value
        assert entering_from == "n" or entering_from == 'e' or entering_from == 's' or entering_from == 'w'

        self.tile_image = "walls_"
        self.x = 0
        self.y = 0
        self.tile_id = tile_id
        self.exits = {
            'n': 0,
            'e': 0,
            's': 0,
            'w': 0
        }
        self.generateExits(entering_from)
        self.generateTileImage()


    def generateExits(self, entering_from):
        """
        Generate values for every exit. 0 for no exit and 1 for exit
        entering_from: String 'n', 'e', 's' or 'w'.
        Special case for first tile
        """
        if self.tile_id == (0,0):
            self.exits = {
                'n': 0,
                'e': 1,
                's': 1,
                'w': 0
            }
        else:
            for key in self.exits.keys():
                exitvalue = random.randint(0, 1)
                if key != entering_from:
                    self.exits[key] = exitvalue
                else:
                    self.exits[entering_from] = 1
        # for key, value in self.exits.items():
        #     print(key, value)

    def generateTileImage(self):
        for key, value in self.exits.items():
            if value == 1:
                self.tile_image += key
        self.tile_image += ".png"
        # print(self.tile_image)
    
    def getTileImage(self):
        return pygame.image.load(os.path.join('data', self.tile_image))

    def generateTile(self):
        pass
    def getTileExits(self, id):
        pass