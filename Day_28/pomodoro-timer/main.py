from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = '✔️'
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(10)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(3)
        title.config(text="Break", fg=PINK)
    else:
        count_down(5)
        title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    count_minutes = math.floor(count/60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'

    canvas.itemconfig(count_down_text, text=f'{count_minutes}:{count_seconds}')
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_string = ''
        for _ in range(math.floor(reps/2)):
            check_string += '✔️'
            check_mark.config(text=check_string)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=60, bg=YELLOW)
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='./tomato.png')
canvas.create_image(100, 111, image=tomato_image, )
count_down_text = canvas.create_text(100, 130, text='00:00', fill='white',
                                     font=('Lato', '30', 'bold'),)
canvas.grid(row=1, column=1)

title = Label(text='Timer', fg=GREEN, font=(
    'Courier', 30, 'bold'), bg=YELLOW)
title.grid(row=0, column=1)

start_button = Button(text='Start', width=10, font=(
    'Lato', '12', 'bold'), command=start_timer,)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', width=10, font=('Lato', '12', 'bold'))
reset_button.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW,
                   font=('Courier', 14, 'bold'),)
check_mark.grid(row=3, column=1)


window.mainloop()
