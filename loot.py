import pygame
import os

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
        "dagger": "loot_dagger.png"
        "stone": "loot_stone.png"
    }
    coords = (100,100)

    def __init__(self,name,description,sprite,effect,inventoryitem = False,coords=(0,0)):
        self.name = name
        self.description = description
        self.effect = effect
        if len(sprite) > 0:
            self.me = pygame.image.load(os.path.join('data', self.picpicker[sprite]))
        self.coords = coords
        self.inventoryitem = inventoryitem

    def draw(self,surface):
        if self.me != None:
            surface.blit(self.me, (self.coords[0],self.coords[0]))

    def setCoords(self,coords):     #only useful for inventory items
        self.coords = coords

    def playerEffect(self,playerObj=None,mobObj=None):
        if self.inventoryitem:
            playerObj.addInventory(self)
        if self.effect[0] = "hp":
            playerObj.setHP(playerObj.getHP() + self.effect[1])
        elif self.effect[0] = "attack":
            playerObj.setAttack(playerObj.getAttack() + self.effect[1])
        elif self.effect[0] = "less mobs":
            playerObj.setMobChance(self.effect[1])

    def removeItem(self):
        if self.effect[0] = "attack":
            playerObj.setAttack(playerObj.getAttack() - self.effect[1])
        elif self.effect[0] = "less mobs":
            playerObj.setMobChance(1)

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
        "description":"A pot of gold!",
        "sprite":"gold",
        "effect":("",0),
        "inventoryitem": True
    },
    "torch": {
        "name": "Torch",
        "description":"A torch that brings light!",
        "sprite":"torch",
        "effect":("less mobs",0.7),
        "inventoryitem": True
    },
    "healing water": {
        "name": "Healing water",
        "description":"A flask of healing water!",
        "sprite":"",
        "effect":("hp",random.randint(10,40)),
        "inventoryitem": False
    },
    "sword": {
        "name": "Enchanted sword",
        "description":"An enchanted sword!",
        "sprite":"",
        "effect":("attack",random.randint(4,8)),
        "inventoryitem": True
    },
    "jewlery": {
        "name": "Jewlery",
        "description":"A bunch of jewlery!",
        "sprite":"gold",
        "effect":("",0),
        "inventoryitem": True
    },
    "food": {
        "name": "Some food",
        "description":"Some food!",
        "sprite":"",
        "effect":("hp",random.randint(5,15)),
        "inventoryitem": False
    },
    "stone": {
        "name": "A sharp stone",
        "description":"A sharp stone!",
        "sprite":"stone",
        "effect":("attack",1),
        "inventoryitem": True
    },
    "dagger": {
        "name": "A dagger",
        "description":"A dagger!",
        "sprite":"stone",
        "effect":("attack",random.randint(1,3)),
        "inventoryitem": True
    }
}
