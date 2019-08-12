import pygame
import json

class Diagram:
    def __init__(self):
        self._diagram = None
    
    def loadFromJson(self, filename):
        with open(filename, 'r') as f:
            self._diagram = json.loads(f.read())
            f.close()
        print(self._diagram)
    
    def draw(self):
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        screen.fill((255, 0, 0))
        pygame.draw.circle(screen, (0,0,255), (150, 100), 100)
        pygame.image.save(screen, ".\\output\\test.png")

d = Diagram()
d.loadFromJson("example.json")
