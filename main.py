# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
ORIGIN_CITY_IATA = "LOS"
today = datetime.now()
tomorrow = today + timedelta(days=1)
six_months = tomorrow + timedelta(days=180)
flight_search = FlightSearch()
data_manager = DataManager()
sheety_data = data_manager.get_data()
if sheety_data[0]["iataCode"] == "":
        for data in sheety_data:
                data["iataCode"] = flight_search.get_destination_code(data["city"])
        data_manager.price_data = sheety_data
        data_manager.update_data()
for data in sheety_data:
        flight = flight_search.get_data(
                city_code=ORIGIN_CITY_IATA,
                destination_city_iatacode=data["iataCode"],
                from_time=tomorrow,
                to_time=six_months
        )