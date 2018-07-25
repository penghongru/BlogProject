# -*- coding: utf-8 -*-

# @Time    : 2018/7/25 10:24

# @Author  : hongru

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

# @Project : BlogProject

# @FileName: feeds.py

# @Software: PyCharm
from django.contrib.syndication.views import Feed

from .models import Post


class AllPostsRssFeed(Feed):
    title = 'Django 博客教程 演示项目'
    link = "/"
    description = "Django 博客教程演示项目测试文章 "

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s]%s' % (item.category, item.title)

    def item_description(self, item):
        return item.body
