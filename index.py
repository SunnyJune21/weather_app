import requests
import pytz
from geopy.geocoders import Nominatim
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from timezonefinder import TimezoneFinder
from datetime import datetime
from services.weatherService import getWeather


def onClick():
    city = textfield.get()
    print(city)
    weather = getWeather(city)
    country = weather['country']
    root.title(f"Weather in {city}, {country}")
    # currentTime = getLocalTime(city)
    print(weather)
    display_city_name(city, country)
    display_statistics(weather)


def display_city_name(city, country):
    capitalized_city = city.capitalize()
    city_label.config(text=f"The weather in {capitalized_city}, {country}")


def display_statistics(weather):
    temp.config(
        text=f"Temperature: {weather['temp']} °C  |  {weather['conditions']}", font=("Poppies", 32))
    feels_like_temp.config(
        text=f"Feels like: {weather['feels_like_temp']} °C")
    conditions.config(text=f"{weather['conditions']}")
    description.config(text=f"{weather['description']}")
    pressure.config(text=f"{weather['pressure']} hPa")
    humidity.config(text=f"{weather['humidity']}%")
    wind.config(text=f"{weather['wind']} m/sec")
    sunrise.config(text=f"Sunrise is at {weather['sunrise']}")
    sunset.config(text=f"Sunset is at {weather['sunset']}")


# creating a window for the app
root = Tk()  # the actual window
root.geometry("900x500+300+200")  # resizing the window
root.title(f"Weather")  # title of the window

# creating a search box, using tkinter and its' PhotoImage
# search_img = tk.PhotoImage(file = "./images/search.png")
myimage = Label(height=20, width=100)
myimage.place(x=20, y=20)

# creating a textfield in the search box image
textfield = tk.Entry(root, justify="center", width=20, font=(
    "Helvetica", 25, "bold"), fg="black", background="white", border=0)
textfield.place(x=100, y=65)
textfield.focus()

myimage_icon = Button(text="Search", height=2, borderwidth=0,
                      cursor="hand", bg="#404040", command=onClick)
myimage_icon.place(x=400, y=64)

original_logo = Image.open("./images/logo.png")
resized_logo = original_logo.resize((250, 250))
logo_image = ImageTk.PhotoImage(resized_logo)
logo = tk.Label(image=logo_image)
logo.place(x=100, y=150)

# name = Label(root, font=("arial", 15, "bold"))
# name.place(x=30, y=100)
# clock = Label(root, font=("Helvetica", 20))
# clock.place(x=30, y=130)

# clock.config(text=currentTime)
# name.config(text="CURRENT WEATHER")
# name.place(x=450, y=120)

label1 = Label(root, text='WIND', font=('Helvetica', 15, 'bold'), fg='white')
label1.place(x=120, y=400)

label2 = Label(root, text='HUMIDITY', font=(
    'Helvetica', 15, 'bold'), fg='white')
label2.place(x=250, y=400)

label3 = Label(root, text='DESCRIPTION', font=(
    'Helvetica', 15, 'bold'), fg='white')
label3.place(x=430, y=400)

label4 = Label(root, text='PRESSURE', font=(
    'Helvetica', 15, 'bold'), fg='white')
label4.place(x=650, y=400)

city_label = Label(root, font=("Helvetica", 28))
city_label.pack(side='top')

feels_like_temp = Label(root, font=("Helvetica", 24))
feels_like_temp.place(x=500, y=200)

temp = Label(font=("poppies", 20, "bold"))
temp.place(x=500, y=150)
conditions = Label(font=("Helvetica", 32, "bold"))

wind = Label(text="...", font=("arial", 20, "bold"), fg='white')
wind.place(x=100, y=430)
humidity = Label(text="...", font=("arial", 20, "bold"), fg='white')
humidity.place(x=250, y=430)
description = Label(text="...", font=("arial", 20, "bold"), fg='white')
description.place(x=430, y=430)
pressure = Label(text="...", font=("arial", 20, "bold"), fg='white')
pressure.place(x=650, y=430)

sunrise = Label(root, font=("Helvetica", 16), fg='white')
sunrise.place(x=500, y=300)
sunset = Label(root, font=("Helvetica", 16), fg='white')
sunset.place(x=500, y=330)

mainloop()  # keeps the window up on the screen
