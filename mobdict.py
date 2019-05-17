import random
chestloot = ["gold", "torch", "healing water", "rope"]
monsterloot = ["gold", "jewlery", "food", "stone", "rope", "dagger"]
mobdict = {
    0: {
        "category": "nothing",
        "name": "Empty room",
        "description": "nothing",
        "hp": -1,
        "killable": False,
        "aggressive": False,
        "attack": 0,
        "attacktrigger": 0,
        "fleetrigger": 0,
        "sprite": "",
        "loot": []
    },
    1: {
        "category": "monster",
        "name": "Zombie",
        "description": "Welcome to the death room, the Zombie is here. He has been here for a long time, nobody knows how long because nobody has never came out of this room alive. You will soon enough smell the flesh of the zombie.do not be afraid,trust in yourself",
        "hp": random.randint(4,10),
        "killable": True,
        "aggressive": True,
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": random.randint(1,5)/10,
        "sprite": "zombie",
        "loot": list(set([random.choice(monsterloot) for item in range(0,random.randint(0,3))]))
    },
    2: {
        "category": "monster",
        "name": "Skeleton",
        "description": "you can hear the sound of bone hitting the ground, he is coming for you The skeleton looks very fresh and bony, you could see places in his body where flesh has recently been removed, there is a hole around the skull with a sharp knife in it, are you brave enough to fight him?",
        "hp": random.randint(2,5),
        "killable": True,
        "aggressive": True,
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": random.randint(1,8)/10,
        "sprite": "skeleton",
        "loot": list(set([random.choice(monsterloot) for item in range(0,random.randint(0,3))]))
    },
    3: {
        "category": "treasure",
        "name": "A Chest",
        "description": "You find a chest full of...what?",
        "hp": 0,
        "killable": True,
        "aggressive": False,
        "attacktrigger": 0,
        "fleetrigger": 0,
        "sprite": "chest",
        "loot": list(set([random.choice(chestloot) for item in range(0,random.randint(0,3))]))
    },
    4: {
        "category": "trap",
        "name": "Arrows from wall",
        "description": "When you step into the room arrows shots out from small holes in the wall",
        "hp": 0,
        "killable": True,
        "aggressive": True,
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": 0,
        "sprite": "chest",
        "loot": []
    }
    
}