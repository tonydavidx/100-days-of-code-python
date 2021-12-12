from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

tim = Turtle()
screen = Screen()

tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


r = 100


def spirograph(gap):
    for r in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading
                       ()+gap)


spirograph(10)

screen.exitonclick()
