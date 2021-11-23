from turtle import Turtle, Screen
import turtle

screen = Screen()
screen.setup(900, 600)
user_bet = screen.textinput(
    title='Take your bet', prompt='Pick the turtle color which you think will win\nRed,Blue,Orange,purple').lower()

colors = ['blue', 'orange', 'red', 'purple']
turtle_names = ['Leo', 'Mike', 'Ralph', 'Donny']


def create_turtles():
    for t in turtle_names:
        t = turtle.Turtle()
        t.penup()
        t.goto(-400, -250)


create_turtles()

screen.exitonclick()
