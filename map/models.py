from django.contrib.auth.models import User
from django.contrib.gis.db import models
from tagulous.models import SingleTagField

from P365.settings import MAX_LENGTH
from tag.models import TagModel


class POIModel(models.Model):
    # Basic
    name = models.CharField(max_length=MAX_LENGTH['name'])
    description = models.TextField(max_length=MAX_LENGTH['description'], null=True)
    # Relations
    user = models.ForeignKey(User)
    tag = SingleTagField(TagModel)
    # Datetime
    created = models.DateTimeField(auto_now_add=True)
    # Flags
    public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # Feature
    geom = models.PointField(dim=3)

    objects = models.Manager()

    def __str__(self):
        return self.name

    @property
    def longitude(self):
        return self.geom.x

    @property
    def latitude(self):
        return self.geom.y

    @property
    def altitude(self):
        return self.geom.z


class RouteModel(models.Model):
    # Basic
    name = models.CharField(max_length=MAX_LENGTH['name'])
    description = models.TextField(max_length=MAX_LENGTH['description'], blank=True)
    # Relations
    user = models.ForeignKey(User)
    tag = SingleTagField(force_lowercase=True, autocomplete_view='poi_tag_autocomplete')
    # Datetime
    created = models.DateTimeField(auto_now_add=True)
    # Distance
    length = models.FloatField(default=0)
    # Altitudes
    altitude_gain = models.FloatField(default=0)
    altitude_loss = models.FloatField(default=0)
    altitude_max = models.FloatField(default=0)
    altitude_min = models.FloatField(default=0)
    # Flags
    public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # Feature
    geom = models.LineStringField(dim=3)

    objects = models.Manager()

    def __str__(self):
        return self.name


class TrackModel(models.Model):
    # Basic
    name = models.CharField(max_length=MAX_LENGTH['name'])
    description = models.TextField(max_length=MAX_LENGTH['description'], null=True)
    # Relations
    user = models.ForeignKey(User)
    tag = SingleTagField(force_lowercase=True, autocomplete_view='poi_tag_autocomplete')
    # Datetime
    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    # Distance
    length = models.FloatField(default=0)
    # Speed
    speed = models.FloatField(default=0)
    speed_max = models.FloatField(default=0)
    # Altitudes
    altitude_gain = models.FloatField(default=0)
    altitude_loss = models.FloatField(default=0)
    altitude_max = models.FloatField(default=0)
    altitude_min = models.FloatField(default=0)
    # Flags
    public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # Feature
    geom = models.MultiLineStringField(dim=3)

    objects = models.Manager()

    def __str__(self):
        return self.name
