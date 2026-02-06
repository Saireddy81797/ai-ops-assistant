import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_current_weather(city: str):
    # If API key missing, return mock data
    if not WEATHER_API_KEY:
        return {
            "city": city,
            "temperature": "28°C",
            "condition": "clear sky (mock data)",
            "humidity": "60%"
        }

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(WEATHER_API_URL, params=params)

    if response.status_code != 200:
        # Fallback instead of crash
        return {
            "city": city,
            "temperature": "28°C",
            "condition": "partly cloudy (fallback)",
            "humidity": "65%"
        }

    data = response.json()

    return {
        "city": city,
        "temperature": f"{data['main']['temp']}°C",
        "condition": data["weather"][0]["description"],
        "humidity": f"{data['main']['humidity']}%"
    }
