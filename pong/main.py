from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Arihant's Pong")
screen.tracer(0)

# Create the game elements
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Control the paddles
screen.listen()
screen.onkey(key='Up', fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key='w', fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    scoreboard.display_score()
    ball.move()

    # Detect collision with top/bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle misses the ball
    if ball.xcor() > 380:
        ball.center()
        scoreboard.increase_l_score()
        ball.bounce_x()

    # Detect if left paddle misses the ball
    if ball.xcor() < -380:
        ball.center()
        scoreboard.increase_r_score()
        ball.bounce_x()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        scoreboard.display_score()
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
