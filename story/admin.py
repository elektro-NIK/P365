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


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    ordering = ('-name',)
    search_fields = ('name',)


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Story, StoryAdmin)
admin.site.register(models.Tag, TagAdmin)
