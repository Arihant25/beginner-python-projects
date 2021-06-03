from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.sety(200)

    def increase_r_score(self):
        self.r_score += 1

    def increase_l_score(self):
        self.l_score += 1

    def display_score(self):
        self.clear()
        self.write(arg=f"{self.l_score}          {self.r_score}", align='center', font=("Roboto", 40, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER', align='center', font=("Roboto", 40, 'normal'))
