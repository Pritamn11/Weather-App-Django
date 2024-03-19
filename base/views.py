from django.shortcuts import render
import requests
import datetime
from config import API_KEY
import json


# Create your views here.

def get_weather_info(request):
    data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = API_KEY

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        response = requests.get(url).json()

        
        if response['cod'] == 200:
            data = {
                'city' : city,
                'temperature' : round(response['main']['temp'] - 273.15,2),
                'weather_description' : response['weather'][0]['description'],
                'humidity' : response['main']['humidity'],
                'min_temp' : response['main']['temp_min'],
                'max_temp' : response['main']['temp_max'],
                'wind' : response['wind']['speed'],
                'time' : datetime.datetime.fromtimestamp(response['dt']).strftime("%A, %I:%M %p"),
                'icon' : response['weather'][0]['icon']
            }

        else:
            error = "Please enter a valid city name."
            return render(request, "base/error.html", {'error':error} )

    context = {'data':data}
    return render(request, 'base/index.html', context)


