import turtle
from turtle import Turtle
import random

COLORS = ['red', 'yellow', 'orange', 'green', 'purple', 'blue', 'maroon', 'violet', 'pink', 'black', 'cyan', 'brown',
          'YellowGreen', 'magenta', 'indigo', 'fuchsia', 'gold', 'turquoise', 'orchid', 'aquamarine']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Has a 1 in 6 chance of creating a car"""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(1, 2)
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            random_y = random.randint(-250, 250)
            new_car.setposition(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
