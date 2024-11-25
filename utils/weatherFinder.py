from dotenv import load_dotenv  # using .env files
import os  # Accessing files
from pprint import pprint  ## pretty print. Makes prints pretty

import weatherapi
from weatherapi.rest import ApiException

load_dotenv()  # checks for a .env file
weather_api_key = os.getenv("WEATHER_API")

# weather config
configuration = weatherapi.Configuration()
configuration.api_key["key"] = weather_api_key  # sets the api key

# http://api.weatherapi.com/v1/current.json?key=b49b00d1b6e24ae9875152543242409&q=Melbourne&aqi=no

# api_url = "http://api.weatherapi.com/v1/current.json"
location = "Melbourne"
# aqi = "no"

# full_call = f"{api_url}?key={weather_api_key}&q={location}&aqi={aqi}"


api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))
q = location
dt = "2024-11-26"


def get_weather_on_date():
    try:
        api_response = api_instance.forecast_weather(q, dt)
        return api_response
    except ApiException as e:
        print("Exception when calling APIsApi -> Forecast: %s\n" % e)


result = get_weather_on_date()
pprint(result)
