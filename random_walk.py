import random
from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.colormode(255)
t.speed(0)
t.width(5)

while True:
    direction = random.choice([0, 90, 180, 270])
    t.forward(15)
    t.setheading(direction)
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Chooses a random RGB color