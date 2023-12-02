from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    a = requests.get('https://v6.exchangerate-api.com/v6/afff1a78fcb6779e4e7b563e/latest/USD')
    aed = a.json()['conversion_rates']['AED']
    uzs = a.json()['conversion_rates']['UZS']
    azn = a.json()['conversion_rates']['AZN']

    context={
        'aed':aed,
        'uzs':uzs,
        'azn':azn,
    }
    return render(request, 'index.html', context)
