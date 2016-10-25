#!/usr/bin/env python
# coding=utf-8

from modeltranslation.translator import translator, TranslationOptions
from service.models import Service

class ServiceTranslationOptions(TranslationOptions):
        fields = ('description',)
#        fallback_values = _('-- sorry, no translation provided --')

translator.register(Service, ServiceTranslationOptions)

