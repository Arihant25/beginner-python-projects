from turtle import Turtle, Screen, colormode
import random

t = Turtle()
s = Screen()

s.colormode(255)

def polygon(sides):
    for i in range(sides):
        t.forward(100)
        t.right(360 / sides)
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # Chooses a random RGB color


for _ in range (3, 11):
    polygon(_)

s.exitonclick()


