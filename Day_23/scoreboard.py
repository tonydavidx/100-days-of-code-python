from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.score = 1
        self.goto(-220, 260)
        self.create_score()

    def create_score(self):
        self.write(arg=f"Level: {self.score}", align='center', font=FONT,)

    def update_score(self):
        self.score += 1
        self.clear()
        self.create_score()

    def game_over_text(self):
        self.goto(0, 0)
        self.write(arg='Game Over', align='center',
                   font=("Courier", 36, "bold"))
