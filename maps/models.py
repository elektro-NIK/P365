from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models as gismodels

from P365.settings import MAX_LENGTH
from hashtag.models import TagModel


class POIModel(models.Model):
    name = models.CharField(max_length=MAX_LENGTH['name'])
    description = models.TextField(max_length=MAX_LENGTH['description'], blank=True)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    geom = gismodels.PointField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TrackModel(models.Model):
    name = models.CharField(max_length=MAX_LENGTH['name'])
    description = models.TextField(max_length=MAX_LENGTH['description'], blank=True)
    user = models.ForeignKey(User)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    length = models.FloatField()
    activity = models.ForeignKey(TagModel, null=True)
    geom = gismodels.LineStringField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
