# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(help_text='Please write in the form (08) 8271-2477', max_length=50),
        ),
    ]