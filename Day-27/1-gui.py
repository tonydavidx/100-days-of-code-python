import tkinter

window = tkinter.Tk()

window.title('My Python Gui')
window.minsize(width=900, height=800)

my_label = tkinter.Label(text='Hello World!', font=('Poppins', 26, 'bold'))
my_label.grid(row=1, column=1)

# buttons

new_button = tkinter.Button(text='New Button')
new_button.grid(row=1, column=3)


def on_click():
    new_text = my_input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text='Click Me', command=on_click)
button.grid(row=2, column=2)

# inputs

my_input = tkinter.Entry()
my_input.config(width=20)
my_input.grid(row=3, column=4)
window.mainloop()
