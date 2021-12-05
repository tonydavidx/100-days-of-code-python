from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title('Pong - 100 days of code')
screen.bgcolor('black')
screen.setup(height=800, width=1200)
screen.tracer(0)

is_game_on = True
screen.listen()

r_paddle = Paddle((550, 0))
l_paddle = Paddle((-550, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.onkeypress(fun=r_paddle.move_up, key='Up')
screen.onkeypress(fun=r_paddle.move_down, key='Down')

screen.onkeypress(fun=l_paddle.move_up, key='w')
screen.onkeypress(fun=l_paddle.move_down, key='s')

while is_game_on:
    time.sleep(0.02)
    screen.update()
    ball.move()
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # detect collision
    if ball.xcor() > 520 and ball.distance(r_paddle) < 100:
        ball.bounce_x()

    if ball.xcor() < -520 and ball.distance(l_paddle) < 100:
        ball.bounce_x()

    if ball.xcor() > 580:
        ball.reset_position()
        scoreboard.point_left()

    if ball.xcor() < -580:
        ball.reset_position()
        scoreboard.point_right()

screen.exitonclick()
