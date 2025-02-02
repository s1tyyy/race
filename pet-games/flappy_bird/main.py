import pygame
import random

pygame.init()

HEIGHT = 800
WIDTH = 500
FPS = 60
GRAVITY = 0.5
FLAP_STRENGTH = -10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg = pygame.image.load("sprites/bg.jpg")
bg_img = pygame.transform.scale(bg, (WIDTH, HEIGHT))
bg_rect = bg.get_rect(topleft=(0, 0))

heights = [[100, 300], [200, 400], [300, 500], [400, 600], [500, 700], [150, 350], [250, 450], [350, 550], [450, 650], [550, 750]]

class Bird:
    def __init__(self):
        self.bird = pygame.Rect(WIDTH // 5 - 40, 400, 50, 50)
        self.velocity = 0
        self.img = pygame.image.load("sprites/bird.png")
        self.bird_img = pygame.transform.scale(self.img, (self.bird.width, self.bird.height))
        self.bird_rect = self.bird_img.get_rect(topleft=(self.bird.x, self.bird.y))

        self.top_colm = pygame.Rect(300, 0, 100, 300)
        self.bot_colm = pygame.Rect(300, 500, 100, 800)

        self.top_colm_image = pygame.image.load("sprites/colm_reverse.png")
        self.top_colm_img = pygame.transform.scale(self.top_colm_image, (self.top_colm.width + 100, self.top_colm.height))
        self.top_colm_rect = self.top_colm_img.get_rect(topleft=(self.top_colm.x, self.top_colm.y))

        self.bot_colm_image = pygame.image.load("sprites/colm.png")
        self.bot_colm_img = pygame.transform.scale(self.bot_colm_image, (self.bot_colm.width + 100, self.bot_colm.height))
        self.bot_colm_rect = self.bot_colm_img.get_rect(topleft=(self.bot_colm.x, self.bot_colm.y))

        self.colm_speed = 4
        self.score = 0

    def draw_obj(self, surface):
        surface.blit(self.bird_img, self.bird_rect)
        surface.blit(self.top_colm_img, self.top_colm_rect)
        surface.blit(self.bot_colm_img, self.bot_colm_rect)

    def update(self):
        self.velocity += GRAVITY
        self.bird_rect.y += self.velocity
        self.bird.y += self.velocity

        self.top_colm.x -= self.colm_speed
        self.bot_colm.x -= self.colm_speed
        self.top_colm_rect.x = self.top_colm.x
        self.bot_colm_rect.x = self.bot_colm.x

        if self.bird_rect.y < 0:
            self.bird_rect.y = 0
            self.bird.y = 0
            self.velocity = 0
        elif self.bird_rect.y > HEIGHT - self.bird.height:
            self.bird_rect.y = HEIGHT - self.bird.height
            self.bird.y = HEIGHT - self.bird.height
            self.velocity = 0

        if self.top_colm.x <= -100 and self.bot_colm.x <= -100:
            self.top_colm.x = WIDTH
            self.bot_colm.x = WIDTH

            result_height = random.choice(heights)
            self.top_colm.height = result_height[0]
            self.bot_colm.y = result_height[1]
            self.bot_colm.height = 800 - self.bot_colm.y

            self.top_colm_img = pygame.transform.scale(self.top_colm_image, (self.top_colm.width + 100, self.top_colm.height))
            self.bot_colm_img = pygame.transform.scale(self.bot_colm_image, (self.bot_colm.width + 100, self.bot_colm.height))
            self.top_colm_rect = self.top_colm_img.get_rect(topleft=(self.top_colm.x, self.top_colm.y))
            self.bot_colm_rect = self.bot_colm_img.get_rect(topleft=(self.bot_colm.x, self.bot_colm.y))

            if self.score % 5 == 0:
                self.colm_speed += 1

            self.score += 1

        if self.bird_rect.colliderect(self.top_colm) or self.bird_rect.colliderect(self.bot_colm):
            print("Game Over") #run = False

    def flap(self):
        self.velocity = FLAP_STRENGTH

game = Bird()

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.flap()

    game.update()

    screen.blit(bg_img, bg_rect)
    game.draw_obj(screen)
    pygame.display.flip()

pygame.quit()
