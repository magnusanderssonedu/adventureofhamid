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
    rooms = {}

    def __init__(self, tile = 0, minmove = (0,0), maxmove = (5,5)):
        if (tile >=0 and tile <=5):
            self.current_tile = tile
        else:
            self.current_tile = 0
        self.minmove = minmove
        self.maxmove = maxmove

    def get_current_tile(self):
        return self.current_tile

    def set_current_tile(self, tile):
        self.current_tile = tile

    def draw(self):
        return self.board

    def coords(self):
        return self.boardcoords

    def enter_room(self, room_id, entering_from):
        x, y = room_id
        room_index = str(x) + str(y)

        if room_index in self.rooms:
            room = self.rooms[room_index]
            print("set_room:", room)
            print("old tile is:", room.getTile())
        else:
            room = Room(room_id, entering_from)
            self.rooms[room_index] = room
            print("set_room:", room)
        print("self.rooms:", self.rooms)

    def get_room_info(self, room_id):
        pass
    def is_validmove(self,movecoords, playercoords):
        #movecoords is a tuple like (x,y) pointing out direction, eg (1, 0) moving right, (-1, 0) moving left
        #playercoords is tuple like (x,y) of players current tile
        move = False
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
        return move