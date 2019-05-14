from tile import Tile
from mobdict import mobdict
import random

class Room:
    tile_holder = []
    room_id = (-1,-1)
    neigbouring_rooms = []
    tile_floor = ""
    hasmob = True
    def __init__(self, room_id, neigbouring_rooms, tile_floor, hasmob=True):
        self.room_id = room_id
        self.tile_holder = []
        self.tile_floor = tile_floor
        self.neigbouring_rooms = neigbouring_rooms
        self.hasmob = hasmob
        print("hasmob:", hasmob)
        mob = self.getMob()
        print(mob)

    def enterRoom(self):
        if not self.hasTile():
            self.putTile()

    def putTile(self):
        """tile id is same as roomcoordinate"""
        # print(self.neigbouring_rooms)
        new_tile = Tile(self.room_id, self.neigbouring_rooms, self.tile_floor)
        self.tile_holder.append(new_tile)

    def hasTile(self):
        return len(self.tile_holder) > 0

    def getTile(self):
        return self.tile_holder[0]

    def getMob(self):
        if self.hasmob:
            mobkey = random.choice(list(mobdict.keys()))
        else:
            mobkey = 0
        return mobdict[mobkey]
    
    def getRoomWalls(self):
        return self.tile_holder[0].getTileWalls()

    def getRoomFloor(self):
        return self.tile_holder[0].getTileFloor()

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
    
