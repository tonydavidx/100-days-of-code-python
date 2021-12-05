from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 280)
        self.write(arg=f"{self.l_score}", align='center',
                   font=('Courier', 80, 'bold'))
        self.goto(100, 280)
        self.write(arg=f"{self.r_score}", align='center',
                   font=('Courier', 80, 'bold'))

    def point_left(self):
        self.l_score += 1
        self.update_score()

    def point_right(self):
        self.r_score += 1
        self.update_score()
