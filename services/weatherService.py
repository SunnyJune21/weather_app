import requests
from datetime import datetime

api_key = "fe397cb63ba2f5bf16a59b217e102af0"


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


def getWeather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # this is to access all individual attributes
    response = requests.get(url).json()

    temp = response['main']['temp']
    temp = round(temp - 273.15)  # convert to C and round the temp

    feels_like_temp = response['main']['feels_like']
    feels_like_temp = round(feels_like_temp - 273.15)

    conditions = response['weather'][0]['main']
    description = response['weather'][0]['description']
    pressure = response['main']['pressure']
    humidity = response['main']['humidity']
    wind = response['wind']['speed']

    sunrise = response['sys']['sunrise']
    sunset = response['sys']['sunset']
    timezone = response['timezone']
    country = response['sys']['country']

    sunriseTime = time_format_for_location(sunrise + timezone)
    sunsetTime = time_format_for_location(sunset + timezone)

    return {
        'temp': temp,
        'feels_like_temp': feels_like_temp,
        'conditions': conditions,
        'description': description,
        'pressure': pressure,
        'humidity': humidity,
        'wind': wind,
        'sunrise': sunriseTime,
        'sunset': sunsetTime,
        'country': country
    }
