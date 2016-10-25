from django.shortcuts import render

from .models import Annonces
from rent_lookup.models import City, Categorie


def annoncespage(request):
    annonces = Annonces.objects.all().order_by("-date")
    cities = list(City.objects.all().order_by("city_name"))
    categories = Categorie.objects.all()
    return render(request, 'annonces/annonces.html', {'annonces': annonces, 'cities': cities, 'categories': categories})
