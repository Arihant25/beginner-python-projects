from tkinter import *
from tkinter import messagebox
import random

# Change this to your own email so that it's prefilled every time
EMAIL = "johndoe@example.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Generates a random password"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Use these to control the length of the password
    NR_LETTERS = random.randint(8, 10)
    NR_SYMBOLS = random.randint(2, 4)
    NR_SYMBOLS = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(NR_LETTERS)]
    password_list += [random.choice(symbols) for _ in range(NR_SYMBOLS)]
    password_list += [random.choice(numbers) for _ in range(NR_SYMBOLS)]

    random.shuffle(password_list)

    password = ''.join(password_list)

    # Clears the previous password and adds the new one
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # Copies the new password
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Confirms and saves the entry, and clears the fields"""

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!")

    else:
        proceed = messagebox.askyesno(title="Confirm Entry",
                                      message=f"These are the details:\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nDo you want to save?")

        if proceed:
            # Save the entry to a file
            with open('data.txt', mode="a") as file:
                file.write(
                    f"{website} | {email} | {password}\n")

            # Clears the entries upon save
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('MyPass Password Manager')
window.config(padx=30, pady=30)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

Label(text='Website:').grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

Label(text="Email/Username:").grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, EMAIL)

Label(text="Password:").grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

Button(text="Generate Password", command=generate_password).grid(column=2, row=3)

Button(text="Add", width=36, command=save).grid(column=1, row=4, columnspan=2)


window.mainloop()
