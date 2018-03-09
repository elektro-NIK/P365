from django.contrib.auth.models import User
from django.contrib.gis.db import models

from P365.settings import MAX_LENGTH


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
    geom = models.PointField()

    objects = models.Manager()

    def __str__(self):
        return self.name
