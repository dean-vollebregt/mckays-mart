# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20170106_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='bathroom',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bedroom',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dining',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hallway',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='living',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='musical',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='office',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
