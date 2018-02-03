from django.contrib import admin

from . import models


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created',)
    ordering = ('-name',)
    search_fields = ('name',)


admin.site.register(models.TagModel, TagAdmin)
