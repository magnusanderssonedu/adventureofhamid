import pygame

def key_diff(cur,pres): #returns difference between two keys using the key-tuple
    return postuple(cur) - postuple(pres)

def postuple(i):    #returns specific key from tuple
    return (1,2,3,4,5,6)[i]

def possibleMoves(x,y):
    #take it easy, I made the list in Excel
    validmove = (('-,3,-,2','-,4,1,3','-,5,2,4','-,6,3,5','-,1,4,6','-,2,5,-'),
('1,5,-,4','2,6,3,5','3,1,4,6','4,2,5,1','5,3,6,2','6,4,1,-'),
('3,1,-,6','4,2,5,1','5,3,6,2','6,4,1,3','1,5,2,4','2,6,3,-'),
('5,3,-,2','6,4,1,3','1,5,2,4','2,6,3,5','3,1,4,6','4,2,5,-'),
('1,5,-,4','2,6,3,5','3,1,4,6','4,2,5,1','5,3,6,2','6,4,1,-'),
('3,-,-,6','4,-,5,1','5,-,6,2','6,-,1,3','1,-,2,4','2,-,3,-'))

    return validmove[y][x]

def move(gamestate, pressed_key, gc):
    room_mob = {}
    redraw = False
    if pressed_key >= 0:      
        move = (0,0)
        if gc['board'].get_current_tile != pressed_key:
            #check for the difference between last key and pressed key
            if key_diff(gc['board'].get_current_tile(),pressed_key) == -1 or key_diff(gc['board'].get_current_tile(),pressed_key) == 5: #moved_right
                move=(1,0)
            if key_diff(gc['board'].get_current_tile(),pressed_key) == 1 or key_diff(gc['board'].get_current_tile(),pressed_key) == -5:  #moved_left
                move=(-1,0)
            if key_diff(gc['board'].get_current_tile(),pressed_key) == -2 or key_diff(gc['board'].get_current_tile(),pressed_key) == 4:  #moved_down
                move=(0,1)
            if key_diff(gc['board'].get_current_tile(),pressed_key) == 2 or key_diff(gc['board'].get_current_tile(),pressed_key) == -4:  #moved_up
                move=(0,-1)
            if gc['board'].is_validmove(move, gc['player'].relcoords()):
                gc['player'].move(move)
                gc['statuscontent']["Coords"].setText("({},{})".format(gc['player'].relcoords()[0],gc['player'].relcoords()[1]))
                gc['board'].set_current_tile(pressed_key)
                room_mob = gc['board'].enter_room(gc['player'].relcoords())
                # room_mob_list.append(room_mob)
                gc['statuscontent']['Mob'].setText(room_mob["name"])
                if room_mob['category'] == 'monster':
                    gc['statuscontent']['MobHP'].setText("HP: " + str(room_mob['hp']))
                else:
                    gc['statuscontent']['MobHP'].setText("")
                gc['statuscontent']['MobDesc'].setText(room_mob['description'])
                gc['statuscontent']["PossibleMoves"].setText("Moves(u,d,l,r): ({})".format(possibleMoves(gc['player'].relcoords()[0],gc['player'].relcoords()[1])))
                redraw = True
                gamestate = 2

    return gc, room_mob, redraw

def roomAction(gc, room_mob):
    """you will end up here if when you press enter and invoke the action in a room"""
    gc['statuscontent']['MobAction'].setText("")
    if room_mob['category'] == 'monster':
        gc['statuscontent']['MobAction'].setText("You attacked the {}".format(room_mob['name']))

    elif room_mob['category'] == 'treasure':
        print("OPEN TREASURE")
        theStatusContent['MobAction'].setText("Open {}?\nPress enter".format(room_mob['name']))
    elif room_mob['category'] == 'trap':
        print("IT'S A TRAP")