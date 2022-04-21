import requests
from twilio.rest import Client

# kootanad geo location
LAT = 10.761591
LON = 76.120890

account_sid = "user account sid"
auth_token = "user auth tocken"

# bacalod city lat, lon
# LAT = 10.684005
# LON = 122.956299

WEATHER_API = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_ONECALL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "user api key"

params = {
    'lat': LAT,
    'lon': LON,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily',
}

response = requests.get(url=WEATHER_ONECALL, params=params)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data['hourly'][:12]
weather_id = []
for hour_data in weather_slice:
    weather_id.append(hour_data["weather"][0]['id'])

will_rain = False

for i in range(len(weather_id)):
    if weather_id[i] < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella with you,since it's a rainy day",
        from_='PHONE NUMBER',
        to='PHONE NUMBER'
    )
    print(message.status)
