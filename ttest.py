import requests
API = "https://api.tequila.kiwi.com"
API_KEY = "CGznDPwXp3yP-kpKASk6jDZnFbOTJZki"

params = {
            "fly_from": "LOS",
            "fly_to": "LON",
            "date_from": "21/09/2022",
            "date_to": "23/10/2022",
            "one_for_city": 1,
            "max_stopovers": 0,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28}
headers = {
    "apikey": API_KEY}


response = requests.get(url=f"{API}/v2/search", headers=headers, params=params)
print(response.json())