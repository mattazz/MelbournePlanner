from dotenv import load_dotenv  # using .env files
import os  # Accessing files

import weatherapi

load_dotenv()  # checks for a .env file
weather_api_key = os.getenv("WEATHER_API")

# weather config
configuration = weatherapi.Configuration()
configuration.api_key = weather_api_key  # sets the api key

# http://api.weatherapi.com/v1/current.json?key=b49b00d1b6e24ae9875152543242409&q=Melbourne&aqi=no

# api_url = "http://api.weatherapi.com/v1/current.json"
location = "Melbourne"
# aqi = "no"

# full_call = f"{api_url}?key={weather_api_key}&q={location}&aqi={aqi}"


api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))
q = location
dt = "2024-11-26"


def get_weather_on_date():
    return
