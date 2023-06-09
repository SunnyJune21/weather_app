import requests
import pytz
from geopy.geocoders import Nominatim
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox

city_country = "Kharkiv,UA"
api_key = "fe397cb63ba2f5bf16a59b217e102af0"

root = Tk() # the actual window
root.geometry("900x500+300+200")  #resizing the window
root.title(f"Weather in {city_country[:-3]}") #title of the window

#search box
search_img = tk.PhotoImage(file = "./images/logo.png")
myimage=Label(image=search_img)
myimage.place(x=20, y=20)

def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url).json() #this is to access all individual attributes

    temp = response['main']['temp']
    temp = round(temp - 273.15) #convert to C and round the temp

    feels_like_temp = response['main']['feels_like']
    feels_like_temp = round(feels_like_temp - 273.15) #convert to C and round the temp

    return {
        'temp':temp,
        'feels_like_temp': feels_like_temp,
    }


weather = get_weather(api_key, city_country)

print(weather['temp'])
print(weather['feels_like_temp'])

def display_city_name(city):
    city_label = Label(root, text=f"{city_country[:-3]}")
    city_label.config(font=("Helvetica", 28))
    city_label.pack(side='top')

def display_statistics(weather):
    temp = Label(root, text = f"Temperature: {weather['temp']} C")
    feels_like_temp = Label(root, text = f"Feels like: {weather['feels_like_temp']} C")

    temp.config(font=("Helvetica", 22))
    feels_like_temp.config(font=("Helvetica", 18))

    temp.pack(side='top')
    feels_like_temp.pack(side='top')

display_city_name(city_country)
display_statistics(weather)

mainloop() #keeps the window up on the screen

