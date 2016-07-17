from django.http import HttpResponse
# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.views import generic

from .models import Residence, City, Department, Ecole, Logement, Categorie

class ResidenceBag(object):

    residence = None
    ecoles = []
    logements = []
    images = []

def department(request, department_id):
    #all_department = Department.objects.all()
    #return render(request,'rent_lookup/globalize.html',{'all_department': all_department})
    cities = City.objects.filter(departement=department_id)
    categories = Categorie.objects.all()
    return render(request,'rent_lookup/department.html', {'cities': cities, 'categories': categories})


def city(request, department_id, city_id):
    residences = Residence.objects.filter(city=city_id)
    categories = Categorie.objects.all()
    return render(request,'rent_lookup/city.html', {'residences': residences, 'categories': categories})


def details(request, department_id, city_id, residence_id):
    residence = Residence.objects.get(pk=residence_id)
    categories = Categorie.objects.all()
    return render(request,'rent_lookup/details.html',{'residence': residence, 'categories': categories})


def globalize(request):
    all_department = Department.objects.all().order_by('departement_name')
    categories = Categorie.objects.all()
    return render(request,'rent_lookup/globalize.html',{'all_department': all_department, 'categories': categories})
