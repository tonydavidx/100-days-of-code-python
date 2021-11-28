import random
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_car()

    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            score.game_over_text()
            game_is_on = False

    if player.is_at_finish():
        player.reset_position()
        carmanager.increase_car_speed()
        score.update_score()


screen.exitonclick()
