import os
import pygame
import random
import time
from player import Player
from board import Board
from drawhelper import DrawHelper

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

def hurtPlayer(player, damage):
    #this method is only for testing the HP bar
    player.setHP(player.getHP()-damage)
    play('male_grunt.ogg')

def play(soundfile):
    s = pygame.mixer.Sound(os.path.join('data/sounds', soundfile))
    empty_channel = pygame.mixer.find_channel()
    empty_channel.play(s)

def move(gamestate, pressed_key, gc):
    room_mob = None
    redraw = False
    gamestate = 1
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
                # hämta den mob som man eventuellt lämnar och se till att den slår en hårt och illa
                old_room_mob = gc['board'].getRoomsMob(gc['player'].relcoords())
                try:
                    if old_room_mob.category == 'monster':
                        hurtPlayer(gc['player'], old_room_mob.damage*2)
                except Exception as e:
                    print("Error", e)

                gc['player'].move(move)
                gc['statuscontent']["Coords"].setText("({},{})".format(gc['player'].relcoords()[0],gc['player'].relcoords()[1]))
                gc['board'].set_current_tile(pressed_key)
                room_mob = gc['board'].enter_room(gc['player'].relcoords(),gc['player'].getMobChance())
                # room_mob_list.append(room_mob)
                gc['statuscontent']['Mob'].setText(room_mob.name)
                if room_mob.category == 'monster':
                    play('zombie1.ogg')
                    # pygame.mixer.music.load('thunder.ogg')
                    # pygame.mixer.music.play()
                    gc['statuscontent']['Image'].setImage("swords_crossing_stone.png")
                    gc['statuscontent']['MobHP'].setText("HP: " + str(room_mob.hp))
                    gc['statuscontent']['MobAttack'].setText("Attack: " + str(room_mob.attacktrigger*100)+"%")
                    gc['statuscontent']['MobDamage'].setText("Damage: " + str(room_mob.damage))
                elif room_mob.category == 'trap':
                    play('arrows.ogg')
                    gc['statuscontent']['Image'].setImage("arrows.png")
                    gc['statuscontent']['MobHP'].setText("HP: " + str(room_mob.hp))
                    gc['statuscontent']['MobAttack'].setText("Attack: " + str(room_mob.attacktrigger*100)+"%")
                    gc['statuscontent']['MobDamage'].setText("Damage: " + str(room_mob.damage))
                else:
                    gc['statuscontent']['Image'].setImage("emptyroom.png")
                    gc['statuscontent']['MobHP'].setText("")
                    gc['statuscontent']['MobAttack'].setText("")
                    gc['statuscontent']['MobDamage'].setText("")


                if room_mob.category == 'trap':
                    dice = random.randint(1, 100)
                    print("Nu kommer jag till en fälla")
                    if dice <= room_mob.attacktrigger*100:
                        hurtPlayer(gc['player'], room_mob.damage)
                        print("Jag blev visst skadad")
                # gc['statuscontent']['MobDesc'].setText(room_mob.description)
                gc['statuscontent']["PossibleMoves"].setText("Moves(u,d,l,r): ({})".format(possibleMoves(gc['player'].relcoords()[0],gc['player'].relcoords()[1])))
                gc['statuscontent']['MobAction'].setText("")
                gc['statuscontent']['Attack'].setText("Atk {}".format(gc['player'].getAttack()))
                redraw = True
                gamestate = 2
                if gc['player'].relcoords() == (5,5):
                    gamestate = 3

    return gc, room_mob, redraw, gamestate

def roomAction(gc, room_mob):
    """you will end up here if when you press enter and invoke the action in a room"""
    gc['statuscontent']['MobAction'].setText("")
    gamestate = 2
    # print("room_mob['category']:", room_mob['category'])
    # if mob is a monster when you press enter the player attacks and get attacked back if the mob is still alive
    if room_mob.category == 'monster':
        gc['statuscontent']['MobAction'].setText("You attacked the {}".format(room_mob.name))
        play('jab.ogg')
        damage = random.randint(1, gc['player'].getAttack())
        left = room_mob.hp - damage

        # if mob has any hp left set new hp to that mob and let the mob hit back at the player
        # else mob is dead (set mob hp to 0) and tell that room i doesn't have any mob any more (hasmob = False)
        if left > 0:
            room_mob.setHP(left)
            gc['statuscontent']['MobHP'].setText("HP: " + str(room_mob.hp))
            dice = random.randint(1, 100)
            
            if dice <= room_mob.attacktrigger*100:
                time.sleep(0.5)
                play('chopp.ogg')
                hurtPlayer(gc['player'], room_mob.damage)
            else:
                time.sleep(0.5)
                play('missed_chopp.ogg')
                
        else:
            time.sleep(0.5)
            play('zombie_pain.ogg')
            room_mob.setHP(0)
            gc['board'].setNoMob(gc['player'].relcoords())
            gc['statuscontent']['MobHP'].setText("DEAD!")
            gc['statuscontent']['MobAction'].setText("Monster dropped {}".format(room_mob.getLootDescription()))
            gc['player'].addInventory(room_mob.getLoot())
            gamestate = 1
    elif room_mob.category == 'treasure':
        print("OPEN TREASURE")
        time.sleep(0.5)
        play('open_chest.ogg')
        gc['board'].setNoMob(gc['player'].relcoords())
        gc['statuscontent']['MobAction'].setText("You got {}".format(room_mob.getLootDescription()))
        gc['player'].addInventory(room_mob.getLoot())
    # elif room_mob['category'] == 'trap':
    #     dice = random.randint(1, 100)
    #     print("Nu kommer jag till en fälla")
    #     if dice <= room_mob.attacktrigger*100:
    #         hurtPlayer(gc['statusbar'], gc['statuscontent'], gc['player'], room_mob.damage)
    #         print("Jag blev visst skadad")
    gc['statuscontent']['Attack'].setText("Atk {}".format(gc['player'].getAttack()))
    return gc, room_mob, gamestate
