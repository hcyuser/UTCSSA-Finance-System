# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='applycost',
            field=models.CharField(default='0', max_length=8, verbose_name='ApplyCost'),
        ),
        migrations.AddField(
            model_name='article',
            name='filldate',
            field=models.CharField(default='00000000', max_length=8, verbose_name='Filldate'),
        ),
        migrations.AddField(
            model_name='article',
            name='uid',
            field=models.CharField(default='0', max_length=10, verbose_name='UID'),
        ),
    ]
