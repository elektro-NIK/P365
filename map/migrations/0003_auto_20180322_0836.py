# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20180314_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routemodel',
            name='description',
            field=models.TextField(blank=True, default='', max_length=250),
            preserve_default=False,
        ),
    ]
