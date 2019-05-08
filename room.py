from tile import Tile
class Room:
    tile_holder = []
    room_id = (-1,-1)
    def __init__(self, room_id):
        self.room_id = room_id
        self.tile_holder = []

    def enterRoom(self, entering_from):
        if not self.hasTile():
            self.putTile(self.room_id, entering_from)

    def putTile(self, room_id, entering_from):
        """tile id is same as roomcoordinate"""
        new_tile = Tile(room_id, entering_from)
        self.tile_holder.append(new_tile)

    def hasTile(self):
        return len(self.tile_holder) > 0

    def getTile(self):
        return self.tile_holder[0]

    def getMob(self):
        pass
    
    def getTileImage(self):
        return self.tile_holder[0].getTileImage()

    def get_exits(self):
        """
        Is called from game to get this rooms exits.
        """
        exits = ''
        for key, value in self.tile_holder[0].exits.items():
            if value == 1:
                exits += key + ' '
        return exits

    def isValidMove(self, movecoords):
        """
        checks and returns True or False if moving from this room to movecoords is a valid move
        movecoords:tuple where (1, 0) moving right, (-1, 0) moving left, (0, 1) moving down, (0, -1) moving up
        """
        valid_move = False
        exits = self.tile_holder[0].exits # dictionary with this tiles exits
        if movecoords == (1, 0) and exits['e'] == 1:
            valid_move = True
        elif movecoords == (-1, 0) and exits['w'] == 1:
            valid_move = True
        elif movecoords == (0, 1) and exits['s'] == 1:
            valid_move = True
        elif movecoords == (0, -1) and exits['n'] == 1:
            valid_move = True
        
        return valid_move