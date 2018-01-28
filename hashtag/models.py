from django.db import models

from P365.settings import MAX_LENGTH


class TagModel(models.Model):
    name = models.CharField(max_length=MAX_LENGTH['tag'])
