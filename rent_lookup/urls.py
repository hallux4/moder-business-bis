#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<department_id>[0-9]+)/(?P<city_id>[0-9]+)/(?P<residence_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<department_id>[0-9]+)/(?P<city_id>[0-9]+)/$', views.city, name='city'),
    url(r'^(?P<department_id>[0-9]+)/$', views.department, name='department'),
    url(r'^$', views.globalize, name='globalize'),
    #url(r'^details$', detailsList.as_view()),
]
