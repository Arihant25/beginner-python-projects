from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ------------------------------------------ Show Cards -----------------------------------------

try:
    original_data = pandas.read_csv('data/words_to_learn.csv').to_dict(orient="records")
except FileNotFoundError:
    new_data = pandas.read_csv('data/french_words.csv').to_dict(orient="records")
    to_learn = new_data
else:
    to_learn = original_data


def next_card():
    global current_card, flip_timer
    # Cancels existing flip_timer
    window.after_cancel(flip_timer)
    # Chooses a random card
    current_card = choice(to_learn)
    # Displays the card on the screen
    canvas.itemconfig(language, text='French', fill="black")
    canvas.itemconfig(word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    # Starts flip_timer for new card
    flip_timer = window.after(3000, flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------------------------------------------ Flip Cards -----------------------------------------


def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back)


# ------------------------------------------UI Setup---------------------------------------------

window = Tk()
window.title("Flashy - Learn French!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Starts a flip timer
flip_timer = window.after(3000, func=flip_card)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_background = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), fill="black")

canvas.grid(column=0, row=0, columnspan=2)

cross = PhotoImage(file="images/wrong.png")
check = PhotoImage(file="images/right.png")

Button(image=cross, command=next_card, highlightthickness=0).grid(column=0, row=1)
Button(image=check, command=is_known, highlightthickness=0).grid(column=1, row=1)

# Shows the first card
next_card()

window.mainloop()
