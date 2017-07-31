# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from cssapayment.models import Payment
from cssapayment.models import Category
admin.site.register(Payment)
admin.site.register(Category)
# Register your models here.
