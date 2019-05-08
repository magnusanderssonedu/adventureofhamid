import pygame
import os
from room import Room

class Board:
    current_tile = 0
    #board = pygame.image.load(os.path.join('data', 'board.png'))
    board = pygame.image.load(os.path.join('data', 'boardcobbled2.png')) #alternative board
    boardcoords = (1,1)
    minmove = (0,0) #top left corner
    maxmove = (5,5) # bottom right corner - (15,10) originally
    rooms = {} # rooms visited on the board
    tiles = [] # list with tuples with this boards all tile_images and corresponding coordinates [(coord, tileimage.png), ...]
    velx = 105 # pixels per coord in room_id
    vely = 105 # pixels per coord in room_id

    def __init__(self, tile = 0, minmove = (0,0), maxmove = (5,5)):
        if (tile >=0 and tile <=5):
            self.current_tile = tile
        else:
            self.current_tile = 0
        self.minmove = minmove
        self.maxmove = maxmove

        self.tiles = []

    def get_current_tile(self):
        return self.current_tile

    def set_current_tile(self, tile):
        self.current_tile = tile

    def draw(self):
        return self.board

    def coords(self):
        return self.boardcoords

    def enter_room(self, room_id, entering_from):
        """
        Is called from game to enter new or old room
        room_id:tuple
        entering_from:String 'n', 'e', 's' or 'w'
        """
        room_index = self.getRoomIndex(room_id)

        if room_index in self.rooms:
            room = self.rooms[room_index]
            room.enterRoom(entering_from)
        else:
            room = Room(room_id)
            room.enterRoom(entering_from)
            self.rooms[room_index] = room
            self.tiles.append(((room_id[0]*self.velx, room_id[1]*self.vely), room.getTileImage()))

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
    
    def getRoomIndex(self, room_id):
        x, y = room_id
        room_index = str(x) + str(y)
        return room_index