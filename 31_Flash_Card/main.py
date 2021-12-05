from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

next_word = {}
to_learn = {}

try:
    words_to_learn = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')
    to_learn = data.to_dict(orient='records')
else:
    to_learn = words_to_learn.to_dict(orient='records')


def show_answer():
    global next_word
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=next_word['English'], fill='white')


def next_card():
    global next_word, filp_timer
    window.after_cancel(filp_timer)
    next_word = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=next_word['French'], fill='black')
    filp_timer = window.after(3000, show_answer)


def is_known():
    to_learn.remove(next_word)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv('./data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)


window.title('Flashy')

filp_timer = window.after(3000, show_answer)

card_front_image = PhotoImage(file='./images/card_front.png')
card_back_image = PhotoImage(file='./images/card_back.png')
canvas = Canvas(height=526, width=800,
                background=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(
    400, 100, text='Title', font=('Arial', 30, 'italic'))
card_word = canvas.create_text(
    400, 263, text='Word', font=('Arial', 50, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='./images/wrong.png')
tick_image = PhotoImage(file='./images/right.png')

unknow_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknow_button.grid(row=1, column=0)

know_button = Button(image=tick_image, highlightthickness=0, command=is_known)
know_button.grid(row=1, column=1)

next_card()

window.mainloop()
