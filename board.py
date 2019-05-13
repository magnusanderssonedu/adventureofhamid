import pygame
import os
from room import Room
import random
from tilefloors import floors

class Board:
    current_tile = 0
    #board = pygame.image.load(os.path.join('data', 'board.png'))
    board = pygame.image.load(os.path.join('data', 'boardcobbled6.png')) #alternative board
    boardcoords = (1,1)
    minmove = (0,0) #top left corner
    maxmove = (5,5) # bottom right corner - (15,10) originally
    rooms = {} # rooms visited on the board
    tiles = [] # list with tuples with this boards all tile_images and corresponding coordinates [(coord, wallimage.png, floorimage.png), ...]
    velx = 105 # pixels per coord in room_id
    vely = 105 # pixels per coord in room_id
    tile_floors = []

    def __init__(self, tile = 0, minmove = (0,0), maxmove = (5,5)):
        if (tile >=0 and tile <=5):
            self.current_tile = tile
        else:
            self.current_tile = 0
        self.minmove = minmove
        self.maxmove = maxmove
        random.shuffle(floors)
        self.tile_floors = floors
        self.tiles = []

    def get_current_tile(self):
        return self.current_tile

    def set_current_tile(self, tile):
        self.current_tile = tile

    def draw(self, surface):    #draws the board with all the tiles
        surface.blit(self.board, self.boardcoords)
        for t in self.tiles:
            surface.blit(t[2], t[0]) #floor
            surface.blit(t[1], t[0]) #walls

    def coords(self):
        return self.boardcoords

    def enter_room(self, room_id):
        """
        Is called from game to enter new or old room
        room_id:tuple
        """
        room_index = self.getRoomIndex(room_id)
        neigbouring_rooms = self.getNeigbouringRooms(room_id) # list with tuples eg [('n', 1), ('s', 0)]
        if room_index in self.rooms:
            room = self.rooms[room_index]
            room.enterRoom()
        else:

            tile_floor = self.tile_floors.pop()
            room = Room(room_id, neigbouring_rooms, tile_floor)
            room.enterRoom()
            self.rooms[room_index] = room
            self.tiles.append(((room_id[0]*self.velx, room_id[1]*self.vely), room.getRoomWalls(), room.getRoomFloor()))

    def getTiles(self):
        return self.tiles

    def room_exits(self, room_id):
        """
        Is called from game to get this rooms exits and put it in the status window
        room_id:tuple
        """
        room_index = self.getRoomIndex(room_id)
        return self.rooms[room_index].get_exits()

    def is_validmove(self,movecoords, playercoords):
        #movecoords is a tuple like (x,y) pointing out direction, eg (1, 0) moving right, (-1, 0) moving left, (0, 1) moving down, (0, -1) moving up
        #playercoords is tuple like (x,y) of players current tile
        move = False
        room = self.rooms[self.getRoomIndex(playercoords)]
        if not (movecoords[0] == 0 and movecoords[1] == 0): # movecoords(0,0) means no move at all.
            move = True
            #check for moves resulting in player outside screen
            if movecoords[0] < 0 and movecoords[0]+playercoords[0] < self.minmove[0]:    #moving past left border is False move
                move = False
            if movecoords[1] < 0 and movecoords[1]+playercoords[1] < self.minmove[1]:    #moving past top border is False move
                move = False
            if movecoords[0] > 0 and movecoords[0]+playercoords[0] > self.maxmove[0]:    #moving past right border is False move
                move = False
            if movecoords[1] > 0 and movecoords[1]+playercoords[1] > self.maxmove[1]:    #moving past bottom border is False move
                move = False
            if not room.isValidMove(movecoords):
                move = False
        return move

    def getNeigbouringRooms(self, room_id):
        """
        Check if existing neigbours to room with room_id has doors leading to if
        room_id:tuple (int x, int y)
        returns neigbouring_doors:list with tuples eg [('n', 1), ('s', 0)] for north neighbour door and south neighbour no door
        """
        neigbouring_rooms = []
        thisx, thisy = room_id

        outofborder = [] # will be filled with directions that is out of game board one step away from this room
        if thisx + 1 > self.maxmove[0]:
            # the room to the right is out of the game board
            outofborder.append('e')
        if thisx - 1 < self.minmove[0]:
            # the room to the left is out of the game board
            outofborder.append('w')
        if thisy + 1 > self.maxmove[1]:
            # the room downwards is out of the game board
            outofborder.append('s')
        if thisy - 1 < self.minmove[1]:
            # the room upwards is out of the game board
            outofborder.append('n')

        # neigbouring room_indexes: dict = {neigbour direction = (room index, direction to check from that room), ...}
        neigbouring_rooms_indexes = {
            'n': (self.getRoomIndex((thisx, thisy-1)), 's'),
            'e': (self.getRoomIndex((thisx + 1, thisy)), 'w'),
            's': (self.getRoomIndex((thisx,thisy + 1)),'n'),
            'w': (self.getRoomIndex((thisx - 1, thisy)), 'e')
            }

        for key, value in neigbouring_rooms_indexes.items():
            index = value[0]
            exit = value[1]

            # if out of border set that direction to 0 otherwise check if room already placed on the board
            if key in outofborder:
                # direction is out of border
                neigbouring_rooms.append((key, 0))
            else:
                # direction is not out of border
                if index in self.rooms:
                    # the room exists
                    if self.rooms[index].tile_holder[0].exits[exit] == 1:
                        neigbouring_rooms.append((key, 1))
                    else:
                        neigbouring_rooms.append((key, 0))

        return neigbouring_rooms





    def getRoomIndex(self, room_id):
        x, y = room_id
        room_index = str(x) + str(y)
        return room_index
