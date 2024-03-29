import random
from turtle import *

colors = ["aquamarine", "cyan", "plum", "dark orchid", "LimeGreen", "goldenrod", "lemon chiffon",
          "HotPink", "DarkKhaki", "DarkOrange", "red", "green", "blue", "yellow", "orange", "purple"]

shape("turtle")
speed(5)
pencolor("white")
pensize(6)
Screen().bgcolor("turquoise")


def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)


def snowflakeArm():
    for _ in range(0, 4):
        forward(30)
        vshape()
    backward(120)


def snowflake():
    for _ in range(0, 6):
        color(random.choice(colors))
        snowflakeArm()
        right(60)


snowflake()
