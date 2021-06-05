from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """Creates a food turtle randomly on the screen"""
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Moves the food once it has been eaten"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
