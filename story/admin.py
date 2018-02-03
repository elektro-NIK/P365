from django.contrib import admin

from . import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'user',)
    list_filter = ('user',)
    ordering = ('-created',)
    search_fields = ('title', 'text',)


class StoryAdmin(admin.ModelAdmin):
    list_display = ('track', 'article', 'event', 'created', 'user',)
    list_filter = ('user',)
    ordering = ('-created',)
    search_fields = ('track', 'article', 'event',)


admin.site.register(models.ArticleModel, ArticleAdmin)
admin.site.register(models.StoryModel, StoryAdmin)
