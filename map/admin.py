from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from map import models


class TrackAdmin(LeafletGeoAdmin):
    list_display = ('name', 'created', 'start_date', 'finish_date', 'public', 'is_active', 'length', 'user',)
    list_filter = ('user', 'public', 'is_active',)
    ordering = ('-created',)
    search_fields = ('name', 'description',)


class RouteAdmin(LeafletGeoAdmin):
    list_display = ('name', 'created', 'public', 'is_active', 'length', 'user',)
    list_filter = ('user', 'public', 'is_active',)
    ordering = ('-created',)
    search_fields = ('name', 'description',)


class POIAdmin(LeafletGeoAdmin):
    list_display = ('name', 'created', 'user', 'is_active',)
    list_filter = ('user', 'is_active',)
    ordering = ('-created',)
    search_fields = ('name', 'description',)


admin.site.register(models.POIModel, POIAdmin)
admin.site.register(models.TrackModel, TrackAdmin)
admin.site.register(models.RouteModel, RouteAdmin)
