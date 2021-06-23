# This class is responsible for talking to the Flight Search API.
import os
import requests
from dotenv import load_dotenv

load_dotenv("../.env")
API_KEY = os.getenv("KIWI_API_KEY")
KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
HEADERS = {"apikey": API_KEY}


class FlightSearch:
    def iata_search(self, city):
        location_endpoint = f"{KIWI_ENDPOINT}/locations/query"

        params = {"term": city, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=HEADERS, params=params)
        response.raise_for_status()
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search(self, fly_from, date_from, date_to, nights_in_dst_from,
               nights_in_dst_to, flight_type, max_stopovers, fly_to, curr):
        search_endpoint = f"{KIWI_ENDPOINT}/v2/search"
        params = {
            "fly_from": fly_from,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dst_to,
            "flight_type": flight_type,
            "max_stopovers": max_stopovers,
            "fly_to": fly_to,
            "curr": curr
        }
        response = requests.get(url=search_endpoint, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()["data"][0]
