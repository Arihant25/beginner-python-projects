from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Segoe UI", 14, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.sety(275)
        self.color('white')
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.sety(0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
