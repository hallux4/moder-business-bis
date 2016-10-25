#!/usr/bin/env python
# coding=utf-8

from modeltranslation.translator import translator, TranslationOptions
from accueil.models import Image


class ImageTranslationOptions(TranslationOptions):
        fields = ('description',)
#        fallback_values = _('-- sorry, no translation provided --')

translator.register(Image, ImageTranslationOptions)

