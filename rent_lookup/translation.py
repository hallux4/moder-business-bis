#!/usr/bin/env python
# coding=utf-8

from modeltranslation.translator import translator, TranslationOptions
from rent_lookup.models import Department, City, Residence, Ecole, Logement


class DepartmentTranslationOptions(TranslationOptions):
        fields = ('departement_name',)
#        fallback_values = _('-- sorry, no translation provided --')

class CityTranslationOptions(TranslationOptions):
        fields = ('city_name',)
#        fallback_values = _('-- sorry, no translation provided --')

class ResidenceTranslationOptions(TranslationOptions):
        fields = ('residence_name', 'description', 'note',)
#        fallback_values = _('-- sorry, no translation provided --')

class EcoleTranslationOptions(TranslationOptions):
        fields = ('ecole',)
#        fallback_values = _('-- sorry, no translation provided --')

class LogementTranslationOptions(TranslationOptions):
        fields = ('rent_type',)
#        fallback_values = _('-- sorry, no translation provided --')

translator.register(Department, DepartmentTranslationOptions)
translator.register(City, CityTranslationOptions)
translator.register(Residence, ResidenceTranslationOptions)
translator.register(Ecole, EcoleTranslationOptions)
translator.register(Logement, LogementTranslationOptions)

