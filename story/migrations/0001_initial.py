# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0002_auto_20171119_2041'),
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='story.Article')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profile.Event')),
                ('track', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maps.Track')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('story', models.ManyToManyField(to='story.Story')),
            ],
        ),
    ]
