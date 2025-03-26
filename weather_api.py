import requests

WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"

def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}"
    response = requests.get(url).json()
    return response["weather"][0]["description"]
