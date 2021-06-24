from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

sheet_data = data_manager.prices

SHEETY_PUT_ENDPOINT = "https://api.sheety.co/47fa3e5c564ccef88d4272e69984a527/flightDealsFinder/prices"

for row in sheet_data:
    city = row["city"]
    current_price = row["lowestPrice (inRupees)"]
    iataCode = row["iataCode"]
    row_id = row["id"]

    # Fill the IATA codes column
    if iataCode == "":
        iataCode = flight_search.iata_search(city)
        data_manager.update_sheet(row_id=row_id, params={"price": {"iataCode": iataCode}})

    # Search for the latest price
    search_results = flight_search.search(flight_data.fly_from, flight_data.date_from, flight_data.date_to,
                                          flight_data.nights_in_dst_from, flight_data.nights_in_dst_to,
                                          flight_data.flight_type, flight_data.max_stopovers, iataCode,
                                          flight_data.curr)
    try:
        new_price = search_results["price"]
        fly_from = search_results["route"][0]["cityFrom"]
        fly_to = search_results["route"][0]["cityTo"]
        departure_iata = search_results["route"][0]["flyFrom"]
        arrival_iata = search_results["route"][0]["flyTo"]
        departure_date = search_results["route"][0]["local_departure"].split("T")[0]
        arrival_date = search_results["route"][0]["local_arrival"].split("T")[0]
    except TypeError:
        # If the data returned is None
        continue
    else:
        # Update the lowest price column and send an email
        if new_price < current_price:
            data_manager.update_sheet(row_id=row_id, params={"price": {"lowestPrice (inRupees)": new_price}})
            for user_row in data_manager.users:
                email = user_row["email"]
                notification_manager.send_email(price=new_price, fly_from=fly_from, fly_to=fly_to,
                                                departure_iata=departure_iata, arrival_iata=arrival_iata,
                                                departure_date=departure_date, arrival_date=arrival_date,
                                                to_addrs=email)
