#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<residence_id>[0-9]+)/$', views.details, name='details'),
    url(r'^$', views.city, name='city'),
]
