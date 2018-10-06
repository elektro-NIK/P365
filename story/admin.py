from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from . import models


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ('title', 'created', 'user',)
    list_filter = ('user',)
    ordering = ('-created',)
    search_fields = ('title', 'text',)


class StoryAdmin(admin.ModelAdmin):
    list_display = ('event', 'track', 'article', 'created', 'user',)
    list_filter = ('user',)
    ordering = ('-created',)
    search_fields = ('track', 'article', 'event',)


admin.site.register(models.ArticleModel, ArticleAdmin)
admin.site.register(models.StoryModel, StoryAdmin)
