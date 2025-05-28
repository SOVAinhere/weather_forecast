import requests
from django.shortcuts import render


def home(request):
    city = request.GET.get("city")
    weather_data = None

    if city:
        geo_data = fetch_geolocation(city)
        if geo_data:
            weather = fetch_weather(*geo_data[:2])  # lat, lon
            if weather:
                weather_data = {
                    "city": geo_data[2],  # name
                    "temperature": weather["temperature"],
                    "windspeed": weather["windspeed"],
                }
            else:
                weather_data = {"error": "Не удалось получить погоду"}
        else:
            weather_data = {"error": "Город не найден"}

    return render(request, "weather.html", {"weather": weather_data, "city": city})


def fetch_geolocation(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "ru", "format": "json"}
    try:
        response = requests.get(url, params=params).json()
        result = response.get("results")
        if result:
            return result[0]["latitude"], result[0]["longitude"], result[0]["name"]
    except Exception:
        pass
    return None


def fetch_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": "true"}
    try:
        response = requests.get(url, params=params).json()
        return response.get("current_weather")
    except Exception:
        return None
