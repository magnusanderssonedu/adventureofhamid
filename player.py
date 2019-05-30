import pygame
import os

class Player:
    #Player constants
    MAXHP = 100.0
    MAXLOOT = 6

    #Player variables
    x = 0
    y = 0
    relx = 0
    rely = 0
    width = 34 #width and height of player image on screen (was originally 34)
    height = 34 # (was originally 34)
    velx = 105  #width+borderwidth (was originally 35)
    vely = 105  #height+borderheight (was originally 35)
    hp = 100.0
    me = pygame.image.load(os.path.join('data', 'player.png'))
    attack = 2
    inventory = []
    mobChance = 1

    def __init__(self,coords=(0,0)):
        self.relx = 0
        self.rely = 0
        self.move(coords)

    def move(self,movecords):
        """Sätter relx, rely (koordinaterna) samt x, y som är antalet pixlar"""
        self.relx = self.relx + movecords[0]
        self.x = self.relx * self.velx + 35
        self.rely = self.rely + movecords[1]
        self.y = self.rely * self.vely + 35

    def draw(self,surface):
        surface.blit(self.me, (self.x,self.y))

    def setHP(self, newhp):
        self.hp = newhp
        if self.hp < 0:
            self.hp = 0
        if self.hp > self.MAXHP:
            self.hp = self.MAXHP

    def getHP(self):
        return self.hp

    def coords(self):
        return (self.x,self.y)

    def relcoords(self):
        return (self.relx,self.rely)

    def getAttack(self):
        return self.attack

    def setAttack(self,attack):
        self.attack = attack

    def addInventory(self, LootObj):
        if len(self.inventory) == self.MAXLOOT:
            self.inventory[0].removeItem()
            self.inventory.pop(0)
        self.inventory.append(LootObj)

    def setMobChance(self,mobChance):
        self.mobChance = mobChance

    def getMobChance(self):
        return self.mobChance
