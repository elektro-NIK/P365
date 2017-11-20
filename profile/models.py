from django.contrib.auth.models import User
from django.db import models

from P365.settings import MAX_LENGTH


class Event(models.Model):
    name = models.CharField(max_length=MAX_LENGTH['name'])
    description = models.TextField(max_length=MAX_LENGTH['description'], blank=True)
    start_date = models.DateField()
    finish_date = models.DateField()
    user = models.ForeignKey(User)
