from django.shortcuts import render

from .models import Service
from rent_lookup.models import City


def servicepage(request):
    service = Service.objects.filter()[:1].get()
    cities = list(City.objects.all().order_by("city_name"))
    return render(request, 'service/presentation.html', {'service': service, 'cities': cities})
