import requests
from flight_data import FlightData


API = "https://api.tequila.kiwi.com"
API_KEY = "CGznDPwXp3yP-kpKASk6jDZnFbOTJZki"


class FlightSearch:
    def __init__(self):
        self.IATACODE = ""

    def get_destination_code(self, city):
        params = {
            "term": city
        }
        headers = {
            "apikey": API_KEY}
        data = requests.get(url=f"{API}/query", headers=headers, params=params)
        self.IATACODE = data.json()["locations"][0]['code']
        return self.IATACODE


# This class is responsible for talking to the Flight Search API.
    def get_data(self,
                 city_code, destination_city_iatacode,
                 from_time, to_time):
        params = {
            "fly_from": city_code,
            "fly_to": destination_city_iatacode,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "one_for_city": 1,
            "max_stopovers": 0,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28
        }
        headers = {
            "apikey": API_KEY
        }

        response = requests.get(url=f"{API}/v2/search", headers=headers, params=params)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"no flights found for {destination_city_iatacode}")
            return None
        flight_data = FlightData(
            origin_city=data['cityFrom'],
            destination_city=data['cityTo'],
            destination_airport=data["flyTo"],
            origin_airport=data["flyFrom"],
            price=data['price'],
            out_date=data["local_departure"].split("T")[0],
            return_date=data["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
