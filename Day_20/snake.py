from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(self.x, self.y)
            self.x = self.x-20
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            newx = self.segments[seg_num-1].xcor()
            newy = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(newx, newy)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
