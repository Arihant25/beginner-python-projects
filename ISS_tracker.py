import requests
import smtplib
from time import sleep
from datetime import datetime, timezone

MY_LAT = 20.368090  # Your latitude
MY_LONG = 86.155860  # Your longitude
MY_EMAIL = 'example@outlook.com'  # Your email
MY_PASSWORD = 'example-password'  # Your password
SMTP_SERVER = 'smtp.office365.com'

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def is_close():
    """Check if your position is within +5 or -5 degrees of the ISS position."""
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def is_dark():
    """Check if it's dark"""
    if sunset <= time_now <= sunrise:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# Get only the hours from the time
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(timezone.utc).hour

while True:
    # If the ISS is close to my current position and it is currently dark
    if is_close() and is_dark():
        # Then send me an email to tell me to look up
        with smtplib.SMTP(SMTP_SERVER, port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject: ISS OVERHEAD\n\n"
                                    "Look up, the International Space Station is passing over you!")
    # Run the code every 60 seconds
    sleep(60)
