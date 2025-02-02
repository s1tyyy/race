import pygame

pygame.init()

HEIGHT = 800
WIDTH = 400

run = True

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

pygame.quit()