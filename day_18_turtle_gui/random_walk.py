import turtle as t
import random


tim = t.Turtle()
screen = t.Screen()

t.colormode(255)


def random_color():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    return (a, b, c)


tim.speed('fast')

directions = [0, 90, 180, 270]

tim.pensize(10)


def random_walk(steps):
    for _ in range(steps):
        tim.color(random_color())
        tim.setheading(random.choice(directions))
        tim.forward(30)


random_walk(random.randint(100, 200))

screen.exitonclick()
