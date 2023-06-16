from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz


def getLocalTime(city):
    geolocator = Nominatim(user_agent="anastasia.nosich@gmail.com")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    localTime = datetime.now(home)
    currentTime = localTime.strftime("%d/%m/%y %H:%M")

    return currentTime
