import requests
from django.shortcuts import render

API_KEY = "260ccc8107bc73f8c1c977fd9e0eb86e" #делаю через openweathermap

def home(request):
    city = request.GET.get("city")
    weather_data = None

    if city:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "lang": "ru"
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "windspeed": data["wind"]["speed"],
                    "description": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"],
                    "main": data["weather"][0]["main"],
                }
            else:
                weather_data = {"error": f"Ошибка: {data.get('message', 'Неизвестная ошибка')}"}
        except Exception as e:
            weather_data = {"error": "Не удалось получить данные о погоде."}

    return render(request, "weather.html", {"weather": weather_data, "city": city})
