from django.contrib import admin
from .models import EventModel


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'finish_date', 'is_active', 'user',)
    list_filter = ('user', 'is_active',)
    ordering = ('-start_date',)
    search_fields = ('name', 'description',)


admin.site.register(EventModel, EventAdmin)
