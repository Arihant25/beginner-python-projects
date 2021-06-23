# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Get environment variables
load_dotenv("../.env")
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
mobile_number = os.environ.get('mobile_number')


class NotificationManager:
    def send_sms(self, price, fly_from, departure_iata, fly_to, arrival_iata, departure_date, arrival_date):
        """Sends an SMS message with the flight details"""
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Low price alert! Only {price} to fly from {fly_from}-{departure_iata} to {fly_to}-{arrival_iata} "
                 f"from {departure_date} to {arrival_date}.",
            from_="+15182865347",
            to=mobile_number
        )
