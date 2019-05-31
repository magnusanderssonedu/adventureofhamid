import pygame
import os

class Status:
    statuscoords = (0,0)
    dimensions = (0,0)
    bgcolor = (0,0,0)
    me = pygame.image.load(os.path.join('data', 'statusbar.png'))

    def __init__(self, statuscoords=(300,0), dimensions=(100,200), bgcolor=(0,0,0)):
        self.statuscoords = statuscoords
        self.dimensions = dimensions
        self.bgcolor = bgcolor

    #def draw(self, win):   //Sparar denna så länge
        #pygame.draw.rect(surface, self.bgcolor, [self.coords[0],self.coords[1],self.dimensions[0],self.dimensions[1]])

    def draw(self,surface):
        surface.blit(self.me, (self.statuscoords[0],self.statuscoords[1]))
        #return self.me

    def coords(self):
        return (self.statuscoords[0],self.statuscoords[1])

class StatusImage:
    image = ""
    coords = (0,0)
    def __init__(self, image="", coords=(0,0)):
        self.image = image
        self.coords = coords

    def setImage(self, image):
        self.image = image

    def draw(self, surface):
        surface.blit(pygame.image.load(os.path.join('data/statusbarimages', self.image)), (self.coords[0], self.coords[1]))

class StatusContent:
    textArray = []
    size = 12
    color = (255,255,255)
    statcoords = (0,0)
    bold = False
    italic = False
    fontobj = False

    def __init__(self, text="",size=12,color = (255,255,255),coords=(0,0),bold=False,italic=False):
        self.setText(text)
        self.size = size
        self.color = color
        self.statcoords = coords
        self.bold = bold
        self.italic = italic
        self.fontobj = pygame.font.SysFont("sans serif",self.size,self.bold,self.italic)

    def draw(self,surface):
        n = 0
        for text in self.textArray:
            TextSurface = self.fontobj.render(text, True, self.color)
            surface.blit(TextSurface, (self.statcoords[0],self.statcoords[1]+n*self.size))
            n += 1

    def coords(self):
        return self.statcoords

    def setText(self,text):
        if text.find("\n") > -1:
            self.textArray = text.split("\n")
            n = 0
            for text in self.textArray:
                self.textArray[n] = text.strip()
                n += 1
        else:
            self.textArray = [text]

class StatusContentBar:
    dimensions = (180,20)
    coords = (600,20)
    bgcolor = (0,0,0)
    color = (255,0,0)
    value = 1.0

    def __init__(self, dimensions = (180,20),coords = (600,20),bgcolor = (0,0,0),color = (255,0,0),value=1.0):
        self.dimensions = dimensions
        self.coords = coords
        self.bgcolor = bgcolor
        self.color = color
        self.value = value

    def setValue(self,val):
        self.value = val

    def setColor(self,color):
        self.color = color

    def draw(self, win):
        #draw background
        pygame.draw.rect(win, self.bgcolor, [self.coords[0],self.coords[1],self.dimensions[0],self.dimensions[1]])
        #draw foreground
        pygame.draw.rect(win, self.color, [self.coords[0]+1,self.coords[1]+1,self.value*(self.dimensions[0]-2),self.dimensions[1]-2])
