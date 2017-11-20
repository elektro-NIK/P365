from django.db import models
from django.contrib.gis.db import models as gismodels

from P365.settings import MAX_LENGTH


class Track(models.Model):
    name = models.CharField(max_length=MAX_LENGTH['name'])
    description = models.TextField(max_length=MAX_LENGTH['description'], blank=True)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    public = models.BooleanField(default=False)
    length = models.FloatField()
    geom = gismodels.LineStringField()
