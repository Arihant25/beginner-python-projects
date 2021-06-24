# This class is responsible for sending notifications with the deal flight details.
import smtplib
import os
from dotenv import load_dotenv

# Get environment variables
load_dotenv("../.env")
my_email = os.getenv("email3")
password = os.getenv("email_password_3")


class NotificationManager:
    def send_email(self, price, fly_from, departure_iata, fly_to, arrival_iata, departure_date, arrival_date, to_addrs):
        """Sends an email with the flight details"""
        with smtplib.SMTP("smtp.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            url = f"https://www.google.co.uk/flights?hl=en#flt={departure_iata}.{arrival_iata}.{departure_date}*" \
                  f"{arrival_iata}.{departure_iata}.{arrival_date}"
            msg = f"Subject: New Low Price Flight Alert!\n\nLow price alert! Only Rs. {price} to fly from {fly_from}-" \
                  f"{departure_iata} to {fly_to}-{arrival_iata} from {departure_date} to {arrival_date}.\n{url}"
            connection.sendmail(from_addr=my_email, to_addrs=to_addrs, msg=msg)
