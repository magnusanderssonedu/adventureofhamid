import pygame
import os

"""This class is a quite generalized class for any type of obstacle, both active and inactiveself.
Eg. a landmine aswell as a zombie is regarded as a mob in this context.
"""

class Mob:
    #Mob variables
    hp = 20 #mob health points
    killable = True #if killable is False the mob will resurrect on every new encounter. Useful on traps that can be triggered multiple times.
    agressive = True #is the mob an attacking or passive Mob. Passive mob being a trap door or mine.
    attack = 2 #damage dealt on attack. For passive mobs, like mines or trap doors, this will happen on trigger
    attacktrigger = 0.3 #percentage that the mob will return the attack.
    fleetrigger = 0.2 #percentage that the mob will attack on flight. Usually a value lower than attack trigger unless the mob is passive
    description = "a mob" #Description for the status bar
    me = None #image of the mob. Use keywords from picpicker to choose sprite

    picpicker = {
        "mine": "mob_mine.png",
        "trap": "mob_trap.png",
        "zombie": "mob_zombie.png"
    }

    def __init__(self,hp=0,killable = True,description="Mine",aggressive=False,attack=10,attacktrigger=0.3,fleetrigger=0.2,sprite="mine"):
        self.hp = hp
        self.killable = killable
        self.aggressive = aggressive
        self.attacktrigger = attacktrigger
        self.fleetrigger = fleetrigger
        self.trigger = trigger
        self.description = description
        self.me = pygame.image.load(os.path.join('data', self.picpicker[sprite]));

    def attack(self,dievalue,flee=False):
        """
        The value dievalue is a percentage and is obligatory
        The value flee is a boolean representing whether the player is fleeing or not.
        Returns a tuple with (hit,damage) where hit is either True or False and damage is the damage dealt by the mob on hit
        """
        retValue = (False,0)
        if(flee):
            triggering = self.fleetrigger
        else:
            triggering = self.attacktrigger

        if(triggering > dievalue):
            retValue = (True,self.attack)
        return retValue

    def hit(self,hit):
        """
        Mob is hit with 100% chance. Damage dealt is managed by player class.
        This method sets hp after hit. Use getHPvalue() to get HP.
        """
        self.hp -= hit
        if self.hp < 0:
            self.hp = 0

    def draw(self): #return image of mob for drawing
        return self.me

    def getDescription(self):   #return description for drawing on status
        return self.description

    def getHPvalue(self):  #return hp for drawing on status
        return self.hp
