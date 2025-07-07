import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Environment variables
OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.environ.get("MY_PHONE_NUMBER")

parameters = {
    "appid" : OPENWEATHER_API_KEY,
    "lat" : 47.376888,
    "lon" : 8.541694,
    "cnt" : 5,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
data = response.json()

will_rain = False
dt = None

for item in data["list"]:
    weather_id = item["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
        dt = item["dt_txt"]
        break

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body =f"It's going to rain today at {dt}. Remember to bring an ☔",
        from_= TWILIO_PHONE_NUMBER,
        to = MY_PHONE_NUMBER
    )
    print(message.status)