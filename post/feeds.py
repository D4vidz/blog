#!/usr/bin/env python
# -*- coding:utf-8 -*-


from django.contrib.syndication.views import Feed
from .models import Blog


class AllBlogRssFeed(Feed):

    title = 'ZZY个人博客'
    link = '/'
    description = 'ZZY博客文章'

    def items(self):
        return Blog.objects.all()

    def item_title(self, item):
        return '%s' % item.title

    def item_description(self, item):
        return item.content
