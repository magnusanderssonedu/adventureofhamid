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

    def __init__(self,coords=(0,0)):
        self.relx = 0
        self.rely = 0
        self.move(coords)
        self.attack = 1
        self.inventory = []
        self.mobChance = 1

    def move(self,movecords):
        """Sätter relx, rely (koordinaterna) samt x, y som är antalet pixlar"""
        self.relx = self.relx + movecords[0]
        self.x = self.relx * self.velx + 35
        self.rely = self.rely + movecords[1]
        self.y = self.rely * self.vely + 35

    def draw(self,surface):
        surface.blit(self.me, (self.x,self.y))
        for item in self.inventory:
            item.draw(surface)

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
        #Returns the attack strength for player. If item in inventory effecting attack, add the highest value to the attack stat.
        effect = 0
        for item in self.inventory:
            if item.effect[0] == "attack" and item.effect[1] > effect:
                effect = item.effect[1]
        return self.attack + effect

    def addInventory(self, LootObj):
        #add loot to inventory. If inventory is full pop the oldest item to get room for the newest.
        if LootObj.inventoryitem:
            if len(self.inventory) == self.MAXLOOT:
                self.inventory.pop(0)
                n = 0
                for item in self.inventory:   #shift places of every inventory item in statusbar
                    item.setRelCoords(n)
                    n += 1
            self.inventory.append(LootObj)
            self.inventory[len(self.inventory)-1].setRelCoords(len(self.inventory)-1)   #set coordinates in statusbar
        else:
            effect, value = LootObj.getEffect()
            if effect == "hp":
                self.setHP(self.hp + value)

    def getMobChance(self):
        #Returns the mobChance for player. If item in inventory effecting mobChance, choose the lowest mobChance
        effect = 1.0
        for item in self.inventory:
            if item.effect[0] == "less mobs" and item.effect[1] < effect:
                effect = item.effect[1]
        return effect
    
    def getTreasure(self):
        gold = 0
        if len(self.inventory) > 0:
            for item in self.inventory:
                if item.effect[0] == 'treasure':
                    gold = gold + item.effect[1]
        
        return gold

    def reset(self):
        self.relx = 0
        self.rely = 0
        self.move((0,0))
        self.hp = 100.0
        self.attack = 1
        self.inventory = []
        self.mobChance = 1
