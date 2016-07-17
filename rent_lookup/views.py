from django.http import HttpResponse
# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.views import generic

from .models import Residence, City, Department, Ecole, Logement

class ResidenceBag(object):

    residence = None
    ecoles = []
    logements = []
    images = []

def department(request, department_id):
    cities = City.objects.filter(departement=department_id)
    return render(request,'rent_lookup/department.html',{'cities': cities})


def city(request, department_id, city_id):
    residences = Residence.objects.filter(city=city_id)
    return render(request,'rent_lookup/city.html',{'residences': residences})


def details(request, department_id, city_id, residence_id):
    residence = Residence.objects.get(pk=residence_id)
    city = residence.city
    department = city.departement
    ecoles = residence.ecole_set.all()
    logements = residence.logement_set.all()
    images = residence.image_set.all()
    residencelist = {
            'residence': residence,
            'ecoles': ecoles,
            'logements': logements,
            "images": images,
            'city': city,
            'department': department}
    return render(request,'rent_lookup/details.html',{'residencelist': residencelist})


def globalize(request):
    all_department = Department.objects.all()
    return render(request,'rent_lookup/globalize.html',{'all_department': all_department})
