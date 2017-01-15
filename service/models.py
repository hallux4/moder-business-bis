# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangocms_text_ckeditor.fields import HTMLField


@python_2_unicode_compatible
class Service(models.Model):
    service_name = models.CharField(max_length=100, blank=False)
    description = HTMLField(blank=True)

    def __str__(self):
        return "- %s" % (self.service_name)
