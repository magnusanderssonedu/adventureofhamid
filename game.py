import pygame
from player import Player
from board import Board
from status import Status, StatusContent, StatusContentBar, StatusContentImage
from drawhelper import DrawHelper
from eventhandler import move, roomAction, hurtPlayer

pygame.init()

win = pygame.display.set_mode((830,630))
pygame.display.set_caption("Adventure boardgame")

def id_keys():
    keys = pygame.key.get_pressed() #tuple with all keys represented as 0 or 1 with 1 for pressed
    available_keys = (pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6)    #Place available keys in tuple; represents index of keys
    for key in available_keys:
        if keys[key]:
            return available_keys.index(key) #return between 0-5 depending on key pressed

#main variables and some essential game components
key_down = False
theStatus = Status((630,0),(830,630),(0,0,0))
thePlayer = Player()
run = True
redraw = True   #boolean to minimize number of Blits

theStatusContent = {
    "HP":   StatusContent(text="HP 100", size=24, coords=(650,20)),
    "Attack":   StatusContent(text="Atk 1", size=24, coords=(720,20)),
    "Coords":   StatusContent(text="(0,0)", color=(44,44,44), size=24, coords=(650,50)),
    "PossibleMoves": StatusContent(text="Moves(u,d,l,r): (-,3,-,2)", size=24, coords=(650, 70)),
    "Mob": StatusContent(text="Empty room", size=24, coords=(650, 330), bold=True),
    "MobHP": StatusContent(text="", size=20, coords=(650, 350), bold=False),
    "MobAttack": StatusContent(text="", size=20, coords=(650, 370), bold=False),
    "MobDamage": StatusContent(text="", size=20, coords=(650, 390), bold=False),
    "MobDesc": StatusContent(text="Nothing", size=16, coords=(650, 410)),
    "MobAction": StatusContent(text="", size=16, coords=(650, 310)),
    "Gamestate": StatusContent(text="Gamestate: 1", size=16, coords=(720, 50))
}

theStatusBars = {
    "HP":   StatusContentBar(color=(230,0,0),bgcolor=(40,40,40),dimensions=(170,20),coords=(645,16))
    }

theStatusImages = {
    "Inventory0":   StatusContentImage(coords=(650,90),sprite="loot_nothing.png"),
    "Inventory1":   StatusContentImage(coords=(740,90),sprite="loot_nothing.png"),
    "Inventory2":   StatusContentImage(coords=(650,165),sprite="loot_nothing.png"),
    "Inventory3":   StatusContentImage(coords=(740,165),sprite="loot_nothing.png"),
    "Inventory4":   StatusContentImage(coords=(650,240),sprite="loot_nothing.png"),
    "Inventory5":   StatusContentImage(coords=(740,240),sprite="loot_nothing.png")
    }

splashImages = {
    "GameOver": StatusContentImage(coords=(0,0), sprite="splash_gameover.png"),
    "Winning" : StatusContentImage(coords=(0,0), sprite="splash_win.png"),
    "Opening" : StatusContentImage(coords=(0,0), sprite="splash_intro.png")
}
theSplashScreens = DrawHelper([v for v in splashImages.values()])

gamestate = 0
room_mob = {}
room_mob_list = []
while run:  #main loop

    for event in pygame.event.get():    #event sniffer
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if gamestate in [-1,3]:
                    gamestate = 0
                    redraw = True
                elif gamestate == 0:
                    thePlayer = None
                    thePlayer = Player()
                    theBoard = None
                    theBoard = Board()
                    theBoard.enter_room(thePlayer.relcoords(), hasmob=False)
                    # Set the order of the Objects to be drawn
                    theDrawHelper = None
                    theDrawHelper = DrawHelper()
                    theDrawHelper.addObjects([theBoard,theStatus])
                    theDrawHelper.addObjects([v for v in theStatusBars.values()])
                    theDrawHelper.addObjects([v for v in theStatusImages.values()])
                    theDrawHelper.addObjects([v for v in theStatusContent.values()])
                    theDrawHelper.addObject(thePlayer)
                    gamestate = 1
                    gamecomponents ={
                        'board': theBoard,
                        'player': thePlayer,
                        'statuscontent': theStatusContent,
                        'statusbar': theStatusBars,
                        'statusimages':theStatusImages,
                        'drawhelper': theDrawHelper,
                        'status': theStatus
                    }
                    #hurtPlayer(theStatusBars, theStatusContent, thePlayer, 0)
                    redraw = True
                elif gamestate == 2:
                    gamecomponent, rb, gs = roomAction(gamecomponents, room_mob)
                    room_mob = rb
                    gamestate = gs
                    redraw = True
            else:
                if gamestate in [1,2]:
                    pressed_key = id_keys() # value between -1-5 where value 0-5 means valid key for move
                    gamecomponents, rb, redraw, gs = move(gamestate, pressed_key, gamecomponents)
                    room_mob = rb
                    gamestate = gs

    if thePlayer.getHP() == 0 and gamestate in [1,2]:  #if player gets to 0 HP its Game Over
        gamestate = -1

    theStatusContent['Gamestate'].setText("Gamestate: {}".format(gamestate))

    if gamestate == 0:      #Opening Splash
        theSplashScreens.drawOne(win,2)
        pygame.display.update()
        redraw = False
    elif gamestate == 3:    #Winning
        theSplashScreens.drawOne(win,1)
        pygame.display.update()
        redraw = False
    elif gamestate == -1:   #GameOver
        theSplashScreens.drawOne(win,0)
        pygame.display.update()
        redraw = False
    elif gamestate == 1 or gamestate == 2:
        theStatusBars["HP"].setValue(thePlayer.getHP()/100.0)
        theStatusContent["HP"].setText("HP {:.0f}".format(thePlayer.getHP()))
        if redraw:
            theDrawHelper.draw(win) #DrawHelper manages and draws all the objects in order on the win-surface
            pygame.display.update()
            redraw = False

pygame.quit()
