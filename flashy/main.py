from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy - Learn French!")
window.minsize(width=500, height=500)
window.config(bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526)
canvas.create_image(0, 0, image=card_front)
canvas.create_text(400, 150, text="French")
canvas.create_text(400, 263, text="trouve")


language = Label(text="French")
Label.grid(column=)
word = Label(text="trouve")


window.mainloop()
