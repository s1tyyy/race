import pygame
import race

class Cars:
    def __init__(self):
        self.sprite_main_car = pygame.image.load("image/classic_car.png")
        self.sprite_main_car = pygame.transform.scale(self.sprite_main_car, (90, 200))
        self.other_blue_car = pygame.image.load("image/other_blue_car.png")
        self.other_blue_car = pygame.transform.scale(self.other_blue_car, (90, 200))
        self.other_red_car = pygame.image.load("image/other_red_car.png")
        self.other_red_car = pygame.transform.scale(self.other_red_car, (90, 200))
        self.other_gray_car = pygame.image.load("image/other_gray_car.png")
        self.other_gray_car = pygame.transform.scale(self.other_gray_car, (90, 200))
        self.other_green_car = pygame.image.load("image/other_green_car.png")
        self.other_green_car = pygame.transform.scale(self.other_green_car, (90, 200))
        self.cars = [self.other_green_car, self.other_red_car, self.other_gray_car, self.other_blue_car]