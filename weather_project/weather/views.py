import requests
from django.shortcuts import render


def home(request):
    city = request.GET.get('city')
    weather_data = None

    if city:
        geo_url = (
            f"https://geocoding-api.open-meteo.com/v1/search"
            f"?name={city}&count=1&language=ru&format=json"
        )
        geo_response = requests.get(geo_url).json()

        results = geo_response.get("results")
        if results:
            lat = results[0]["latitude"]
            lon = results[0]["longitude"]
            name = results[0]["name"]

            weather_url = (
                f"https://api.open-meteo.com/v1/forecast"
                f"?latitude={lat}&longitude={lon}&current_weather=true"
            )
            weather_response = requests.get(weather_url).json()

            weather_data = {
                "city": name,
                "temperature": weather_response["current_weather"]["temperature"],
                "windspeed": weather_response["current_weather"]["windspeed"],
            }
        else:
            weather_data = {"error": "Город не найден"}

    return render(request, "weather.html", {"weather": weather_data, "city": city})
