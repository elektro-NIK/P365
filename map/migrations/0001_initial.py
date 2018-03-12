# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-12 10:38
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hashtag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='POIModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=250, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('public', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hashtag.TagModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RouteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=250, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('length', models.FloatField(default=0)),
                ('altitude_gain', models.FloatField(default=0)),
                ('altitude_loss', models.FloatField(default=0)),
                ('altitude_max', models.FloatField(default=0)),
                ('altitude_min', models.FloatField(default=0)),
                ('public', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(dim=3, srid=4326)),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hashtag.TagModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrackModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=250, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField()),
                ('finish_date', models.DateTimeField()),
                ('length', models.FloatField(default=0)),
                ('speed', models.FloatField(default=0)),
                ('speed_max', models.FloatField(default=0)),
                ('altitude_gain', models.FloatField(default=0)),
                ('altitude_loss', models.FloatField(default=0)),
                ('altitude_max', models.FloatField(default=0)),
                ('altitude_min', models.FloatField(default=0)),
                ('public', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(dim=3, srid=4326)),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hashtag.TagModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
