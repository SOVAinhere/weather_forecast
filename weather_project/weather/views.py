import requests
from django.shortcuts import render


def home(request):
    city = request.GET.get('city')
    weather_data = None

    if city:
        # 1. Геокодинг: получаем координаты
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru&format=json"
        geo_response = requests.get(geo_url).json()

        if geo_response.get("results"):
            lat = geo_response["results"][0]["latitude"]
            lon = geo_response["results"][0]["longitude"]
            name = geo_response["results"][0]["name"]

            # 2. Погода
            weather_url = (
                f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
                f"&current_weather=true"
            )
            weather_response = requests.get(weather_url).json()
            weather_data = {
                "city": name,
                "temperature": weather_response["current_weather"]["temperature"],
                "windspeed": weather_response["current_weather"]["windspeed"]
            }

            # сохраняем город в сессию для следующих шагов
            request.session["last_city"] = name

    return render(request, "weather.html", {"weather": weather_data})
