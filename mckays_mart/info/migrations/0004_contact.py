# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_about_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('phone', models.CharField(help_text='Please write in the form (08) 82xx-xxxx to be smartphone link', max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
