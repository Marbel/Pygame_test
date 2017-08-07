import pygame

pygame.init()
screen = pygame.display.set_mode((900,700))

finished = False

while finished == False:
    for event in pygame.event.get():
        
