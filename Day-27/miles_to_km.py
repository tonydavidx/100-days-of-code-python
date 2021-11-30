from tkinter import *

window = Tk()
window.title("Miles to Kilometers converter")
# window.minsize(width=900, height=600)
window.config(padx=20, pady=20)


def convert():
    miles = miles_input.get()
    print(miles)
    km = float(miles) * 1.609
    print(km)
    km_input.delete(0, END)
    km_input.insert(0, km)


miles_input = Entry(width=20)
miles_input.grid(row=0, column=1)

km_input = Entry(width=20)
km_input.grid(row=1, column=1)

label_1 = Label(text="is Equal to")
label_1.grid(row=1, column=0)

label_miles = Label(text='Miles')
label_miles.grid(row=0, column=2)

label_km = Label(text='Kilometers')
label_km.grid(row=1, column=2)

button = Button(text='Convert', command=convert)
button.grid(row=2, column=1)

window.mainloop()
