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
        "description": "A very smelly zombie",
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
        "description": "A very bony skeleton",
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