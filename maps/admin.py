from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from . import models

admin.site.register(models.POIModel, LeafletGeoAdmin)
admin.site.register(models.TrackModel, LeafletGeoAdmin)
