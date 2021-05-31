from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput("Make Your Bet", "Which turtle is going to win the race?\n Enter a color from the rainbow:").lower()

all_turtles = []
color_list = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
y_pos = [150, 100, 50, 0, -50, -100, -150]

for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    new_turtle.color(color_list[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if user_bet == winner:
    print("You've won the race!")

else:
    print("You lost the race.")

print(f"The winner was {winner}!")

screen.exitonclick()
