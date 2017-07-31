# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(u'Name', max_length=50)

    def __unicode__(self):
        return self.name


class Payment(models.Model):
    name = models.CharField(u'姓名', max_length=50)
    uid = models.CharField(u'學號', max_length=10)
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    gender = models.CharField(u'生理性別',max_length=1, choices=GENDER_CHOICES)
    CSSA_PAY = (
        ('0131', '國泰世華商業銀行CUCB 轉帳'),
        ('0132', '國泰世華商業銀行CUCB 無摺存款'),
        ('8221', '中國信託CTBC 轉帳'),
        ('8222', '中國信託CTBC 無摺存款'),
        ('7001', '中華郵政Chunghwa Post 轉帳'),
        ('7002', '中華郵政Chunghwa Post 無摺存款'),
        ('9999', '親自收款'),
    )
    paymentway = models.CharField(u'付款方式',max_length=4, choices=CSSA_PAY)
    CAMP = (
        ('Y', '參加宿營'),
        ('N', '不參加宿營'),

    )
    choicecamp = models.CharField(u'宿營意願',max_length=1, choices=CAMP)
    money = models.CharField(u'繳交金額', max_length=5)
    category = models.ForeignKey('Category', blank=True, null=True)
    def __unicode__(self):
        return self.uid


# Create your models here.
