import pygame
import os
import random

"""A class handeling loot of different kind
"""

class Loot:
    name = ""
    description = ""
    me = None
    effect = ("player_hp",1)    #choose the effect from available effects in playerEffect method
    inventoryitem = False
    picpicker = {
        "gold": "loot_gold.png",
        "torch": "loot_torch.png",
        "sword": "loot_sword.png",
        "dagger": "loot_dagger.png",
        "stone": "loot_stone.png",
        "jewlery": "loot_jewlery.png"
    }
    coords = (100,100)

    def __init__(self,name,description,sprite,effect,inventoryitem = False,coords=(0,0)):
        self.name = name
        self.description = description
        self.effect = effect
        if len(sprite) > 0:
            if sprite in self.picpicker:
                self.me = pygame.image.load(os.path.join('data', self.picpicker[sprite]))
        self.coords = coords
        self.inventoryitem = inventoryitem

    def draw(self,surface):
        if self.me != None:
            surface.blit(self.me, (self.coords[0],self.coords[1]))

    def setCoords(self,coords):     #only useful for inventory items
        self.coords = coords

    def setRelCoords(self,index):   #get coordinates based on item index
        relCoords = [(650,90),
        (740,90),
        (650,165),
        (740,165),
        (650,240),
        (740,240)]
        self.setCoords(relCoords[index])

    def getDescription(self):
        return self.description

    def getEffect(self):
        return self.effect

lootdict = {
    "": {
        "name": "nothing",
        "description":"",
        "sprite":"",
        "effect":("",0),
        "inventoryitem": False
    },
    "gold": {
        "name": "Gold",
        "description":"a pot of gold!",
        "sprite":"gold",
        "effect":("",0),
        "inventoryitem": True
    },
    "torch": {
        "name": "Torch",
        "description":"a flaming torch!",
        "sprite":"torch",
        "effect":("less mobs",random.randint(30,70)*0.01),
        "inventoryitem": True
    },
    "healing water": {
        "name": "Healing water",
        "description":"a flask of healing water!",
        "sprite":"",
        "effect":("hp",random.randint(10,40)),
        "inventoryitem": False
    },
    "sword": {
        "name": "Enchanted sword",
        "description":"an enchanted sword!",
        "sprite":"sword",
        "effect":("attack",random.randint(4,8)),
        "inventoryitem": True
    },
    "jewlery": {
        "name": "Jewlery",
        "description":"some jewlery!",
        "sprite":"jewlery",
        "effect":("",0),
        "inventoryitem": True
    },
    "food": {
        "name": "some food",
        "description":"some food!",
        "sprite":"",
        "effect":("hp",random.randint(5,15)),
        "inventoryitem": False
    },
    "stone": {
        "name": "A sharp stone",
        "description":"a sharp stone!",
        "sprite":"stone",
        "effect":("attack",1),
        "inventoryitem": True
    },
    "dagger": {
        "name": "A dagger",
        "description":"a dagger!",
        "sprite":"dagger",
        "effect":("attack",random.randint(1,3)),
        "inventoryitem": True
    }
}
