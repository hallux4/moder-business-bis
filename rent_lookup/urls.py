#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<city_id>[0-9]+)/(?P<residence_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<city_id>[0-9]+)/$', views.residence, name='residence'),
    url(r'^$', views.city, name='city'),
    #url(r'^$', views.globalize, name='globalize'),
]
