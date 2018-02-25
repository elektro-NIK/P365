from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from track import models


class TrackAdmin(LeafletGeoAdmin):
    list_display = ('name', 'created', 'start_date', 'finish_date', 'activity', 'public', 'is_active', 'length', 'user',)
    list_filter = ('user', 'activity', 'public', 'is_active',)
    ordering = ('-created',)
    search_fields = ('name', 'description',)


admin.site.register(models.TrackModel, TrackAdmin)
