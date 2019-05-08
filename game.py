import pygame
from player import Player
from board import Board
from status import Status, StatusContent

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
    return -1

def key_diff(cur,pres): #returns difference between two keys using the key-tuple
    return postuple(cur) - postuple(pres)

def postuple(i):    #returns specific key from tuple
    return (1,2,3,4,5,6)[i]
    
thePlayer = Player()
theBoard = Board()

# Entering first room and setting tile
theBoard.enter_room(thePlayer.relcoords())


# theStatus = Status((804,0),(246,630),(0,0,0))
theStatus = Status((630,0),(830,630),(0,0,0))
theStatusContent = []
theStatusContent.append(StatusContent(text="HP=100", size=24, coords=(650,20)))
theStatusContent.append(StatusContent(text="Steps=4", size=24, coords=(650,50)))
theStatusContent.append(StatusContent(text="Throw die", size=24, coords=(650,80)))
theStatusContent.append(StatusContent(text="(0,0)", color=(44,44,44), size=24, coords=(650,200)))
theStatusContent.append(StatusContent(text="Exits: e s", size=24, coords=(650, 250)))
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
                            theStatusContent[3].set_text("({},{})".format(thePlayer.relcoords()[0],thePlayer.relcoords()[1]))
                            theBoard.set_current_tile(pressed_key)
                            theBoard.enter_room(thePlayer.relcoords())
                            theStatusContent[4].set_text("Exits: " + theBoard.room_exits(thePlayer.relcoords()))
                                        
        if event.type == pygame.KEYUP:
            key_down = False    #key up means player token is moved
    
    win.fill((0,0,0))
    win.blit(theBoard.draw(), theBoard.coords())
    # bliting tiles
    for t in theBoard.getTiles():
        win.blit(t[1], t[0])
    win.blit(thePlayer.draw(), thePlayer.coords())
    theStatus.draw(win)
    for draw_text in theStatusContent:
        win.blit(draw_text.draw(), draw_text.coords())
    pygame.display.update()

pygame.quit()