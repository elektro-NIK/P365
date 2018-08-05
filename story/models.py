from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

from P365.settings import MAX_LENGTH
from calendar_year.models import EventModel
from map.models import TrackModel


class ArticleModel(models.Model):
    title = models.CharField(max_length=MAX_LENGTH['title'])
    text = models.TextField(max_length=MAX_LENGTH['text'])
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.title


class StoryModel(models.Model):
    track = models.ForeignKey(TrackModel, on_delete=models.CASCADE, null=True, blank=True)
    article = models.OneToOneField(ArticleModel, on_delete=models.CASCADE)
    event = models.OneToOneField(EventModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'{self.event} {self.article} {self.track}'
