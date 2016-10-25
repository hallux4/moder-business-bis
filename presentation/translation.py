#!/usr/bin/env python
# coding=utf-8

from modeltranslation.translator import translator, TranslationOptions
from presentation.models import Presentation

class TextTranslationOptions(TranslationOptions):
        fields = ('description',)
#        fallback_values = _('-- sorry, no translation provided --')

translator.register(Presentation, TextTranslationOptions)

