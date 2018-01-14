from django.contrib.auth.models import User
from django.db import models

from P365.settings import MAX_LENGTH
from maps.models import TrackModel
from calendar_year.models import Event


class Article(models.Model):
    title = models.CharField(max_length=MAX_LENGTH['title'])
    text = models.TextField(max_length=MAX_LENGTH['text'])
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Story(models.Model):
    track = models.ForeignKey(TrackModel, null=True)
    article = models.OneToOneField(Article)
    event = models.OneToOneField(Event)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.event, self.article, self.track


class Tag(models.Model):
    name = models.CharField(max_length=MAX_LENGTH['name'], unique=True)
    story = models.ManyToManyField(Story)

    def __str__(self):
        return self.name
