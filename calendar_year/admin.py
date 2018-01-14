from django.contrib import admin
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'finish_date', 'user')
    list_filter = ('user',)
    ordering = ('-start_date',)
    search_fields = ('name', 'description',)


admin.site.register(models.Event, EventAdmin)
