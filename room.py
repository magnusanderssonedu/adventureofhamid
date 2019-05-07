from tile import Tile
class Room:
    tile = {}
    def __init__(self, room_id, entering_from):
        self.room_id = room_id
        self.enterRoom(entering_from)

    def enterRoom(self, entering_from):
        if self.hasTile():
            tile = self.getTile()
        else:
            self.putTile(self.room_id, entering_from)

    def putTile(self, room_id, entering_from):
        """tile id is same as roomcoordinate"""
        self.tile = Tile(room_id, entering_from)
        print("self.tile", self.tile)

    def hasTile(self):
        return len(self.tile) > 0

    def getTile(self):
        return self.tile

    def getMob(self):
        pass