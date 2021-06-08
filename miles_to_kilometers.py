from tkinter import *


def convert():
    miles = float(input_box.get())
    km = miles * 1.609
    answer.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

# Entry

input_box = Entry(width=8)
input_box.grid(column=1, row=0)

# Labels

Label(text="miles", font=("Segoe UI", 20, "normal")).grid(column=2, row=0)
Label(text="is equal to", font=("Segoe UI", 20, "normal")).grid(column=0, row=1)
Label(text="kilometers", font=("Segoe UI", 20, "normal")).grid(column=2, row=1)
answer = Label(text="0", font=("Segoe UI", 20, "normal"))
answer.grid(column=1, row=1)

# Button

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
