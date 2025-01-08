import pygame
import random
import cars

pygame.init()
WIDTH = 500
HEIGHT = 900
FPS = 120

def random_choice(list):
    a, b = random.choice(list)
    return random.randint(a, b)   #Первая полоса 30-45 Вторая полоса 140-155  Третья полоса 250- 270  Четвертая полоса 360-385

class Player(cars.Cars):
    def __init__(self):
        super().__init__()
        self.main_car = pygame.Rect((WIDTH // 2 - 50, 600, 90, 200))
        self.other_cars = pygame.Rect((random.randint(10, 400), 0 - 100, 90, 200))
        self.other_speed = 10
        self.rand_car = random.choice(self.cars)

    def draw_cars(self):
        screen.blit(self.sprite_main_car, self.main_car)
        screen.blit(self.rand_car, self.other_cars)

    def main_car_move(self, speed):
        self.main_car.x += speed
        if self.main_car.x >= WIDTH - self.main_car.width:
            self.main_car.x = WIDTH - self.main_car.width
        if self.main_car.x <= 0:
            self.main_car.x = 0

    def vertical_car_move(self, speed):
        self.main_car.y += speed
        if self.main_car.y >= HEIGHT - self.main_car.height:
            self.main_car.y = HEIGHT - self.main_car.height
        if self.main_car.y <= 0:
            self.main_car.y = 0

    def other_car_move(self):
        self.other_cars.y += self.other_speed
        if self.other_cars.y >= HEIGHT:
            self.other_cars.x = random_choice(pos)
            self.other_cars.y = 0 - 100
            self.other_speed += 0.3
            self.rand_car = random.choice(self.cars)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
main = Player()
pos = [(30, 35), (140, 155), (250, 270), (360, 385)]
roads_sprites = ["image/road.jpg", "image/road2.jpg", "image/road3.jpg", "image/road4.jpg"]
run = True

while run:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    road = pygame.image.load(random.choice(roads_sprites))
    road_map = pygame.transform.scale(road, (WIDTH, HEIGHT))
    road_map_rect = road_map.get_rect()
    screen.blit(road_map, road_map_rect)
    main.draw_cars()
    if keys[pygame.K_a]:
        main.main_car_move(-10)
    elif keys[pygame.K_d]:
        main.main_car_move(10)
    if keys[pygame.K_w]:
        main.vertical_car_move(-10)
    elif keys[pygame.K_s]:
        main.vertical_car_move(10)
    main.other_car_move()
    if main.main_car.colliderect(main.other_cars):
        print("авария")
    pygame.display.flip()

pygame.quit()
