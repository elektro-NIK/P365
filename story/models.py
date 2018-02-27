from django.contrib.auth.models import User
from django.db import models

from P365.settings import MAX_LENGTH
from hashtag.models import TagModel
from track.models import TrackModel
from calendar_year.models import EventModel


class ArticleModel(models.Model):
    title = models.CharField(max_length=MAX_LENGTH['title'])
    text = models.TextField(max_length=MAX_LENGTH['text'])
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    objects = models.Manager()

    def __str__(self):
        return self.title


class StoryModel(models.Model):
    track = models.ForeignKey(TrackModel, null=True)
    article = models.OneToOneField(ArticleModel)
    event = models.OneToOneField(EventModel)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(TagModel)
    user = models.ForeignKey(User)

    objects = models.Manager()

    def __str__(self):
        return '{} {} {}'.format(self.event, self.article, self.track)
