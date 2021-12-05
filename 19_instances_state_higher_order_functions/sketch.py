from turtle import Turtle, Screen, setheading

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clearn_screen():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()

screen.onkey(key='Right', fun=move_forward)
screen.onkey(key='Left', fun=move_backward)
screen.onkey(key='Up', fun=turn_left)
screen.onkey(key='Down', fun=turn_right)

screen.onkeypress(key='c', fun=clearn_screen)

screen.exitonclick()
