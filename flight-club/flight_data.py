# This class is responsible for structuring the flight data.
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv("../.env")


class FlightData:
    def __init__(self):
        self.fly_from = "BBI"
        tomorrow = date.today() + timedelta(days=1)
        self.date_from = tomorrow.strftime("%d/%m/%Y")
        self.date_to = (tomorrow + 30 * timedelta(days=6)).strftime("%d/%m/%Y")  # 6 months from tomorrow
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28
        self.flight_type = "round"
        self.max_stopovers = 0
        self.curr = "INR"
