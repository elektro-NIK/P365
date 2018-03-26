from django.contrib.auth.models import User
from django.db import models
from tagulous.models import TagField

from P365.settings import MAX_LENGTH
from calendar_year.models import EventModel
from map.models import TrackModel
from tag.models import TagModel


class ArticleModel(models.Model):
    title = models.CharField(max_length=MAX_LENGTH['title'])
    text = models.TextField(max_length=MAX_LENGTH['text'])
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    objects = models.Manager()

    def __str__(self):
        return self.title


class StoryModel(models.Model):
    track = models.ForeignKey(TrackModel, null=True, blank=True)
    article = models.OneToOneField(ArticleModel)
    event = models.OneToOneField(EventModel)
    created = models.DateTimeField(auto_now_add=True)
    tags = TagField(TagModel)
    user = models.ForeignKey(User)

    objects = models.Manager()

    def __str__(self):
        return f'{self.event} {self.article} {self.track}'
