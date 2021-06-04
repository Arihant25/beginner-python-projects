from turtle import Turtle

FONT = ("Futura", 24, 'normal')


class Timer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(110, 255)
        self.time = 0
        self.display_time()

    def display_time(self):
        self.clear()
        self.time += 0.1
        self.write(arg=f"Time: {round(self.time, 2)}", align="left", font=FONT)
