from turtle import Turtle, Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()

screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

screen.setup(height=800, width=800)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
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

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.add_score()

    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        scoreboard.reset_score()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
