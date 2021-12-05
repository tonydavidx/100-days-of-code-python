from turtle import Turtle, Screen
import turtle

tim = Turtle()
screen = Screen()

# def draw_square():
#     for _ in range(4):
#         tim.forward(100)
#         tim.left(90)

# draw_square()


def dash_lines():
    for _ in range(12):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)


dash_lines()

screen.exitonclick()
