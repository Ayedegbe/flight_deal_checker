import requests

print("Welcome to flight club we help you find the best flight deals")
first_name = "daniel"
last_name = "ayedegbe"
email = "danielayedegbe1@gmail.com"
# email_confirmation = input("type your email again: ")
data = {
    "sheet3": {
        "email": email,
        "Last Name": last_name,
        "First Name": first_name
    }
}
response = requests.post(url="https://api.sheety.co/fd03cbf60232f190adaead5b6de995a1/flightDeals/sheet3", json=data)
print(response.json())
