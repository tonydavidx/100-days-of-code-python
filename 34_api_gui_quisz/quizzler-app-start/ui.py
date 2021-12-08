from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text='Score:', bg=THEME_COLOR, fg='white')

        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125, text='Quizz', width=280, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
        true_image = PhotoImage(file='../quizzler-app-start/images/true.png')
        false_image = PhotoImage(file='../quizzler-app-start/images/false.png')
        self.right_button = Button(
            image=true_image, padx=10, pady=10, command=self.right_button_clicked)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(
            image=false_image, padx=10, pady=10, command=self.wrong_button_clicked)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(
                self.question_text, text=q_text)
            self.canvas.config(bg='white')
        else:
            self.canvas.itemconfig(
                self.question_text, text='You reached the end of the quiz')
            self.canvas.config(bg='white')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def right_button_clicked(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def wrong_button_clicked(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
