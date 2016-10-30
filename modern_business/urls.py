# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.http import HttpResponse
from accueil import views

admin.autodiscover()

urlpatterns = i18n_patterns('',
    (r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
    url(r'^admin-lecheng-location/', include(admin.site.urls)),
    url(r'^_nested_admin/', include('nested_admin.urls')),
    url(r'^$', views.accueilpage, name='accueilpage'),
    url(r'^rent_lookup/', include('rent_lookup.urls')),
    url(r'^accueil/', include('accueil.urls')),
    url(r'^presentation/', include('presentation.urls')),
    url(r'^service/', include('service.urls')),
    url(r'^annonces/', include('annonces.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^', include('cms.urls')),
)

