from turtle import Turtle, Screen
import turtle
import random

screen = Screen()
screen.setup(900, 600)

is_race_on = False

user_bet = screen.textinput(
    title='Take your bet', prompt='Pick the turtle color which you think will win\nRed,Blue,Orange,purple').lower()

colors = ['blue', 'orange', 'red', 'purple']
turtles_list = []

x = -400
y = -150

if user_bet:
    is_race_on = True


def create_turtles():
    global y
    for i in range(4):
        my_turtle = Turtle(shape='turtle')
        my_turtle.color(colors[i])
        my_turtle.penup()
        my_turtle.goto(x, y)
        y = y+100
        turtles_list.append(my_turtle)


create_turtles()

while is_race_on:
    for t in turtles_list:

        if t.xcor() > 430:
            is_race_on = False
            winning_colors = t.pencolor()
            if winning_colors == user_bet:
                print(f"You've Won {winning_colors} is the winner")
            else:
                print(f"You've Lost {winning_colors} is the winning color")

        random_movement = random.randint(1, 10)
        t.forward(random_movement)

screen.exitonclick()
