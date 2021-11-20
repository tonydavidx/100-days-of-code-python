from turtle import Turtle, Screen
import random
import turtle

tim = Turtle()
screen = Screen()
random_x = random.randint(50, 70)
random_Y = random.randint(50, 70)


colors = ['CadetBlue', 'Brown', 'aquamarine',
          'DarkBlue', 'DarkGreen', 'DarkCyan', 'DeepPink', 'DarkViolet']

tim.hideturtle()
tim.penup()
tim.width(10)
tim.sety(screen.window_height() / random_Y)
tim.setx(screen.window_width() / random_x)
tim.showturtle()
tim.pendown()

tim.speed('normal')


def random_walk(steps):
    for _ in range(steps):
        tim.color(random.choice(colors))
        random.choice([tim.left(random.choice([90, 180])),
                      tim.right(random.choice([90, 180]))])
        tim.forward(30)


# def random_walk(steps):
#     for step in range(steps):
#         tim.color(random.choice(colors))
#         if step % 2 == 0:
#             tim.left(random.choice([90, 180]))
#             tim.forward(30)
#         elif step % 3 == 0:
#             tim.right(random.choice([90, 180]))
#             tim.forward(30)
#         else:
#             random.choice([tim.left(45),
#                           tim.right(45)])
#             tim.forward(30)


random_walk(random.randint(20, 100))

screen.exitonclick()
