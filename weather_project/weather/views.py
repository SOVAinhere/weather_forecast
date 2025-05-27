from django.shortcuts import render
from .utils import get_weather

def home(request):
    context = {}
    if "city" in request.GET:
        city = request.GET["city"]
        weather = get_weather(city)
        context = {"city": city, "weather": weather}
    return render(request, "weather/home.html", context)
