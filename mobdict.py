import random
chestloot = ["gold", "torch", "healing water", "sword","jewlery", "food", "stone", "poison"]
monsterloot = ["jewlery", "food", "stone", "dagger"]
mobdict = {
    0: {
        "category": "nothing",
        "name": "Empty room",
        "description": "nothing",
        "hp": (0,0),
        "killable": False,
        "aggressive": False,
        "damage": (0,0),
        "attacktrigger": (0,0),
        "fleetrigger": (0,0),
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
        "hp": (4,10),
        "killable": True,
        "aggressive": True,
        "damage": (1,5),
        "attacktrigger": (1,5),
        "fleetrigger": (1,5),
        "sprite": "zombie",
        "loot": monsterloot
    },
    2: {
        "category": "monster",
        "name": "Troll",
        "description": """Welcome to the death room,
        the Zombie is here. He has
        been here for a long time,
        nobody knows how long
        because nobody has never
        come out of this room alive.
        You will soon enough smell the
        flesh of the zombie. Do not be
        afraid, trust in yourself""",
        "hp": (10,20),
        "killable": True,
        "aggressive": True,
        "damage": (5,15),
        "attacktrigger": (1,3),
        "fleetrigger": (1,3),
        "sprite": "troll",
        "loot": monsterloot
    },
    3: {
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
        "hp": (2,5),
        "killable": True,
        "aggressive": True,
        'damage': (1,5),
        "attacktrigger": (1,5),
        "fleetrigger": (1,8),
        "sprite": "skeleton",
        "loot": monsterloot
    },
    4: {
        "category": "treasure",
        "name": "A Chest",
        "description": """You find a chest full of
        ...what?

        Press action to open.""",
        "hp": (0,0),
        "killable": True,
        "aggressive": False,
        "damage": (0,0),
        "attacktrigger": (0,0),
        "fleetrigger": (0,0),
        "sprite": "chest",
        "loot": chestloot
    },
    5: {
        "category": "trap",
        "name": "Arrows from wall",
        "description": """When you step into the room
        arrows shoots out from small
        holes in the wall!""",
        "hp": (0,0),
        "killable": True,
        "aggressive": True,
        "damage": (1,10),
        "attacktrigger": (1,5),
        "fleetrigger": (0,0),
        "sprite": "chest",
        "loot": ""
    },
    6: {
        "category": "monster",
        "name": "Goblin",
        "description": """Welcome to the death room,
        the Zombie is here. He has
        been here for a long time,
        nobody knows how long
        because nobody has never
        come out of this room alive.
        You will soon enough smell the
        flesh of the zombie. Do not be
        afraid, trust in yourself""",
        "hp": (1,3),
        "killable": True,
        "aggressive": True,
        "damage": (1,3),
        "attacktrigger": (1,6),
        "fleetrigger": (1,3),
        "sprite": "troll",
        "loot": monsterloot
    },

}
