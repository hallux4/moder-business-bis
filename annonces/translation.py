#!/usr/bin/env python
# coding=utf-8

from modeltranslation.translator import translator, TranslationOptions
from annonces.models import Annonces


class AnnoncesTranslationOptions(TranslationOptions):
        fields = ('description', 'annonces_name',)
#        fallback_values = _('-- sorry, no translation provided --')

translator.register(Annonces, AnnoncesTranslationOptions)

