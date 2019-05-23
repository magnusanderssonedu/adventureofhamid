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
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": random.randint(1,5)/10,
        "sprite": "zombie",
        "loot": list(set([random.choice(monsterloot) for item in range(0,random.randint(0,3))]))
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
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": random.randint(1,8)/10,
        "sprite": "skeleton",
        "loot": list(set([random.choice(monsterloot) for item in range(0,random.randint(0,3))]))
    },
    3: {
        "category": "treasure",
        "name": "A Chest",
        "description": """You find a chest full of
        ...what?""",
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
        "description": """When you step into the room
        arrows shoots out from small
        holes in the wall!""",
        "hp": 0,
        "killable": True,
        "aggressive": True,
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": 0,
        "sprite": "chest",
        "loot": []
    },
    5: {
        "category": "monster",
        "name": "Jones the pirate",
        "description": "I am sure that you have heard about the jones the pirate,he has the soul of devil in himself, he has became the spirit of sea by collecting the souls of people who died at sea  !""",
        "hp": random.randint(2,8),
        "killable": True,
        "aggressive": True,
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": 0,
        "sprite": "chest",
        "loot": []
    },
    6:  {
        "category": "monster",
        "name": "A vampire wolf",
        "description": "this creature has been reprted from north to south, He will drain your body out of blod, he is a large bear sized creature with long arms and three sharp fingers.
        "killable": True,
        "aggressive": True,
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": 0,
        "sprite": "chest",
        "loot": []
    },
     6:  {
        "category": "monster",
        "name": "A resurrected corpse",
        "description": "He has returned back from a long absence,he has returned back from the dead for one reason, to kill you  .
        "killable": True,
        "aggressive": True,
        "attacktrigger": random.randint(1,5)/10,
        "fleetrigger": 0,
        "sprite": "chest",
        "loot": []
    },


     
    
