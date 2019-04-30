import pygame

class Status:
    coords = (0,0)
    dimensions = (0,0)
    bgcolor = (0,0,0)

    def __init__(self, coords=(300,0), dimensions=(100,200), bgcolor=(0,0,0)):
        self.coords = coords
        self.dimensions = dimensions
        self.bgcolor = bgcolor

    def draw(self, surface):
        pygame.draw.rect(surface, self.bgcolor, [self.coords[0],self.coords[1],self.dimensions[0],self.dimensions[1]])


class StatusContent:
    text = ""
    size = 12
    color = (255,255,255)
    statcoords = (0,0)
    bold = False
    italic = False
    fontobj = False

    def __init__(self, text="",size=12,color = (255,255,255),coords=(0,0),bold=False,italic=False):
        self.text = text
        self.size = size
        self.color = color
        self.statcoords = coords
        self.bold = bold
        self.italic = italic
        self.fontobj = pygame.font.SysFont("sans serif",self.size,self.bold,self.italic)

    def draw(self):
        TextSurface = self.fontobj.render(self.text, True, self.color)
        return TextSurface

    def coords(self):
        return self.statcoords

    def set_text(self,text):
        self.text = text