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
    neigbouring_rooms = []
    def __init__(self, tile_id, neigbouring_rooms):
        """
        tile_id: tuple is same as room coord
        """

        # Checking valid entering_from value
        # assert entering_from == "n" or entering_from == 'e' or entering_from == 's' or entering_from == 'w'

        self.neigbouring_rooms = neigbouring_rooms
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
        self.generateExits()
        self.generateTileImage()


    def generateExits(self):
        """
        Generate values for every exit. 0 for no exit and 1 for exit
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
            # unzip [('n', 1), ('s', 1)] to neigbour_direction = ('n', 's') and neigbour_value = (1, 0)
            unzipped = list(zip(*self.neigbouring_rooms))
            neigbour_direction = unzipped[0]
            neigbour_value = unzipped[1]
            for i, key in enumerate(self.exits.keys()):
                # if negibour exists set exit to 0 or 1 depending on if that neigbour has door to this room or not
                if key in neigbour_direction:
                    self.exits[key] = neigbour_value[neigbour_direction.index(key)]
                else:
                    res = random.randint(0,100)
                    if key == 'w' or key == 's':
                        if res < 75:
                            self.exits[key] = 1
                        else:
                            self.exits[key] = 0
                    else:
                        if res < 50:
                            self.exits[key] = 1
                        else:
                            self.exits[key] = 0



        
        

    def generateTileImage(self):
        for key, value in self.exits.items():
            if value == 1:
                self.tile_image += key
        self.tile_image += ".png"
        # print(self.tile_image)
    
    def getTileImage(self):
        return pygame.image.load(os.path.join('data', self.tile_image))

    def getTileFloor(self):
        return pygame.image.load(os.path.join('data', 'tile_stone_1.png'))

    def generateTile(self):
        pass
    def getTileExits(self, id):
        pass