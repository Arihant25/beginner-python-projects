# This class is responsible for talking to the Google Sheet.
import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env")
SHEETY_GET_ENDPOINT = "https://api.sheety.co/47fa3e5c564ccef88d4272e69984a527/flightDealsFinder/prices"
SHEETY_PUT_ENDPOINT = "https://api.sheety.co/47fa3e5c564ccef88d4272e69984a527/flightDealsFinder/prices"
USERS_GET_ENDPOINT = "https://api.sheety.co/47fa3e5c564ccef88d4272e69984a527/flightDealsFinder/users"
AUTH_TOKEN = os.getenv("flight_club_auth")
headers = {"Authorization": AUTH_TOKEN}


class DataManager:
    def __init__(self):
        response = requests.get(SHEETY_GET_ENDPOINT, headers=headers)
        response.raise_for_status()
        self.prices = response.json()["prices"]
        response = requests.get(url=USERS_GET_ENDPOINT, headers=headers)
        response.raise_for_status()
        self.users = response.json()["users"]

    def update_sheet(self, row_id, params):
        response = requests.put(url=f"{SHEETY_PUT_ENDPOINT}/{row_id}", json=params, headers=headers)
        response.raise_for_status()
