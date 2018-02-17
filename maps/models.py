from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models as gismodels

from P365.settings import MAX_LENGTH
from hashtag.models import TagModel


class POIModel(models.Model):
    # General
    name = models.CharField(max_length=MAX_LENGTH['name'])
    description = models.TextField(max_length=MAX_LENGTH['description'], blank=True)
    # Inside
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    # Properties
    is_active = models.BooleanField(default=True)
    # GIS
    geom = gismodels.PointField()

    def __str__(self):
        return self.name


class TrackModel(models.Model):
    # General
    name = models.CharField(max_length=MAX_LENGTH['name'])
    description = models.TextField(max_length=MAX_LENGTH['description'], blank=True)
    # Inside
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    # Outside
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    length = models.FloatField(default=0)
    speed = models.FloatField(default=0)
    altitude_gain = models.FloatField(default=0)
    altitude_loss = models.FloatField(default=0)
    # Properties
    activity = models.ForeignKey(TagModel, default=1)
    public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # GIS
    geom = gismodels.LineStringField()

    def __str__(self):
        return self.name
