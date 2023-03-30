import tkinter as tk
import requests
from tkinter import messagebox

DEFAULT_FONT = ('Arial', 14, 'bold')
BIG_FONT = ('Arial', 20)
DIGIT_FONT = ('Arial', 24, 'bold')

SEARCH_COLOR = "#ADD8E6"
LIGHT_GRAY = "#F5F5F5"
OFF_WHITE = '#F8FAFF'

class WeatherApp:
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("380x677")
        self.root.resizable(0, 0)
        self.root.title('Weather')

        self.search_frame = self.create_search_frame()
        self.info_frame = self.create_info_frame()

        self.search_label = self.create_search_label()
        self.search = self.create_search()
        self.search_button = self.create_search_button()

        self.city_label, self.weather_label, self.temperature_label, self.windspeed_label = self.create_city_label()

    def create_search_frame(self):
        frame = tk.Frame(self.root, bg=SEARCH_COLOR, height=50)
        frame.place(x=0, y=0)
        return frame

    def create_info_frame(self):
        frame = tk.Frame(self.root, height=577)
        frame.pack(expand=True)
        return frame
    
    def create_search_label(self):
        label = tk.Label(self.search_frame, font=DEFAULT_FONT, text="SEARCH", bg=SEARCH_COLOR)
        label.grid(row=0, columnspan=2, pady=5)

    def create_search(self):
        search_bar = tk.Entry(self.search_frame, font=DEFAULT_FONT, width=25)
        search_bar.grid(row=1, column=0, padx=5)
        return search_bar

    def create_search_button(self):
        button = tk.Button(self.search_frame, font=DEFAULT_FONT, bg=OFF_WHITE, text="Search", borderwidth=0, command=self.update_weather)
        button.grid(row=1, column=1, padx=5, pady=5)

    def create_city_label(self):
        city_label = tk.Label(self.info_frame, font=DEFAULT_FONT)
        city_label.pack()

        weather_label = tk.Label(self.info_frame, font=DEFAULT_FONT)
        weather_label.pack()

        temperature_label = tk.Label(self.info_frame, font=DEFAULT_FONT)
        temperature_label.pack()

        windspeed_label = tk.Label(self.info_frame, font=DEFAULT_FONT)
        windspeed_label.pack()

        return city_label, weather_label, temperature_label, windspeed_label

    def update_weather(self):
        api = "Your API"
        city = self.search.get()
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api}"

        response = requests.get(url).json()
        if len(response) < 1:
            messagebox.showerror(title="Input Error", message="Such city does not exist")
        else:
            lat = response[0]['lat']
            lon = response[0]['lon']

            weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric'

            weather_response = requests.get(weather_url).json()
            weather = weather_response['weather'][0]['main']
            temperature = weather_response['main']['temp']
            windspeed = weather_response['wind']['speed']

            self.city_label.config(text=f"City: {city}")
            self.weather_label.config(text=f"Weather: {weather}")
            self.temperature_label.config(text=f"Temperature: {temperature}°C")
            self.windspeed_label.config(text=f"Wind Speed: {windspeed}m/s")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WeatherApp()
    app.run()