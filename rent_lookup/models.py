# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangocms_text_ckeditor.fields import HTMLField
#@python_2_unicode_compatible
#class Department(models.Model):
#    departement_name = models.CharField(max_length=40)
#    def __str__(self):
#        return self.departement_name

@python_2_unicode_compatible
class City(models.Model):
#    departement = models.ForeignKey(Department, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=40)

    def __str__(self):
        return "%s" % (self.city_name)

@python_2_unicode_compatible
class Residence(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    residence_name = models.CharField(max_length=100)
    description = HTMLField(blank=False)
    note = HTMLField(blank=True)

    def __str__(self):
        return "%s, %s" % (self.residence_name, self.city)


@python_2_unicode_compatible
class Ecole(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    ecole = models.CharField(max_length=100)
    distance = models.IntegerField(default=0)
    waypath = HTMLField(blank=False)

    def __str__(self):
        return "%s, %s" % (self.ecole, self.residence)

class Image(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='rent_lookup',blank=False, default='rent_lookup/no-image-available.jpg')

    def __str__(self):
        return "%s, %s" % (self.photo, self.residence)

@python_2_unicode_compatible
class Logement(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    rent_type = models.CharField(max_length=50)
    m2_min = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    m2_max = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    charge_min = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    charge_max = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    caution = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    frais_dossier = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return "%s, %s" % (self.rent_type, self.residence)

@python_2_unicode_compatible
class Categorie(models.Model):
    home = models.CharField(max_length=30)
    recherche = models.CharField(max_length=30)
    description_detail = models.CharField(max_length=30)
    type_logement = models.CharField(max_length=30)
    superficie_logement = models.CharField(max_length=30)
    loyer_logement = models.CharField(max_length=30)
    caution = models.CharField(max_length=30)
    note = models.CharField(max_length=30, default="note")
    more = models.CharField(max_length=30, default="more")
    frais_de_dossier = models.CharField(max_length=30)
    ecole_nom = models.CharField(max_length=30)
    ecole_distance = models.CharField(max_length=30)
    chemin_ecole = models.CharField(max_length=30)

    def __str__(self):
        return "%s" % (self.home)


