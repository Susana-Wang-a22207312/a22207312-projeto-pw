from django.shortcuts import render
import requests

def weather_today(request):
    url_forecast = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    url_weather_types = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    response_forecast = requests.get(url_forecast)
    response_weather_types = requests.get(url_weather_types)

    context = {
        'forecast': response_forecast.json(),
        'weather_types': response_weather_types.json()
    }

    return render(request, 'meteo/index.html', context)


