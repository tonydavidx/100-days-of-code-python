from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(random_x, random_y)
