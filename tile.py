import random

class Tile:
    tile_id = -1
    exits = {
        'n': 0,
        'e': 0,
        's': 0,
        'w': 0
    }
    def __init__(self, tile_id, entering_from):
        """tile id is same as room coordiante. entering from is string 'n', 'e', 's' or 'w'"""

        # Checking valid entering_from value
        assert entering_from == "n" or entering_from == 'e' or entering_from == 's' or entering_from == 'w'

        self.tile_id = tile_id
        self.generateExits(entering_from)

    def generateExits(self, entering_from):
        """generate values for every exit. 0 for no exit and 1 for exit"""
        for key in self.exits.keys():
            exitvalue = random.randint(0, 1)
            exits[key] = exitvalue

    def generateTile(self):
        pass
    def getTileExits(self, id):
        pass