# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from autoslug import AutoSlugField

@python_2_unicode_compatible
class Department(models.Model):
    departement_name = models.CharField(max_length=40)
    slug = AutoSlugField(populate_from='departement_name', unique=True, allow_unicode=True)
    def __str__(self):
        return self.departement_name


@python_2_unicode_compatible
class City(models.Model):
    departement = models.ForeignKey(Department, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=40)
    slug = AutoSlugField(populate_from='city_name', unique=True, allow_unicode=True)

    def __str__(self):
        return "%s, %s" % (self.city_name, self.departement)


@python_2_unicode_compatible
class Residence(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    residence_name = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    note = models.CharField(max_length=200,default=".")
    slug = AutoSlugField(populate_from='residence_name', unique=True, allow_unicode=True)

    def __str__(self):
        return "%s, %s" % (self.residence_name, self.city)


@python_2_unicode_compatible
class Ecole(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    ecole = models.CharField(max_length=50)
    distance = models.IntegerField(default=0)
    waypath = models.CharField(max_length=100,default=".")
    geo_lat = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    geo_long = models.DecimalField(max_digits=10, decimal_places=6, default=0)


    def __str__(self):
        return "%s, %s" % (self.ecole, self.residence)

class Image(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='rent_lookup')

    def __str__(self):
        return "%s, %s" % (self.photo, self.residence)

@python_2_unicode_compatible
class Logement(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    rent_type = models.CharField(max_length=20)
    m2_min = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    m2_max = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    charge_min = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    charge_max = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    caution = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    geo_lat = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    geo_long = models.DecimalField(max_digits=10, decimal_places=6, default=0)


    def __str__(self):
        return "%s, %s" % (self.rent_type, self.residence)

