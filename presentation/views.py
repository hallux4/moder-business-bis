from django.shortcuts import render

from .models import Presentation
from rent_lookup.models import City


def presentationpage(request):
    presentation = Presentation.objects.filter()[:1].get()
    cities = list(City.objects.all().order_by("city_name"))
    return render(request, 'presentation/presentation.html', {'presentation': presentation, 'cities': cities})
