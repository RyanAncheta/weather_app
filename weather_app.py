import requests
import tkinter as tk
from tkinter import messagebox

api_key = 'd50be31ddfeb552eb8bb3161a4300385'

def get_weather(city_name):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name, 'appid': api_key, 'units': 'metric'}

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['cod'] == 200:
        temperature = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        result_label.config(text=f'Temperature in {city_name}: {temperature}°C\nWeather: {weather_desc}')
    else:
        messagebox.showerror("Error", "City not found. Please check the spelling.")

def get_weather_button_clicked():
    city = city_entry.get()
    if city:
        get_weather(city)
    else:
        messagebox.showerror("Error", "Please enter a city name.")


root = tk.Tk()
root.title("Weather App")

window_width = 300
window_height = 400
root.geometry(f"{window_width}x{window_height}")

city_label = tk.Label(root, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_button_clicked)
get_weather_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
