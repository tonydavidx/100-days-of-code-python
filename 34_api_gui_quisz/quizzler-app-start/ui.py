from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250)

        self.window.mainloop()
