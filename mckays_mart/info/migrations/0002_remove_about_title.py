# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 23:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='title',
        ),
    ]