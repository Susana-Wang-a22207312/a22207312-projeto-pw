from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.weather_today, name='index'),
]
