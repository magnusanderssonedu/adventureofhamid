import random
chestloot = ["gold", "torch", "healing water", "sword","jewlery", "food", "stone"]
monsterloot = ["jewlery", "food", "stone", "dagger"]
mobdict = {
    0: {
        "category": "nothing",
        "name": "Empty room",
        "description": "nothing",
        "hp": -1,
        "killable": False,
        "aggressive": False,
        "damage": 0,
        "attacktrigger": 0,
        "fleetrigger": 0,
        "sprite": "",
        "loot": ""
    },
    1: {
        "category": "monster",
        "name": "Zombie",
        "description": """Welcome to the death room,
        the Zombie is here. He has
        been here for a long time,
        nobody knows how long
        because nobody has never
        come out of this room alive.
        You will soon enough smell the
        flesh of the zombie. Do not be
        afraid, trust in yourself""",
        "hp": random.randint(4,10),
        "killable": True,
        "aggressive": True,
        "damage": random.randint(1,5),
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": random.randint(1,5)/10,
        "sprite": "zombie",
        "loot": random.choice(monsterloot)
    },
    2: {
        "category": "monster",
        "name": "Skeleton",
        "description": """You can hear the sound of
        bone hitting the ground. It is
        coming for you. The skeleton
        looks very fresh and bony, you
        could see places in his body
        where flesh has recently been
        removed. There is a hole around
        the skull with a sharp knife in it.
        - Are you brave enough
        to fight it?""",
        "hp": random.randint(2,5),
        "killable": True,
        "aggressive": True,
        'damage': random.randint(1,5),
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": random.randint(1,8)/10,
        "sprite": "skeleton",
        "loot": random.choice(monsterloot)
    },
    3: {
        "category": "treasure",
        "name": "A Chest",
        "description": """You find a chest full of
        ...what?

        Press action to open.""",
        "hp": 0,
        "killable": True,
        "aggressive": False,
        "damage": 0,
        "attacktrigger": 0,
        "fleetrigger": 0,
        "sprite": "chest",
        "loot": random.choice(chestloot)
    },
    4: {
        "category": "trap",
        "name": "Arrows from wall",
        "description": """When you step into the room
        arrows shoots out from small
        holes in the wall!""",
        "hp": 0,
        "killable": True,
        "aggressive": True,
        "damage": random.randint(1,10),
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": 0,
        "sprite": "chest",
        "loot": ""
    }

}
