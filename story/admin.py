from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . import models


class StoryAdmin(admin.ModelAdmin):
    summernote_fields = ('text',)
    list_display = ('title', 'event', 'track', 'created', 'user',)
    list_filter = ('user',)
    ordering = ('-created',)
    search_fields = ('title', 'text', 'track', 'event',)


admin.site.register(models.StoryModel, StoryAdmin)
