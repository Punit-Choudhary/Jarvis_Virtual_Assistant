''' This module returns weather of desired city '''

import requests
import json
import os
from dotenv import load_dotenv

import voice

load_dotenv()

api_key = os.getenv('W_KEY')   # Add your API key here
base_url = "https://api.openweathermap.org/data/2.5/weather?"

city_name = "Kotputli,IN"

complete_url = base_url + "q=" + city_name + "&APPID=" + api_key

def fetch_weather():
    response = requests.get(complete_url)
    resp = response.json()

    if resp['cod'] != '404':
        main = resp["main"]

        current_temp = main["temp"]
        current_pressure = main["pressure"]
        current_humidity = main["humidity"]

        weather = resp["weather"]

        weather_description = weather[0]["description"]

        voice.speak(f"""Today's Weather details for {city_name} are,
                      Weather is {weather_description}, 
                      Temprature is {current_temp} kelvin,
                      {current_pressure} atmospheric pressure
                      and humidity is {current_humidity} percent""")
    else:
        voice.speak(f"I am unable to fetch weather details for {city_name}")
