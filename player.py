import pygame
import os

class Player:
    #Player variables
    x = 0
    y = 0
    relx = 0
    rely = 0
    width = 34 #width and height of player image on screen
    height = 34
    velx = 35  #width+borderwidth
    vely = 35  #height+borderheight
    me = pygame.image.load(os.path.join('data', 'player.png'))

    def __init__(self,coords=(0,0)):
        self.relx = 0
        self.rely = 0
        self.move(coords)

    def move(self,movecords):
        """Sätter relx, rely (koordinaterna) samt x, y som är pixlarna"""
        self.relx = self.relx + movecords[0]
        self.x = self.velx*self.relx
        self.rely = self.rely + movecords[1]
        self.y = self.vely*self.rely

    def draw(self):
        return self.me

    def coords(self):
        return (self.x,self.y)

    def relcoords(self):
        return (self.relx,self.rely)