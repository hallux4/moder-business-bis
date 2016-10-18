from django.shortcuts import render

# from .models import Residence, City, Department, Ecole, Logement, Categorie
from .models import Residence, City, Categorie

class ResidenceBag(object):

    residence = None
    ecoles = []
    logements = []
    images = []

def city(request):
    cities = list(City.objects.all().order_by("city_name"))
    #cities = City.objects.filter(departement=department_id).order_by("city_name")
    categories = Categorie.objects.all()
    return render(request,'rent_lookup/department.html', {'cities': cities, 'categories': categories})


def residence(request, city_id):
    residences = Residence.objects.filter(city=city_id).order_by("residence_name")
    categories = Categorie.objects.all()
    return render(request,'rent_lookup/city.html', {'residences': residences, 'categories': categories})


def details(request, city_id, residence_id):
    residence = Residence.objects.get(pk=residence_id)
    categories = Categorie.objects.all()
    return render(request,'rent_lookup/details.html',{'residence': residence, 'categories': categories})


#def globalize(request):
#    all_department = list(Department.objects.all().order_by("departement_name"))
#    categories = Categorie.objects.all()
#    return render(request,'rent_lookup/globalize.html',{'all_department': all_department, 'categories': categories})
