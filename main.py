import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

screen.fill((255, 0, 0))

pygame.draw.circle(screen, (0,0,255), (150, 100), 100)

pygame.image.save(screen, ".\\output\\test.png")