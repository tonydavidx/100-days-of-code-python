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
        self.high_score = self.read_high_score()
        self.display_score()

    def add_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.display_score()
        self.save_high_score()

    def read_high_score(self):
        score_data = 0
        with open('data.txt', 'r') as data:
            score_data = data.read()
            score_data = int(score_data)
            return score_data

    def save_high_score(self):
        with open('data.txt', 'w') as data:
            new_high_score = self.high_score
            new_high_score = str(new_high_score)
            data.write(new_high_score)
