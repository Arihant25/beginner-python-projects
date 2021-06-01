from turtle import Turtle

STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Used to initialize the three turtles"""

        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.setx(position)
            self.segments.append(new_segment)

    def move(self):
        """Moves the last segment to the second-last segment, the second-last segment to the third-last segment,
        and so on"""

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # X coordinate of the second-last segment
            new_y = self.segments[seg_num - 1].ycor()  # Y coordinate of the second-last
            self.segments[seg_num].goto(new_x, new_y)  # Sets the coordinates of the last segment
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

