import pandas
import smtplib
import datetime as dt
import random

# Enter the number of letter templates in the folder
LETTER_TEMPLATES = 3

# Enter your email, password and SMTP Server
EMAIL = "example@outlook.com"
PASSWORD = "password0"
SMTP_SERVER = "smtp.office365.com"

now = dt.datetime.now()
today = (now.month, now.day)

# Read the CSV file containing everyone's birthdays
birthdays = pandas.read_csv('birthdays.csv')

# Convert it to a dictionary
birthdays_dict = {(row['month'], row['day']): row for (index, row) in birthdays.iterrows()}

# Check if today matches a birthday in birthdays.csv
if today in birthdays_dict:
    # Pick a random letter from letter templates
    letter_number = random.randint(1, LETTER_TEMPLATES - 1)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter:
        # Write the receiver's name in the template
        letter = letter.read().replace('[NAME]', birthdays_dict[today]['name'])
        # Send an email
        with smtplib.SMTP(host=SMTP_SERVER, port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=birthdays_dict[today]['email'],
                                msg=f"Subject:Happy Birthday!\n\n{letter}")
