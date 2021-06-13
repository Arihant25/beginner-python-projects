import smtplib
import datetime as dt
import random

# Change these to your own email and password
MY_EMAIL = "youremail@youremailprovider.com"
MY_PASSWORD = "yourPassword"
RECEIVERS_EMAIL = "theiremail@theiremailprovider.com"
now = dt.datetime.now()

# Check if today is a Monday
if now.weekday() == 0:

    with open('quotes.txt') as quotes:
        # Get all quotes
        quotes_list = quotes.readlines()
        # Choose a random quote
        random_quote = random.choice(quotes_list)
        # Send an email with the quote
        with smtplib.SMTP("smtp.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVERS_EMAIL,
                                msg=f"Subject: Today's Quote!\n\n{random_quote}")
