from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from . import models


class POIAdmin(LeafletGeoAdmin):
    list_display = ('name', 'created', 'user', 'is_active',)
    list_filter = ('user', 'is_active',)
    ordering = ('-created',)
    search_fields = ('name', 'description',)


admin.site.register(models.POIModel, POIAdmin)
