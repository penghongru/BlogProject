# -*- coding: utf-8 -*-

# @Time    : 2018/7/25 13:16

# @Author  : hongru

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

# @Project : BlogProject

# @FileName: search_indexes.py

# @Software: PyCharm
from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
