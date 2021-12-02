import random
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

TEXT_STYLE = ('Arial', 14, 'normal')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = password_list + \
        [choice(letters) for i in range(randint(8, 10))]

    password_list = password_list + \
        [choice(symbols) for i in range(randint(2, 4))]

    password_list = password_list + \
        [choice(numbers) for i in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    """
    This function saves website,username and passowrd.
    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Opps', 'Please enter all fields')

    else:
        is_okay = messagebox.askokcancel(
            title=f'{website}', message=f"Do you want to save this data?\n website: {website}\n email: {email}\n password: {password}")

        if is_okay:
            with open('data.txt', 'a') as file:
                file.write(f"{website} | {email} | {password}\n")
                print('successfully saved')

            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text='Website', font=TEXT_STYLE)
website_label.grid(row=1, column=0)

website_entry = Entry(font=TEXT_STYLE, width=30)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# Email
email_label = Label(text="Email / Username", font=TEXT_STYLE,)
email_label.grid(row=2, column=0)

email_entry = Entry(font=TEXT_STYLE, width=30)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'tony@gmail.com')

# Password
passowrd_label = Label(text='Password', font=TEXT_STYLE)
passowrd_label.grid(row=3, column=0)

password_entry = Entry(width=21, font=TEXT_STYLE,)
password_entry.grid(row=3, column=1)

generate_button = Button(
    text='Generate', font=TEXT_STYLE, command=generate_password)
generate_button.grid(row=3, column=2)


# Add button

add_button = Button(text='Add', font=TEXT_STYLE, width=30, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
