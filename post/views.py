#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import markdown
from markdown.extensions.toc import TocExtension

from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.text import slugify

from post.models import Blog

# Create your views here.


def index(request):
    blog_list = Blog.objects.all()
    per_page = 5
    page_num = request.GET.get('page', 1)
    data = {}
    paginate_queryset(blog_list, per_page, page_num, data)
    return render(request, 'blog/list.html', context=data)


def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.increase_views()

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        TocExtension(slugify=slugify)
    ])
    blog.content = md.convert(blog.content)
    blog.toc = md.toc
    try:
        previous_blog = Blog.objects.get(id=int(blog_id) - 1)
    except Blog.DoesNotExist:
        previous_blog = None
    try:
        next_blog = Blog.objects.get(id=int(blog_id) + 1)
    except Blog.DoesNotExist:
        next_blog = None
    return render(request, 'blog/detail.html', locals())


def archives(request, year, month):
    """
    get blog by year and month
    :param request:
    :param year:
    :param month:
    :return:
    """
    blog_list = Blog.objects.filter(
        ctime__year=year, ctime__month=month
    )
    per_page = 10
    page_num = request.GET.get('page', 1)
    data = {}
    paginate_queryset(blog_list, per_page, page_num, data)
    return render(request, 'blog/list.html', context=data)


def tag_blog(request, tag):
    """
    find all blogs by a tag
    :param request:
    :param tag:
    :return:
    """
    blog_list = Blog.objects.filter(tag__name=tag)
    per_page = 10
    page_num = request.GET.get('page', 1)
    data = {}
    paginate_queryset(blog_list, per_page, page_num, data)
    return render(request, 'blog/list.html', context=data)


def paginate_queryset(queryset, per_page, page_num, data):
    # there is a paginator for paginate result
    paginator = Paginator(queryset, per_page)
    # notify page and make the result of this page
    page = paginator.page(page_num)
    # the num of all pages
    total_page_num = paginator.num_pages
    # which page i am
    now_page = page.number
    previous_page = page.previous_page_number() if page.has_previous() else None
    next_page = page.next_page_number() if page.has_next() else None
    blog_list = page.object_list
    data.update({
        'total_page_num': total_page_num, 'now_page': now_page,
        'previous_page': previous_page, 'next_page': next_page,
        'blog_list': blog_list
    })
