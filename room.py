from tile import Tile
from mob import Mob
from mobdict import mobdict
import random

class Room:
    tile_holder = []
    room_id = (-1,-1)
    neigbouring_rooms = []
    tile_floor = ""
    hasmob = True
    mob = {}
    room_mob = None
    def __init__(self, room_id, neigbouring_rooms, tile_floor, hasmob=True):
        self.room_id = room_id
        self.tile_holder = []
        self.tile_floor = tile_floor
        self.neigbouring_rooms = neigbouring_rooms
        self.hasmob = hasmob
        self.mob = {}
        self.room_mob = None

    def enterRoom(self):
        """This is called from the board when a player enters the room"""
        # put tile if there isn't one
        if not self.hasTile():
            self.putTile()
        # get this rooms mob depending on certain circumstances
        self.mob = self.getMob()

    def putTile(self):
        """tile id is same as roomcoordinate"""
        # print(self.neigbouring_rooms)
        new_tile = Tile(self.room_id, self.neigbouring_rooms, self.tile_floor)
        self.tile_holder.append(new_tile)

    def hasTile(self):
        return len(self.tile_holder) > 0

    def getTile(self):
        return self.tile_holder[0]

    def setNoMob(self):
        self.hasmob = False

    def getMob(self):
        """Get this rooms mob"""


        # if this room is supposed to have a mob but doesn't yet, find one randomly
        if self.hasmob and not self.mob:
            mobkey = random.choice(list(mobdict.keys()))
            mob = mobdict[mobkey]
            self.room_mob = Mob(mob['hp'],mob['killable'],mob['description'],mob['aggressive'],mob['damage'],mob['attacktrigger'], mob['fleetrigger'], mob['loot'], mob['name'], mob['category'])
        # else if this room is supposed to have a mob and already has one, get that one
        elif self.hasmob and self.mob:
            mob = self.mob
        # else if this room isn't supposed to have a mob get the nothing mob
        else:
            # get the nothing-mob
            mob = mobdict[0]
            self.room_mob = Mob(mob['hp'],mob['killable'],mob['description'],mob['aggressive'],mob['damage'],mob['attacktrigger'], mob['fleetrigger'], mob['loot'], mob['name'], mob['category'])
        print("room->getMob->self.room_mob", self.room_mob)
        return self.room_mob
    
    def getRoomWalls(self):
        """Get this rooms walls"""
        return self.tile_holder[0].getTileWalls()

    def getRoomFloor(self):
        """Get this rooms floor"""
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
    
