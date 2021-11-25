from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 370)
        self.score = 0
        self.display_score()

    def add_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}",
                   align=ALIGNMENT, font=FONT)

    def show_game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT,
                   font=("Courier", 35, 'bold'))
