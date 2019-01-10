from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

from P365.settings import MAX_LENGTH
from calendar_year.models import EventModel
from map.models import TrackModel


class StoryModel(models.Model):
    title = models.CharField(max_length=MAX_LENGTH['title'])
    text = models.TextField(max_length=MAX_LENGTH['text'])
    track = models.ForeignKey(TrackModel, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
