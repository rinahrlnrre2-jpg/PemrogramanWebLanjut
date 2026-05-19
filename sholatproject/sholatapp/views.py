import requests
from django.shortcuts import render

def jadwal_sholat(request):
    url = "https://api.aladhan.com/v1/timingsByCity?city=Samarinda&country=Indonesia&method=8"

    data = requests.get(url).json()
    timings = data['data']['timings']

    context = {
        'subuh': timings['Fajr'],
        'dzuhur': timings['Dhuhr'],
        'ashar': timings['Asr'],
        'maghrib': timings['Maghrib'],
        'isya': timings['Isha'],
    }

    return render(request, 'jadwal.html', context)