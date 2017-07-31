# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin

from article.models import Article, Category

admin.site.register(Article)
admin.site.register(Category)
# Register your models here.
