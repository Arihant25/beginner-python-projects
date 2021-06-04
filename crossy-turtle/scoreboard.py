from turtle import Turtle

FONT = ("Futura", 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.display_level()
