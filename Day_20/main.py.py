from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()

screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

screen.setup(height=800, width=800)

snake = Snake()

is_game_on = True

screen.listen()

screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.down, key='Down')

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
