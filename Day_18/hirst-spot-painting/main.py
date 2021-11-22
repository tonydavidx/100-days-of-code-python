import turtle
from PIL.Image import new
import colorgram
import random

from turtle import Turtle, Screen
t = turtle
tim = Turtle()
screen = Screen()


t.colormode(255)

# rgb_colors = []
# colors = colorgram.extract('spot-paint.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

tim.penup()
tim.speed(0)

colors_list = [(233, 239, 246), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71),
               (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), ]

x = -250
y = -250

tim.goto(x, y)


def one_line():
    for i in range(10):
        tim.dot(20, random.choice(colors_list))
        tim.forward(50)


for _ in range(10):
    y += 50
    tim.goto(x, y)
    one_line()


screen.exitonclick()
