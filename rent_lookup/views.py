from django.shortcuts import render

# from .models import Residence, City, Department, Ecole, Logement, Categorie
from .models import Residence, City, Categorie

def city(request):
    cities = list(City.objects.all().order_by("city_name"))
    categories = Categorie.objects.all()
    return render(request,'rent_lookup/department.html', {'cities': cities, 'categories': categories})


def details(request, residence_id):
    residence = Residence.objects.get(pk=residence_id)
    categories = Categorie.objects.all()
    return render(request,'rent_lookup/details.html',{'residence': residence, 'categories': categories})

