import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv(".env")  # Gets the environment variables file

# Open Weather API
API_KEY = os.getenv("OWM_API_KEY")
latitude = float(os.getenv('latitude'))
longitude = float(os.getenv('longitude'))
parameters = {
    "appid": API_KEY,
    'lat': latitude,
    'lon': longitude,
    'exclude': 'current,minutely,daily',
    'units': 'metric'
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

hourly_data = weather_data['hourly'][:12]

rain = False

for hour in hourly_data:
    if hour['weather'][0]['id'] < 700:
        rain = True

# Twilio
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
mobile_number = os.environ.get('mobile_number')

if rain:  # Send an SMS message
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body="It's going to rain today! ⛈",
            from_='+15182865347',
            to=mobile_number
        )
