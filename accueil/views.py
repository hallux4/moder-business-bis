from django.shortcuts import render

from .models import Banniere
from rent_lookup.models import City

def accueilpage(request):
    banniere = Banniere.objects.filter()[:1].get()
    cities = list(City.objects.all().order_by("city_name"))
    return render(request, 'accueil/accueil.html', {'banniere': banniere, 'cities': cities})

