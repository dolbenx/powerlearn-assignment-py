import tkinter as tk
import requests

# Function to get weather data from OpenWeatherMap API
def get_weather():
    city_name = city_entry.get()
    api_key = "346b50c1b54d3ecdf8591884f0f66ef9"  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather = data['weather'][0]

            # Extract relevant information
            temperature = main['temp']
            weather_description = weather['description']
            pressure = main['pressure']
            humidity = main['humidity']
            weather_condition = weather['main'].lower()

            # Update UI with weather data
            weather_label.config(text=f"Weather in {city_name.capitalize()}:")
            temp_label.config(text=f"Temperature: {temperature}°C")
            description_label.config(text=f"Weather: {weather_description.capitalize()}")
            pressure_label.config(text=f"Pressure: {pressure} hPa")
            humidity_label.config(text=f"Humidity: {humidity}%")
            
            # Add condition-based visuals for rain, snow, or sun
            if "rain" in weather_condition:
                weather_icon.config(text="🌧️ Rainy")
            elif "snow" in weather_condition:
                weather_icon.config(text="❄️ Snowy")
            elif "clear" in weather_condition:
                weather_icon.config(text="☀️ Sunny")
            else:
                weather_icon.config(text="🌥️ Cloudy")
        else:
            error_label.config(text="City not found or invalid API key.")
    except Exception as e:
        error_label.config(text="Error fetching data. Please try again.")

# Create the main window using Tkinter
window = tk.Tk()
window.title("Weather App")
window.geometry("400x350")
window.config(bg="#f0f0f0")

# Create widgets
city_label = tk.Label(window, text="Enter City:", font=("Arial", 14), bg="#f0f0f0")
city_label.pack(pady=10)

city_entry = tk.Entry(window, font=("Arial", 14), width=25)
city_entry.pack(pady=5)

search_button = tk.Button(window, text="Get Weather", font=("Arial", 14), command=get_weather)
search_button.pack(pady=20)

weather_label = tk.Label(window, text="", font=("Arial", 14), bg="#f0f0f0")
weather_label.pack()

temp_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
temp_label.pack()

description_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
description_label.pack()

pressure_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
pressure_label.pack()

humidity_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
humidity_label.pack()

weather_icon = tk.Label(window, text="", font=("Arial", 20), bg="#f0f0f0")
weather_icon.pack(pady=10)

error_label = tk.Label(window, text="", font=("Arial", 12), fg="red", bg="#f0f0f0")
error_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
