# # Extracts colors from the image

# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen
import random

color_list = [(1, 12, 31), (53, 25, 17), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24),
              (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163),
              (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147),
              (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]


def random_color():
    return random.choice(color_list)


t = Turtle()
s = Screen()
t.hideturtle()
t.penup()
t.speed(0)
t.setpos(-100, -100)
s.title("Spot Painting by Arihant")
s.colormode(255)

for _ in range(10):
    for _ in range(10):  # Prints 1 row of dots
        t.pendown()
        t.dot(20, random_color())
        t.penup()
        t.forward(50)

    t.penup()
    t.back(50)
    t.sety(t.pos()[1] + 50)
    t.right(180)

s.exitonclick()