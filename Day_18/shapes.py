from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ['CadetBlue', 'Brown', 'aquamarine',
          'DarkBlue', 'DarkGreen', 'DarkCyan', 'DeepPink', 'DarkViolet']


def draw_shapes(number_of_shapes):
    angle = 360 / number_of_shapes
    for _ in range(number_of_shapes):
        tim.forward(100)
        tim.right(angle)


for shapes_num in range(3, 11):
    tim.color(random.choice(colors))
    draw_shapes(shapes_num)


screen = Screen()

screen.exitonclick()
