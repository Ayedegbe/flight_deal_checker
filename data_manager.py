import requests
FLIGHT_DEALS_GET_API = ""
FLIGHT_DEALS_PUT_API = ""


class DataManager:

    def __init__(self):
        self.price_data = {}

    def get_data(self):
        response = requests.get(url=FLIGHT_DEALS_GET_API)
        data = response.json()
        self.price_data = data["sheet1"]
        return self.price_data
# This class is responsible for talking to the Google Sheet.

    def update_data(self):
        for city in self.price_data:
            new_data = {
                "sheet1": {
                    'iataCode': city["iataCode"]
                }
            }
            response = requests.put(url=f"{FLIGHT_DEALS_GET_API}/{city['id']}", json=new_data)
            print(response.text)
