# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangocms_text_ckeditor.fields import HTMLField
from datetime import datetime

@python_2_unicode_compatible
class Annonces(models.Model):
    annonces_name = models.CharField(max_length=40)
    description = HTMLField(blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    link_url = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return "%s, %s" % (self.date, self.annonces_name)

