from turtle import Turtle, Screen

tim = Turtle()


def triangle():
    for _ in range(3):
        tim.forward(100)
        tim.right(120)


triangle()

screen = Screen()

screen.exitonclick()
