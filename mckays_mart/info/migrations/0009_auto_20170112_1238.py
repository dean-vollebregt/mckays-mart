# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 02:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_auto_20170112_1236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name_plural': 'Home'},
        ),
    ]
