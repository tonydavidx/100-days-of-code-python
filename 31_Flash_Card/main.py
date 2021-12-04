from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

window.title('Flashy')

card_front_image = PhotoImage(file='./images/card_front.png')
card_back_image = PhotoImage(file='./images/card_back.png')
canvas = Canvas(height=526, width=800)
canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)


window.mainloop()
