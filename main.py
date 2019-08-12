import pygame
import json

class Diagram:
    def __init__(self):
        self.diagram = None
        self.font = None
    
    def loadFromJson(self, filename):
        with open(filename, 'r') as f:
            self.diagram = json.loads(f.read())
            f.close()
    
    def draw(self):
        pygame.init()
        self.loadFonts()
        screen = pygame.display.set_mode((1024, 768))
        screen.fill((255, 255, 255))
        self.drawDiagram(screen)
        pygame.image.save(screen, ".\\output\\test.png")
        pygame.quit()
    
    def loadFonts(self):
        pygame.font.init()
        fname = pygame.font.get_default_font()
        self.font = pygame.font.Font(fname, 12)
    
    def getTextSurface(self, text):
        if not pygame.font.get_init():
            raise Exception("intialise fonts first")
        return self.font.render(text, 1, (0,0,0))

    def drawDiagram(self, surface):
        for block in self.diagram["blocks"]:
            self.drawBlock(surface, block)
    
    def drawBlock(self, surface, block):
        rect = pygame.Rect(block["x"], block["y"], 100, 50)
        pygame.draw.rect(surface, (255,255,255), rect)
        pygame.draw.rect(surface, (0,0,0), rect, 1)
        textSurface = self.getTextSurface(block["text"])
        surface.blit(textSurface, (rect.centerx - textSurface.get_width() / 2, rect.centery - textSurface.get_height() / 2))

d = Diagram()
d.loadFromJson("example.json")
d.draw()
