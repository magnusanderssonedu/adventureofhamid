import pygame
from player import Player
from board import Board
from status import Status, StatusContent, StatusContentBar

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

def key_diff(cur,pres): #returns difference between two keys using the key-tuple
    return postuple(cur) - postuple(pres)

def postuple(i):    #returns specific key from tuple
    return (1,2,3,4,5,6)[i]

thePlayer = Player()
theBoard = Board()

def hurtPlayer():
    #this method is only for testing the HP bar
    thePlayer.setHP(thePlayer.getHP()-2)
    theStatusBars["HP"].setValue(thePlayer.getHP()/100.0)
    theStatusContent["HP"].set_text("HP {:.0f}".format(thePlayer.getHP()))

def possibleMoves(x,y):
    #take it easy, I made the list in Excel
    validmove = (('-,3,-,2','-,4,1,3','-,5,2,4','-,6,3,5','-,1,4,6','-,2,5,-'),
('1,5,-,4','2,6,3,5','3,1,4,6','4,2,5,1','5,3,6,2','6,4,1,-'),
('3,1,-,6','4,2,5,1','5,3,6,2','6,4,1,3','1,5,2,4','2,6,3,-'),
('5,3,-,2','6,4,1,3','1,5,2,4','2,6,3,5','3,1,4,6','4,2,5,-'),
('1,5,-,4','2,6,3,5','3,1,4,6','4,2,5,1','5,3,6,2','6,4,1,-'),
('3,-,-,6','4,-,5,1','5,-,6,2','6,-,1,3','1,-,2,4','2,-,3,-'))

    return validmove[y][x]

# Entering first room and setting tile
theBoard.enter_room(thePlayer.relcoords())


# theStatus = Status((804,0),(246,630),(0,0,0))
theStatus = Status((630,0),(830,630),(0,0,0))
theStatusContent = {
    "HP":   StatusContent(text="HP 100", size=24, coords=(650,20)),
    "Throw":  StatusContent(text="Throw die", size=24, coords=(650,80)),
    "Coords":   StatusContent(text="(0,0)", color=(44,44,44), size=24, coords=(650,200)),
    "Exits":    StatusContent(text="Exits: e s", size=24, coords=(650, 250)),
    "PossibleMoves": StatusContent(text="Moves(u,d,l,r): (-,3,-,2)", size=24, coords=(650, 300))
}

theStatusBars = {
    "HP":   StatusContentBar(color=(230,0,0),bgcolor=(40,40,40),dimensions=(170,20),coords=(645,16))
    }
run = True

while run:  #main loop

    for event in pygame.event.get():    #event sniffer
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:    #handeling key event
            if not key_down:    #the player token will be constantly triggering this event, so just check if the token is moved to save time
                pressed_key = id_keys() # value between -1-5 where value 0-5 means valid key for move
                if pressed_key >= 0:
                    key_down = True
                    move = (0,0)
                    if theBoard.get_current_tile != pressed_key:
                        #check for the difference between last key and pressed key
                        if key_diff(theBoard.get_current_tile(),pressed_key) == -1 or key_diff(theBoard.get_current_tile(),pressed_key) == 5: #moved_right
                            move=(1,0)
                        if key_diff(theBoard.get_current_tile(),pressed_key) == 1 or key_diff(theBoard.get_current_tile(),pressed_key) == -5:  #moved_left
                            move=(-1,0)
                        if key_diff(theBoard.get_current_tile(),pressed_key) == -2 or key_diff(theBoard.get_current_tile(),pressed_key) == 4:  #moved_down
                            move=(0,1)
                        if key_diff(theBoard.get_current_tile(),pressed_key) == 2 or key_diff(theBoard.get_current_tile(),pressed_key) == -4:  #moved_up
                            move=(0,-1)
                        if theBoard.is_validmove(move, thePlayer.relcoords()):
                            thePlayer.move(move)
                            theStatusContent["Coords"].set_text("({},{})".format(thePlayer.relcoords()[0],thePlayer.relcoords()[1]))
                            theBoard.set_current_tile(pressed_key)
                            theBoard.enter_room(thePlayer.relcoords())
                            theStatusContent["Exits"].set_text("Exits: " + theBoard.room_exits(thePlayer.relcoords()))
                            theStatusContent["PossibleMoves"].set_text("Moves(u,d,l,r): ({})".format(possibleMoves(thePlayer.relcoords()[0],thePlayer.relcoords()[1])))

        if event.type == pygame.KEYUP:
            key_down = False    #key up means player token is moved

    win.fill((0,0,0))
    win.blit(theBoard.draw(), theBoard.coords())
    # bliting tiles
    for t in theBoard.getTiles():
        win.blit(t[2], t[0])
        win.blit(t[1], t[0])
    win.blit(thePlayer.draw(), thePlayer.coords())
    #bliting statusBar and content
    win.blit(theStatus.draw(), theStatus.coords())
    for bars,draw_bars in theStatusBars.items():
        draw_bars.draw(win)
    for text,draw_text in theStatusContent.items():
        win.blit(draw_text.draw(), draw_text.coords())
    pygame.display.update()

pygame.quit()
