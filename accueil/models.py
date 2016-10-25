# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangocms_text_ckeditor.fields import HTMLField


@python_2_unicode_compatible
class Banniere(models.Model):
    banniere_name = models.CharField(max_length=40)

    def __str__(self):
        return self.banniere_name


@python_2_unicode_compatible
class Image(models.Model):
    banniere_name = models.ForeignKey(Banniere, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='accueil')
    description = HTMLField(blank=True)

    def __str__(self):
        return "%s %s" % (self.photo, self.banniere_name)
