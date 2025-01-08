import pygame
import random
import cars
import menu

pygame.init()
WIDTH = 500
HEIGHT = 900
FPS = 120

def random_choice(list):
    a, b = random.choice(list)
    return random.randint(a, b)

def disable():
    global state
    main_menu.disable()
    state = "game"

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
main_menu = menu.Menu(screen)
play = main_menu.add.button("Играть", disable)
difficulty = main_menu.add.range_slider("Сложность", 1, (1, 2, 3, 4, 5))
main_menu.add.button("Выход", quit)
pos = [(30, 35), (140, 155), (250, 270), (360, 385)]
roads_sprites = ["image/road.jpg", "image/road2.jpg", "image/road3.jpg", "image/road4.jpg"]
state = "menu"
run = True


while run:
    clock.tick(FPS)
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in events:
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
    if state == "game":
        main.other_car_move()
    if main.main_car.colliderect(main.other_cars):
        state = "menu"
        main_menu.enable()
        main.other_cars.y = 0 - 100
        main.other_cars.x = random_choice(pos)
        main.speed = 10
    main_menu.flip2(events)
    pygame.display.flip()

pygame.quit()
