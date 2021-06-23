# This class is responsible for talking to the Google Sheet.
import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env")
SHEETY_GET_ENDPOINT = "https://api.sheety.co/47fa3e5c564ccef88d4272e69984a527/flightDealsFinder/prices"
SHEETY_PUT_ENDPOINT = "https://api.sheety.co/47fa3e5c564ccef88d4272e69984a527/flightDealsFinder/prices"


class DataManager:
    def __init__(self):
        response = requests.get(SHEETY_GET_ENDPOINT)
        response.raise_for_status()
        self.prices = response.json()["prices"]

    def update_sheet(self, row_id, params):
        response = requests.put(url=f"{SHEETY_PUT_ENDPOINT}/{row_id}", json=params)
        response.raise_for_status()
