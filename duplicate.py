#!/usr/bin/env python
# coding=utf-8

from rent_lookup.models import *
from copy import deepcopy
from random import randrange
from django.core.files import File

def create_depatment():


    index_departement = 10

    while index_departement > 0:
        departementtxt = "departement %d" % index_departement

        departement = Department(departement_name=departementtxt)
        departement.save()

        index_city = randrange(2, 10)
        while index_city > 0:
            citytxt = "city %d" % index_city
            city = City(city_name=citytxt, departement=departement)
            city.save()
            index_city = index_city - 1

            index_residence = randrange(1, 10)
            while index_residence > 0:
                residencetxt = "residence %d" % index_residence

                residence = deepcopy(Residence.objects.all()[0])
                residence.pk = None
                residence.city = city
                residence.residence_name = residencetxt
                residence.residence_name_zh_hans = "%s cn" % residencetxt
                #residence = Residence(residence_name=residencetxt, description="aaaaaaaa", city=city)
                residence.save()

                ecole = deepcopy(Ecole.objects.all()[0])
                ecole.pk = None
                ecole.residence = residence
                ecole.save()

                logement = deepcopy(Logement.objects.all()[0])
                logement.pk = None
                logement.residence = residence
                logement.save()

                index_residence = index_residence - 1

                index_image = randrange(4, 10)
                while index_image > 0:

                    f = File(open('test.jpg','r'))
                    image = Image(residence=residence)
                    image.photo = f

                    #image = deepcopy(Image.objects.all()[0])
                    #image.pk = None
                    #image.residence = residence
                    image.save()
                    index_image = index_image - 1
        index_departement = index_departement - 1

