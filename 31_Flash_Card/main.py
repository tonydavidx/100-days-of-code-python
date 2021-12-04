from tkinter import *
from tkinter import font

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

window.title('Flashy')

card_front_image = PhotoImage(file='./images/card_front.png')
card_back_image = PhotoImage(file='./images/card_back.png')
canvas = Canvas(height=526, width=800,
                background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 100, text='Title', font=('Arial', 30, 'italic'))
canvas.create_text(400, 263, text='Word', font=('Arial', 50, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='./images/wrong.png')
tick_image = PhotoImage(file='./images/right.png')

unknow_button = Button(image=cross_image, highlightthickness=0)
unknow_button.grid(row=1, column=0)

know_button = Button(image=tick_image, highlightthickness=0)
know_button.grid(row=1, column=1)

window.mainloop()
