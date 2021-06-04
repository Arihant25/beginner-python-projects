from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from timer import Timer
import time


# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize the game elements
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
timer = Timer()

# Listen for key presses
screen.listen()
screen.onkey(fun=player.move_up, key="Up")
# Uncomment these if you want to enable additional controls.
# screen.onkey(fun=player.move_down, key="Down")
# screen.onkey(fun=player.move_left, key="Left")
# screen.onkey(fun=player.move_right, key="Right")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    timer.display_time()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect if player has crossed the game edges
    if player.xcor() > 285 or player.xcor() < -290 or player.ycor() < -290:
        screen.update()
        game_is_on = False
        scoreboard.game_over()

    # Detect successful crossing
    if player.ycor() > 280:
        scoreboard.level_up()
        car_manager.level_up()
        player.start()

    #  Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            screen.update()
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
