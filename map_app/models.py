from django.db import models

from django.contrib.gis.db import models as gismodels
from django.contrib.auth.models import User


class POIModel(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField(max_length=256)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    geom = gismodels.PointField()

    def __str__(self):
        return self.name


class TrackModel(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    geom = gismodels.LineStringField()

    def __str__(self):
        return self.name
