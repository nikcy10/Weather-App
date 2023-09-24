from django.shortcuts import render, HttpResponse
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=4502e1534a899932bb25e2f50702efce').read()
        listOfData = json.loads(source)
        data = {
            "city" : city,
            "country_code" : str(listOfData['sys']['country']),
            "temp" : str(listOfData['main']['temp']) + ' °C',
            "humidity" : str(listOfData['main']['humidity']),
            "main" : str(listOfData['weather'][0]['main']), 
            "description" : str(listOfData['weather'][0]['description']).title,
            "icon" : str(listOfData['weather'][0]['icon']),
            "feelslike" : str(listOfData['main']['feels_like']),
        }
        
    else:
        data = {}
    return render(request, 'index.html', data)
def contact(request):
    return HttpResponse("<h1>Hello World!")

def about(request):
    return HttpResponse("<h1>Hello World!")
