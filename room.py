from tile import Tile
class Room:
    tile = None
    def putTile(self, id):
        """tile id is same as roomcoordinate"""
        self.tile = Tile(id)

    def getTile(self):
        pass
    def getMob(self):
        pass
    