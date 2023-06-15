import requests

api_key = "fe397cb63ba2f5bf16a59b217e102af0"

def getWeather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url).json() #this is to access all individual attributes

    temp = response['main']['temp']
    temp = round(temp - 273.15) #convert to C and round the temp

    feels_like_temp = response['main']['feels_like']
    feels_like_temp = round(feels_like_temp - 273.15) #convert to C and round the temp

    conditions = response['weather'][0]['main']
    description = response['weather'][0]['description']
    pressure = response['main']['pressure']
    humidity = response['main']['humidity']
    wind = response['wind']['speed']

    #temp.config(text=f"{temp}°")
    #conditions.config(text=(conditions, "|", "FEELS", "LIKE", temp, "°"))

    return {
        'temp':temp,
        'feels_like_temp': feels_like_temp,
        'conditions': conditions,
        'description': description,
        'pressure': pressure,
        'humidity': humidity,
        'wind': wind
    }
