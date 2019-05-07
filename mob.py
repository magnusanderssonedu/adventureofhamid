import pygame
import os

class Mob:
    #Mob variables
    hp = 20 #mob health points
    agressive = True #is the mob an attacking or passive Mob
    attack = 2 #damage dealt on attack. For passive mobs, like mines or trap doors, this will happen on trigger
    trigger = 0.2 #percentage that the mob will attack
    description = "a mob" #Description for the status bar
    me = None #image of the mob

    def __init__():
        self.relx = 0
