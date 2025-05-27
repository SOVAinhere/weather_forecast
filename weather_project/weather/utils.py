import requests

def get_weather(city):
    try:
        geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geocode_response = requests.get(geocode_url).json()

        if not geocode_response.get("results"):
            return {"error": "Город не найден"}

        lat = geocode_response["results"][0]["latitude"]
        lon = geocode_response["results"][0]["longitude"]

        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        )
        weather_response = requests.get(weather_url).json()
        return weather_response.get("current_weather", {"error": "Нет данных о погоде"})
    except Exception as e:
        return {"error": str(e)}
