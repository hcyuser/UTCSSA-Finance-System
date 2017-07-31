# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
class Category(models.Model):
    name = models.CharField(u'Name', max_length=50)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.TextField(u'購買品項(EX: 蘇打餅X1)')
    uid = models.CharField(u'學號',default='0',max_length=10)
    filldate =  models.DateTimeField(u'Date YYYY-MM-DD',default=datetime.now)
    applycost = models.CharField(u'請款金額',default='0',max_length=8)
    content = models.TextField(u'事由')

    category = models.ForeignKey('Category', blank=True, null=True)

    def __unicode__(self):
        return self.title
