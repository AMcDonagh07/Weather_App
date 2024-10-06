# Weather App 01/10/2024

import requests

# Replace with your OpenWeatherMap API key
API_KEY = 'Your API Here!'

def get_weather(city):
    # OpenWeatherMap URL for current weather data
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters to pass to the API
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # To get temperature in Celsius (for Fahrenheit, use 'imperial')
    }
    
    # Send the GET request to the API
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()
        
        # Extract and display relevant weather data
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        print(f"Weather in {city}:")
        print(f"Description: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found or invalid API request!")

# Ask the user for the city name
city = input("Enter city name: ")
get_weather(city)
