import requests
from pprint import pprint

SHEETY_API_GET = "https://api.sheety.co/1e529c46a7318b8178174ba7764a6062/flightDealsByHari/prices"
SHEETY_API_POST = "https://api.sheety.co/1e529c46a7318b8178174ba7764a6062/flightDealsByHari/prices"


response = requests.get(url=SHEETY_API_GET)
response.raise_for_status()
sheet_data = response.json()
print(sheet_data)