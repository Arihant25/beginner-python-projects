import os
import smtplib
from bs4 import BeautifulSoup
import requests
from time import sleep
from dotenv import load_dotenv

# Get the product URL
url = input("Enter the URL of the product you wish to track:\n")
headers = {"Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
           "User-Agent": "Defined"}
html = requests.get(url, headers=headers)

# Create a BeautifulSoup object with the html data
soup = BeautifulSoup(html.text, "html.parser")


def get_price():
    """Get the price from the html"""
    price = soup.find("span", id="priceblock_ourprice").text
    print("The current price of the product is: " + price)
    price_float = float(price.replace(",", "").split()[-1])
    return price_float


price_float = get_price()

# Ask the user for the price they want to track and their email address
desired_price = float(input("Enter the price you want to track:"))
email = input("Enter your email address:")
print(
    f"You will be emailed at {email} when the price reaches {desired_price}.")

# Check if the price has dropped below the desired price
while price_float > desired_price:
    price_float = get_price()
    sleep(86400)  # Runs once a day
    print("I'll check for the price once everyday. Keep this program running.")

# Send an email to the user with the current price
print("The price has dropped! Sending email...")
load_dotenv(".env")
my_email = os.getenv("email3")
password = os.getenv("email_password_3")
with smtplib.SMTP("smtp.office365.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email,
                        msg=f"Subject: Price Drop Alert!\n\nHey there, this is your friendly Python bot, here to inform you that your product is finally available cheaper than your desired price ({price_float})! You can buy it from here: {url}")
