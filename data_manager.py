import requests
from pprint import pprint
FLIGHT_DEALS_GET_API = "https://api.sheety.co/fd03cbf60232f190adaead5b6de995a1/flightDeals/sheet1"


class DataManager:

    def __init__(self):
        self.price_data = {}

    def get_data(self):
        response = requests.get(url=FLIGHT_DEALS_GET_API)
        data = response.json()
        self.price_data = data["sheet1"]
        return self.price_data
 #This class is responsible for talking to the Google Sheet.
