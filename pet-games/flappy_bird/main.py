import pygame
from pygame import K_SPACE

pygame.init()

HEIGHT = 800
WIDTH = 500
FPS = 60

class Bird:
    def __init__(self):
        self.bird = pygame.Rect(WIDTH // 5 - 40, HEIGHT // 2, 50, 50)
        self.step = 10

    def draw_obj(self, surface):
        pygame.draw.rect(surface, "red", self.bird)

    def move_bird(self):
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            self.bird.y -= self.step

run = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game = Bird()
clock = pygame.time.Clock()

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    screen.fill("white")
    clock.tick(FPS)
    game.draw_obj(screen)
    game.move_bird()
    pygame.display.flip()

pygame.quit()