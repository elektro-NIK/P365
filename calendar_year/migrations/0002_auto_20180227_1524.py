# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_year', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='finish_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
