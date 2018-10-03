#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.index, name='blog_list'),
    url(r'^blog/(?P<blog_id>\d+)/', views.detail, name='blog_detail'),
    url(r'^blog/archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^blog/tag/(?P<tag>.*)/$', views.tag_blog, name='tag'),
]
