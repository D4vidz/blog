#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import template

from post.models import Blog, Tag


register = template.Library()


@register.simple_tag
def recent_blogs(num=5):
    return Blog.objects.all()[:num]


@register.simple_tag
def archives():
    return Blog.objects.dates('ctime', 'month', order='DESC')


@register.simple_tag
def tags():
    return Tag.objects.all()
