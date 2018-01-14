from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from . import models


class POIAdmin(LeafletGeoAdmin):
    list_display = ('name', 'created', 'user',)
    list_filter = ('user',)
    ordering = ('-created',)
    search_fields = ('name', 'description',)


class TrackAdmin(LeafletGeoAdmin):
    list_display = ('name', 'created', 'start_date', 'finish_date', 'public', 'length', 'user',)
    list_filter = ('user', 'public',)
    ordering = ('-created',)
    search_fields = ('name', 'description',)


admin.site.register(models.POIModel, POIAdmin)
admin.site.register(models.TrackModel, TrackAdmin)
