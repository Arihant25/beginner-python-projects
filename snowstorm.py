import random
from turtle import *

colors = ["aquamarine", "cyan", "plum", "dark orchid", "LimeGreen", "goldenrod", "lemon chiffon", "HotPink", "DarkKhaki", "DarkOrange", "red", "green", "blue", "yellow", "orange", "purple", "black", "white"]

shape("turtle")
speed(10)
pencolor("white")
pensize(6)
Screen().bgcolor("turquoise")

def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)

def snowflakeArm(size):
    for x in range(0, 4):
        forward(size)
        vshape(size)
    backward(size*4)

def snowflake(size):
    color(random.choice(colors))
    for x in range(0, 6):
        snowflakeArm(size)
        right(60)

for i in range(0,10):
    size = random.randint(5,30)
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    penup()
    goto(x,y)
    pendown()
    snowflake(size)
