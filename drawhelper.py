import pygame

class DrawHelper:
    """Drawing helper

    a Class made to order and run draw methods in existing classes.
    To make it work the drawObjectsList saves a link to the objects and the draw method
    will call the draw methods in the objects by order.
    """

    def __init__(self, listOfObjects=[]):
        self.drawObjectsList = []
        if len(listOfObjects) > 0:
            self.addObjects(listOfObjects)

    def draw(self, surface):
        surface.fill((0,0,0))
        for objects in self.drawObjectsList:
            objects.draw(surface)

    def drawOne(self, surface, index):
        surface.fill((0,0,0))
        self.drawObjectsList[index].draw(surface)

    def addObjects(self, listOfObjects):
        for objects in listOfObjects:
            self.drawObjectsList.append(objects)

    def addObject(self, oneObject):
        self.drawObjectsList.append(oneObject)

    def getDrawObjectsList(self):
        return self.drawObjectsList[:]  #returns a copy of the list

    def delObject(self, index):
        del self.drawObjectsList[index]     #remove object by index

    def removeObject(self,Object):
        self.drawObjectsList.remove(Object) #remove object by object
