# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-01 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
