# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangocms_text_ckeditor.fields import HTMLField


@python_2_unicode_compatible
class Presentation(models.Model):
    presentation_name = models.CharField(max_length=40)
    description = HTMLField(blank=True)

    def __str__(self):
        return self.presentation_name

