import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWN_API_KEY")

MY_LAT =  33.7490
MY_LONG =  84.3880
OW_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast?"
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "units": "imperial",
    "cnt": 4,
}

response = requests.get(OW_ENDPOINT, params = parameters)
response.raise_for_status()
data = response.json()
print(data)

http_code = data["cod"]
print(http_code)

weather_list = data["list"]
time_cnt = data["cnt"]

for num in range(4):
    weather_item = weather_list[num]
    weather_dt = weather_item["dt"]
    weather_dt_txt = weather_item["dt_txt"]
    weather_id = int(weather_item["weather"][0]["id"])
    weather_desc = weather_item["weather"][0]["description"]
    if weather_id < 700:
        print(f"{weather_dt_txt} - Bring an umbrella")
