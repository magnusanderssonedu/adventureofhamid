import pygame
import os
from player import Player
from board import Board
from status import Status, StatusContent, StatusContentBar, StatusImage
from drawhelper import DrawHelper

from eventhandler import move, roomAction




pygame.init()

win = pygame.display.set_mode((830,630))
pygame.display.set_caption("Adventure boardgame")

#main variables
key_down = False

def id_keys():
    keys = pygame.key.get_pressed() #tuple with all keys represented as 0 or 1 with 1 for pressed
    available_keys = (pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6)    #Place available keys in tuple; represents index of keys
    for key in available_keys:
        if keys[key]:
            return available_keys.index(key) #return between 0-5 depending on key pressed
    if keys[pygame.K_0]: #ONLY FOR PLAYING AROUND - I WANT TO HURT THE PLAYER! Press zero to hurt player
        hurtPlayer()
    return -1

thePlayer = Player()
theBoard = Board()





# Entering first room and setting tile
theBoard.enter_room(thePlayer.relcoords(), hasmob=False)


# theStatus = Status((804,0),(246,630),(0,0,0))
theStatus = Status((630,0),(830,630),(0,0,0))
theStatusContent = {
    "HP":   StatusContent(text="HP 100", size=24, coords=(650,20)),
    "Throw":  StatusContent(text="Throw die", size=24, coords=(650,80)),
    "Coords":   StatusContent(text="(0,0)", color=(44,44,44), size=24, coords=(650,50)),
    "PossibleMoves": StatusContent(text="Moves(u,d,l,r): (-,3,-,2)", size=24, coords=(650, 110)),
    "Mob": StatusContent(text="Empty room", size=24, coords=(650, 330), bold=True),
    "MobHP": StatusContent(text="", size=20, coords=(650, 350), bold=False),
    "MobAttack": StatusContent(text="", size=20, coords=(650, 370), bold=False),
    "MobDamage": StatusContent(text="", size=20, coords=(650, 390), bold=False),
    "MobDesc": StatusContent(text="Nothing", size=16, coords=(650, 410)),
    "MobAction": StatusContent(text="", size=16, coords=(650, 310)),
    "Gamestate": StatusContent(text="Gamestate: 1", size=16, coords=(650, 130)),
    "Image": StatusImage(image='emptyroom.png', coords=(680, 150))
}



theStatusBars = {
    "HP":   StatusContentBar(color=(230,0,0),bgcolor=(40,40,40),dimensions=(170,20),coords=(645,16))
    }
run = True

gamecomponents ={
    'board': theBoard,
    'player': thePlayer,
    'statuscontent': theStatusContent,
    'statusbar': theStatusBars
}

# Set the order of the Objects to be drawn
theDrawHelper = DrawHelper([theBoard,thePlayer,theStatus])
theDrawHelper.addObjects([v for v in theStatusBars.values()])
theDrawHelper.addObjects([v for v in theStatusContent.values()])
redraw = True   #boolean to minimize number of Blits

pygame.mixer.init()
# pygame.mixer.music.load(os.path.join('data/sounds', 'waterdrops.mp3'))
pygame.mixer.music.load(os.path.join('data/sounds', 'waterdrops.ogg'))
pygame.mixer.music.play(-1)

gamestate = 1
room_mob = {}
room_mob_list = []
while run:  #main loop

    for event in pygame.event.get():    #event sniffer
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if gamestate == 2:
                    gamecomponent, rb, gs = roomAction(gamecomponents, room_mob)
                    room_mob = rb
                    gamestate = gs
            else:
                pressed_key = id_keys() # value between -1-5 where value 0-5 means valid key for move
                gamecomponents, rb, redraw, gs = move(gamestate, pressed_key, gamecomponents)
                room_mob = rb
                gamestate = gs

    gamecomponents['statuscontent']['Gamestate'].setText("Gamestate: {}".format(gamestate))
        
    if redraw:
        theDrawHelper.draw(win) #DrawHelper manages and draws all the objects in order on the win-surface
        pygame.display.update()
        

    

pygame.quit()


