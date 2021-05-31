from turtle import Turtle, Screen
import random as R

t = Turtle()
s = Screen()
t.speed("fastest")
s.colormode(255)

def random_color():
    """Returns a random RGB color value"""
    r = R.randint(0, 255)
    g = R.randint(0, 255)
    b = R.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)
        t.color(random_color())


draw_spirograph(1) # Change this number to 10 to get a simpler effect

s.exitonclick()