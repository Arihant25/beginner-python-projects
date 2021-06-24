# Adds new users' details to the database
import requests
import os
from dotenv import load_dotenv

load_dotenv("../.env")

USERS_PUT_ENDPOINT = "https://api.sheety.co/47fa3e5c564ccef88d4272e69984a527/flightDealsFinder/users"
AUTH_TOKEN = os.getenv("flight_club_auth")
headers = {"Authorization": AUTH_TOKEN}

print("Welcome to Arihant's Flight Club!")
print("We find the best flight deals and email you.")

fname = input("What is your first name?\n")
lname = input("What is your last name?\n")
email = input("Please enter your email:\n")
email_again = input("Confirm your email by entering it one more time:\n")

while email != email_again:
    print("Your emails didn't match.")
    email = input("Please enter your email:\n")
    email_again = input("Confirm your email by entering it one more time:\n")

params = {"user": {
    "firstName": fname,
    "lastName": lname,
    "email": email
}}

response = requests.post(url=USERS_PUT_ENDPOINT, headers=headers, params=params)
response.raise_for_status()
